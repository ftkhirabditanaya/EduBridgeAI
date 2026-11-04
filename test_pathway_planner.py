import unittest

from tools.pathway_planner_tool import create_pathway_plan


class PathwayPlannerTests(unittest.TestCase):
    def setUp(self):
        self.catalogs = {
            "careers": [{
                "career": "AI Engineer",
                "stream": "PCM",
                "description": "Build AI systems",
                "required_skills": "Python,TensorFlow,ML",
                "degree": "B.Tech AI",
            }],
            "projects": [{
                "project": "AI Portfolio Demo",
                "domain": "AI",
                "difficulty": "Medium",
                "skills": "Python,TensorFlow",
            }],
            "scholarships": [{
                "scholarship": "Engineering Merit Award",
                "eligibility": "Engineering Students, Merit Based",
                "amount": 50000,
                "last_date": "October",
            }],
            "internships": [{
                "company": "Example Labs",
                "role": "AI Intern",
                "skills": "Python,TensorFlow",
                "location": "Remote",
                "stipend": 30000,
                "apply_link": "https://example.com/careers",
            }],
            "skill_catalog": [
                {"skill": "Python", "difficulty": "Easy"},
                {"skill": "TensorFlow", "difficulty": "Hard"},
                {"skill": "ML", "difficulty": "Medium"},
            ],
        }

    def plan(self, **overrides):
        arguments = {
            "goal": "AI Engineer",
            "current_skills": ["Python"],
            "education_stage": "Undergraduate",
            "weekly_hours": 6,
            "monthly_budget": 1000,
            "months": 3,
            "stream": "PCM",
            "location": "Remote",
            **self.catalogs,
        }
        arguments.update(overrides)
        return create_pathway_plan(**arguments)

    def test_builds_explainable_skill_gaps_and_milestones(self):
        plan = self.plan()

        self.assertEqual(plan["goal"], "AI Engineer")
        self.assertEqual(plan["skills"]["already_have"], ["Python"])
        self.assertEqual(plan["skills"]["gaps"], ["ML", "TensorFlow"])
        self.assertEqual(len(plan["milestones"]), 3)
        self.assertIn("6/12/20", plan["explanation"][2])

    def test_recommends_catalog_project_internship_and_funding(self):
        plan = self.plan()

        self.assertEqual(plan["project"]["name"], "AI Portfolio Demo")
        self.assertEqual(plan["internships"][0]["company"], "Example Labs")
        self.assertIn("preferred location", plan["internships"][0]["reason"])
        self.assertEqual(plan["funding"][0]["fit"], "Potential fit")
        self.assertEqual(plan["funding"][0]["amount"], 50000)

    def test_marks_unrealistic_timeline_without_hiding_estimate(self):
        plan = self.plan(weekly_hours=1, months=1)

        self.assertFalse(plan["effort"]["timeline_fits"])
        self.assertGreater(plan["effort"]["estimated_hours"], plan["effort"]["available_hours"])

    def test_rejects_unmatched_goal_and_invalid_constraints(self):
        with self.assertRaisesRegex(ValueError, "No catalog career matched"):
            self.plan(goal="astronaut")
        with self.assertRaisesRegex(ValueError, "must be positive"):
            self.plan(weekly_hours=0)

    def test_existing_skills_are_matched_case_insensitively(self):
        plan = self.plan(current_skills=["python", "tensorflow", "ML"])

        self.assertEqual(plan["skills"]["already_have"], ["Python", "TensorFlow", "ML"])
        self.assertEqual(plan["skills"]["gaps"], [])


if __name__ == "__main__":
    unittest.main()
