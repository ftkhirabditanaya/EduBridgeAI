import os
import pandas as pd

from tools.query_parser import parse_internship_query
from tools.normalizer import normalize_filters

DATABASE_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "database",
    "internships.csv"
)


def load_database():
    return pd.read_csv(DATABASE_PATH)


def search_internships(query=""):
    df = load_database()

    # Return all internships if no query is provided
    if query.strip() == "":
        return df.sort_values(
            by="stipend",
            ascending=False
        ).to_dict(orient="records")

    # Parse natural language query using Gemini
    filters = parse_internship_query(query)

    # Normalize extracted filters
    filters = normalize_filters(filters)

    results = df.copy()

    # Filter by domain
    if filters.get("domain"):
        results = results[
            results["domain"]
            .str.lower()
            .str.contains(filters["domain"].lower(), na=False)
        ]

    # Filter by location
    if filters.get("location"):
        results = results[
            results["location"]
            .str.lower()
            .str.contains(filters["location"].lower(), na=False)
        ]

    # Filter by mode
    if filters.get("mode"):
        results = results[
            results["mode"]
            .str.lower()
            ==
            filters["mode"].lower()
        ]

    # Filter by branch
    if filters.get("branch"):
        results = results[
            results["branch"]
            .str.contains(filters["branch"], case=False, na=False)
        ]

    # Filter by minimum stipend
    if filters.get("minimum_stipend"):
        results = results[
            results["stipend"] >= filters["minimum_stipend"]
        ]

    return results.sort_values(
        by="stipend",
        ascending=False
    ).to_dict(orient="records")