import pandas as pd
import os

DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "database",
    "internships.csv"
)

def search_internships(skill=""):
    """
    Search internships by skill.
    """

    df = pd.read_csv(DATA_PATH)

    if skill:
        results = df[
            df["skills"].str.contains(skill, case=False, na=False)
        ]
    else:
        results = df

    return results.to_dict(orient="records")