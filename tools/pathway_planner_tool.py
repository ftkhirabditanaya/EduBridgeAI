"""Explainable student pathway planning from EduBridge's local catalogs."""

import math
import os
import re
import csv


DATABASE_DIR = os.path.join(os.path.dirname(__file__), "..", "database")
DIFFICULTY_HOURS = {"easy": 6, "medium": 12, "hard": 20}
DIFFICULTY_ORDER = {"easy": 0, "medium": 1, "hard": 2}


def _normalize(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def _items(value):
    if not value:
        return []
    return [item.strip() for item in str(value).split(",") if item.strip()]


def _load_catalog(filename):
    path = os.path.join(DATABASE_DIR, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Required pathway planning data not found: {path}")
    with open(path, newline="", encoding="utf-8-sig") as catalog_file:
        return list(csv.DictReader(catalog_file))


def _find_career(goal, careers):
    normalized_goal = _normalize(goal)
    for career in careers:
        name = _normalize(career.get("career", ""))
        if normalized_goal == name or normalized_goal in name or name in normalized_goal:
            return career

    terms = [term for term in normalized_goal.split() if len(term) > 2]
    ranked = []
    for career in careers:
        searchable = _normalize(
            " ".join(
                str(career.get(field, ""))
                for field in ("career", "description", "domain", "required_skills")
            )
        )
        matches = [term for term in terms if term in searchable.split()]
        if matches:
            ranked.append((len(matches), career))

    if not ranked:
        available = ", ".join(str(item.get("career", "")) for item in careers)
        raise ValueError(f"No catalog career matched '{goal}'. Choose from: {available}")
    return max(ranked, key=lambda item: item[0])[1]


def _difficulty(skill, skill_catalog):
    normalized = _normalize(skill)
    for item in skill_catalog:
        if _normalize(item.get("skill", "")) == normalized:
            return str(item.get("difficulty", "Medium")).lower()
    return "medium"


def _select_project(required_skills, gaps, projects):
    planned_skills = {_normalize(skill) for skill in required_skills}
    gap_skills = {_normalize(skill) for skill in gaps}
    ranked = []

    for project in projects:
        project_skills = _items(project.get("skills", ""))
        matched = [
            skill for skill in project_skills
            if _normalize(skill) in planned_skills
        ]
        gap_matches = [
            skill for skill in matched
            if _normalize(skill) in gap_skills
        ]
        ranked.append((len(gap_matches), len(matched), project, matched))

    if not ranked:
        return None

    _, _, project, matched = max(ranked, key=lambda item: (item[0], item[1]))
    return {
        "name": project.get("project", "Portfolio project"),
        "domain": project.get("domain", ""),
        "difficulty": project.get("difficulty", "Medium"),
        "skills": _items(project.get("skills", "")),
        "matched_skills": matched,
        "reason": (
            f"Builds {', '.join(matched)} from the target career requirements."
            if matched else "Closest project in the local catalog to your target career."
        ),
    }


def _rank_internships(required_skills, current_skills, internships, location):
    known = {_normalize(skill) for skill in current_skills}
    target = {_normalize(skill) for skill in required_skills}
    ranked = []

    for internship in internships:
        skills = _items(internship.get("skills", ""))
        matched = [
            skill for skill in skills
            if _normalize(skill) in known or _normalize(skill) in target
        ]
        missing = [skill for skill in skills if _normalize(skill) not in known]
        score = round(100 * len(matched) / len(skills)) if skills else 0
        location_match = bool(
            location
            and _normalize(location) in _normalize(internship.get("location", ""))
        )
        ranked.append((score, location_match, internship, matched, missing))

    ranked.sort(key=lambda item: (item[0], item[1]), reverse=True)
    results = []
    for score, location_match, internship, matched, missing in ranked[:3]:
        reasons = []
        if matched:
            reasons.append(f"shares target skills: {', '.join(matched)}")
        if location_match:
            reasons.append(f"matches preferred location ({location})")
        results.append({
            "company": internship.get("company", ""),
            "role": internship.get("role", ""),
            "location": internship.get("location", ""),
            "stipend": internship.get("stipend", ""),
            "apply_link": internship.get("apply_link", ""),
            "match_score": score,
            "matched_skills": matched,
            "skills_to_build": missing,
            "reason": "; ".join(reasons) or "Listed in the local internship catalog.",
        })
    return results


def _rank_funding(career, education_stage, scholarships):
    career_text = _normalize(
        " ".join(str(career.get(field, "")) for field in ("career", "degree", "stream"))
    )
    stage = _normalize(education_stage)
    ranked = []

    for scholarship in scholarships:
        eligibility = str(scholarship.get("eligibility", ""))
        normalized_eligibility = _normalize(eligibility)
        reasons = []

        if "engineering" in normalized_eligibility and "engineering" in career_text:
            reasons.append("eligibility mentions engineering")
        if (
            ("ug" in normalized_eligibility or "undergraduate" in normalized_eligibility)
            and ("undergraduate" in stage or "college" in stage)
        ):
            reasons.append("eligibility mentions undergraduate study")
        if "merit" in normalized_eligibility:
            reasons.append("merit-based criteria may apply")
        if "technical" in normalized_eligibility and (
            "engineering" in career_text or "technical" in career_text
        ):
            reasons.append("eligibility mentions technical education")

        amount = scholarship.get("amount", 0)
        try:
            amount = int(float(amount))
        except (TypeError, ValueError):
            amount = 0

        ranked.append((bool(reasons), amount, scholarship, reasons))

    ranked.sort(key=lambda item: (item[0], item[1]), reverse=True)
    return [
        {
            "name": item.get("scholarship", ""),
            "eligibility": item.get("eligibility", ""),
            "amount": int(float(item.get("amount", 0) or 0)),
            "deadline": item.get("last_date", ""),
            "fit": "Potential fit" if reasons else "Review eligibility",
            "reason": "; ".join(reasons) or (
                "The local catalog has no verified profile match; review the criteria."
            ),
        }
        for has_reasons, _, item, reasons in ranked[:3]
    ]


def create_pathway_plan(
    goal,
    current_skills,
    education_stage,
    weekly_hours,
    monthly_budget,
    months,
    stream="",
    location="",
    careers=None,
    projects=None,
    scholarships=None,
    internships=None,
    skill_catalog=None,
):
    """Create an explainable roadmap from a career target and student constraints."""
    if not str(goal).strip():
        raise ValueError("A career goal is required.")
    if weekly_hours <= 0 or months <= 0 or monthly_budget < 0:
        raise ValueError("Study hours and timeline must be positive; budget cannot be negative.")

    careers = careers if careers is not None else _load_catalog("careers.csv")
    projects = projects if projects is not None else _load_catalog("projects.csv")
    scholarships = scholarships if scholarships is not None else _load_catalog("scholarships.csv")
    internships = internships if internships is not None else _load_catalog("internships.csv")
    skill_catalog = skill_catalog if skill_catalog is not None else _load_catalog("skills.csv")

    career = _find_career(goal, careers)
    required_skills = _items(career.get("required_skills", ""))
    current_by_key = {_normalize(skill): skill.strip() for skill in current_skills if skill.strip()}
    already_have = [
        skill for skill in required_skills if _normalize(skill) in current_by_key
    ]
    gaps = [
        skill for skill in required_skills if _normalize(skill) not in current_by_key
    ]
    gaps.sort(
        key=lambda skill: (
            DIFFICULTY_ORDER.get(_difficulty(skill, skill_catalog), 1),
            required_skills.index(skill),
        )
    )

    estimated_hours = sum(
        DIFFICULTY_HOURS.get(_difficulty(skill, skill_catalog), 12) for skill in gaps
    )
    estimated_hours += 24 if gaps else 12
    available_hours = weekly_hours * 4 * months
    minimum_months = max(1, math.ceil(estimated_hours / (weekly_hours * 4)))

    project = _select_project(required_skills, gaps, projects)
    internship_matches = _rank_internships(
        required_skills, current_skills, internships, location
    )
    funding = _rank_funding(career, education_stage, scholarships)

    milestones = [
        {
            "title": "Close the highest-priority skill gaps",
            "timeframe": f"Weeks 1-{max(1, min(months * 2, minimum_months * 2))}",
            "action": (
                f"Study {', '.join(gaps)} in this order."
                if gaps else "Refresh your existing skills and document evidence for each one."
            ),
            "deliverable": (
                "A small practice artifact or notes for each skill, reviewed against the "
                "career requirements."
            ),
            "rationale": (
                f"{len(already_have)} of {len(required_skills)} catalog-required skills "
                "already match your profile; the remaining gaps are ordered by catalog difficulty."
            ),
        },
        {
            "title": "Prove your skills with a portfolio project",
            "timeframe": f"By month {max(1, math.ceil(months * 0.7))}",
            "action": (
                f"Build {project['name']} and publish the work with a clear README."
                if project else "Choose a small project that demonstrates the target-career skills."
            ),
            "deliverable": (
                f"{project['name']} with a README and a short explanation of your decisions."
                if project else "A finished, documented project related to your target career."
            ),
            "rationale": project["reason"] if project else (
                "No project catalog entry was available, so this is a general portfolio step."
            ),
        },
        {
            "title": "Prepare applications and funding checks",
            "timeframe": f"By month {months}",
            "action": (
                "Update your resume with project evidence, compare the internship leads below, "
                "and verify each funding program's official eligibility and current deadline."
            ),
            "deliverable": "A tailored resume, application shortlist, and verified funding checklist.",
            "rationale": (
                "Internship and funding leads are ranked from the local catalogs; eligibility "
                "and availability must be confirmed with the provider."
            ),
        },
    ]

    return {
        "goal": career.get("career", str(goal).strip()),
        "career": career,
        "constraints": {
            "education_stage": education_stage,
            "stream": stream,
            "weekly_hours": int(weekly_hours),
            "monthly_budget": int(monthly_budget),
            "months": int(months),
            "location": location,
        },
        "skills": {
            "already_have": already_have,
            "required": required_skills,
            "gaps": gaps,
        },
        "effort": {
            "estimated_hours": estimated_hours,
            "available_hours": available_hours,
            "minimum_months_at_current_pace": minimum_months,
            "timeline_fits": estimated_hours <= available_hours,
        },
        "project": project,
        "internships": internship_matches,
        "funding": funding,
        "milestones": milestones,
        "explanation": [
            "Career requirements and opportunity leads come from EduBridge's local CSV catalogs.",
            "Skill gaps use case-insensitive exact matching against the selected career's required skills.",
            "Effort estimates use 6/12/20 learning hours per missing easy/medium/hard skill, plus project time.",
            "Funding leads are possible leads, not confirmed eligibility; check official program rules and dates.",
        ],
    }


def build_pathway_plan(
    goal: str,
    current_skills: str,
    education_stage: str,
    weekly_hours: int,
    monthly_budget: int,
    months: int,
    stream: str = "",
    location: str = "",
):
    """Agent tool: build a student roadmap using the local EduBridge catalogs."""
    return create_pathway_plan(
        goal=goal,
        current_skills=_items(current_skills),
        education_stage=education_stage,
        weekly_hours=weekly_hours,
        monthly_budget=monthly_budget,
        months=months,
        stream=stream,
        location=location,
    )
