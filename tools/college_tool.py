import pandas as pd
import os

DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "database",
    "colleges.csv"
)

def search_colleges(course=""):
    """
    Search colleges by course.
    """

    df = pd.read_csv(DATA_PATH)

    if course:
        results = df[
            df["course"].str.contains(course, case=False, na=False)
        ]
    else:
        results = df

    return results.to_dict(orient="records")