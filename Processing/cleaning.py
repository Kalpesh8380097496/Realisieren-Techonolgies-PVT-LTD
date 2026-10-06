import re


def clean_text(value):
    if value is None:
        return ""

    return " ".join(str(value).split())


def clean_price(value):
    if not value:
        return None

    value = str(value).replace("£", "").strip()

    try:
        return float(value)
    except ValueError:
        return None


def clean_rating(value):
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    return rating_map.get(value, None)


def normalize_record(record):

    record["name_or_title"] = clean_text(
        record.get("name_or_title")
    )

    record["author"] = clean_text(
        record.get("author")
    )

    record["tags"] = clean_text(
        record.get("tags")
    )

    record["category"] = clean_text(
        record.get("category")
    )

    record["price"] = clean_price(
        record.get("price")
    )

    record["rating"] = clean_rating(
        record.get("rating")
    )

    return record