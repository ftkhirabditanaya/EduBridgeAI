def normalize_filters(filters):
    """
    Convert similar terms into the format used
    inside the internship database.
    """

    domain_map = {
        "ai": "AI",
        "artificial intelligence": "AI",
        "machine learning": "AI",
        "deep learning": "AI",
        "computer vision": "AI",
        "nlp": "AI",

        "embedded": "Embedded",
        "embedded systems": "Embedded",

        "data science": "Data",
        "data analytics": "Data"
    }

    mode_map = {
        "remote": "Remote",
        "hybrid": "Hybrid",
        "onsite": "Onsite",
        "on-site": "Onsite"
    }

    # Normalize domain
    if filters.get("domain"):
        domain = filters["domain"].strip().lower()

        if domain in domain_map:
            filters["domain"] = domain_map[domain]

    # Normalize mode
    if filters.get("mode"):
        mode = filters["mode"].strip().lower()

        if mode in mode_map:
            filters["mode"] = mode_map[mode]

    return filters