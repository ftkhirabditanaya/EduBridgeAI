import os
import pandas as pd

from tools.query_parser import parse_internship_query
from tools.normalizer import normalize_filters
from tools.recommendation_engine import calculate_match_score


# ----------------------------------------------------
# Database Path
# ----------------------------------------------------

DATABASE_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "database",
    "internships.csv"
)


# ----------------------------------------------------
# Load Database
# ----------------------------------------------------

def load_database():
    return pd.read_csv(DATABASE_PATH)


# ----------------------------------------------------
# Internship Search
# ----------------------------------------------------

def search_internships(query=""):

    df = load_database()

    # If no query is provided, return all internships
    if query.strip() == "":
        filters = {}
        results = df.copy()

    else:

        # Parse natural language query
        filters = parse_internship_query(query)

        # Normalize values
        filters = normalize_filters(filters)

        results = df.copy()

        # --------------------------------------------
        # Domain Filter
        # --------------------------------------------

        if filters.get("domain"):

            results = results[
                results["domain"]
                .str.lower()
                .str.contains(
                    filters["domain"].lower(),
                    na=False
                )
            ]

        # --------------------------------------------
        # Location Filter
        # --------------------------------------------

        if filters.get("location"):

            results = results[
                results["location"]
                .str.lower()
                .str.contains(
                    filters["location"].lower(),
                    na=False
                )
            ]

        # --------------------------------------------
        # Mode Filter
        # --------------------------------------------

        if filters.get("mode"):

            results = results[
                results["mode"]
                .str.lower()
                ==
                filters["mode"].lower()
            ]

        # --------------------------------------------
        # Branch Filter
        # --------------------------------------------

        if filters.get("branch"):

            results = results[
                results["branch"]
                .str.contains(
                    filters["branch"],
                    case=False,
                    na=False
                )
            ]

        # --------------------------------------------
        # Minimum Stipend Filter
        # --------------------------------------------

        if filters.get("minimum_stipend"):

            results = results[
                results["stipend"]
                >=
                filters["minimum_stipend"]
            ]

    # ------------------------------------------------
    # Recommendation Engine
    # ------------------------------------------------

    recommendations = []

    for _, row in results.iterrows():

        internship = row.to_dict()

        recommendation = calculate_match_score(
            filters,
            internship
        )

        internship["match_score"] = recommendation["score"]
        internship["reasons"] = recommendation["reasons"]
        internship["missing"] = recommendation["missing"]

        recommendations.append(internship)

    # ------------------------------------------------
    # Sort by Match Score then Stipend
    # ------------------------------------------------

    recommendations.sort(

        key=lambda internship: (

            internship["match_score"],
            internship["stipend"]

        ),

        reverse=True

    )

    return recommendations