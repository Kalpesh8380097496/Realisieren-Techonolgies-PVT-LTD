from urllib.parse import urlparse


def is_valid_url(url):
    if not url:
        return False

    parsed = urlparse(url)

    return parsed.scheme in ["http", "https"] and bool(parsed.netloc)


def validate_record(record):

    errors = []

    if not record.get("source"):
        errors.append("Missing source")

    if not record.get("name_or_title"):
        errors.append("Missing name_or_title")

    if not is_valid_url(record.get("source_url")):
        errors.append("Invalid source_url")

    price = record.get("price")

    if price is not None and not isinstance(price, (int, float)):
        errors.append("Invalid price")

    rating = record.get("rating")

    if rating is not None:
        if not isinstance(rating, (int, float)):
            errors.append("Invalid rating")
        elif not 1 <= rating <= 5:
            errors.append("Rating out of range")

    return len(errors) == 0, errors