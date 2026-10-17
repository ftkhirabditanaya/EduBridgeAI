"""
EduBridge AI
Recommendation Engine

This module calculates how well an internship
matches the user's requirements.
"""

# -----------------------------
# Scoring Configuration
# -----------------------------

SCORE_WEIGHTS = {

    "domain": 30,

    "location": 20,

    "mode": 15,

    "branch": 15,

    "stipend": 20
}


def get_score_weights():
    """
    Returns the scoring configuration.

    This allows us to easily change weights
    later without touching the algorithm.
    """

    return SCORE_WEIGHTS

def match_domain(user_domain, internship_domain):

    if not user_domain:
        return False

    return user_domain.lower() == internship_domain.lower()


def match_location(user_location, internship_location):

    if not user_location:
        return False

    return user_location.lower() == internship_location.lower()


def match_mode(user_mode, internship_mode):

    if not user_mode:
        return False

    return user_mode.lower() == internship_mode.lower()


def match_branch(user_branch, internship_branch):

    if not user_branch:
        return False

    return user_branch.lower() in internship_branch.lower()


def match_stipend(required_stipend, internship_stipend):

    if not required_stipend:
        return False

    return internship_stipend >= required_stipend

def calculate_match_score(filters, internship):

    """
    Calculates:

    • Match Score

    • Matching Reasons

    • Missing Criteria
    """

    weights = get_score_weights()

    score = 0

    reasons = []

    missing = []

    # Domain

    if match_domain(
        filters.get("domain"),
        internship["domain"]
    ):

        score += weights["domain"]

        reasons.append("✓ Domain matches")

    else:

        missing.append("Domain")

    # Location

    if match_location(
        filters.get("location"),
        internship["location"]
    ):

        score += weights["location"]

        reasons.append("✓ Preferred location")

    else:

        missing.append("Location")

    # Mode

    if match_mode(
        filters.get("mode"),
        internship["mode"]
    ):

        score += weights["mode"]

        reasons.append("✓ Preferred work mode")

    else:

        missing.append("Mode")

    # Branch

    if match_branch(
        filters.get("branch"),
        internship["branch"]
    ):

        score += weights["branch"]

        reasons.append("✓ Suitable for your branch")

    else:

        missing.append("Branch")

    # Stipend

    if match_stipend(
        filters.get("minimum_stipend"),
        internship["stipend"]
    ):

        score += weights["stipend"]

        reasons.append("✓ Meets stipend expectation")

    else:

        missing.append("Stipend")

    return {

        "score": score,

        "reasons": reasons,

        "missing": missing
    }