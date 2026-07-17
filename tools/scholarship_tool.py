import pandas as pd
import os

DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "database",
    "scholarships.csv"
)

def search_scholarships(keyword=""):

    df = pd.read_csv(DATA_PATH)

    if keyword:
        results = df[
            df["eligibility"].str.contains(keyword, case=False, na=False)
        ]
    else:
        results = df

    return results.to_dict(orient="records")