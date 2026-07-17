import pandas as pd
import os

# ==============================
# Database Path
# ==============================

DATABASE_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "database",
    "careers.csv"
)


# ==============================
# Load Database
# ==============================

def load_database():
    return pd.read_csv(DATABASE_PATH)


# ==============================
# Return Entire Database
# ==============================

def get_all_careers():
    df = load_database()
    return df.to_dict(orient="records")


# ==============================
# Search by Stream
# Example:
# PCB
# PCM
# Commerce
# ==============================

def search_by_stream(stream: str):

    df = load_database()

    results = df[
        df["stream"].str.contains(
            stream,
            case=False,
            na=False
        )
    ]

    return results.to_dict(orient="records")


# ==============================
# Search by Skill
# ==============================

def search_by_skill(skill: str):

    df = load_database()

    results = df[
        df["required_skills"].str.contains(
            skill,
            case=False,
            na=False
        )
    ]

    return results.to_dict(orient="records")


# ==============================
# Search by Career Name
# ==============================

def search_by_career(name: str):

    df = load_database()

    results = df[
        df["career"].str.contains(
            name,
            case=False,
            na=False
        )
    ]

    return results.to_dict(orient="records")


# ==============================
# Universal Career Search
# (Used by ADK Agents)
# ==============================

def search_careers(query: str = ""):

    df = load_database()

    if query.strip() == "":
        return df.to_dict(orient="records")

    results = df[
        df.apply(
            lambda row: query.lower() in str(row).lower(),
            axis=1
        )
    ]

    return results.to_dict(orient="records")