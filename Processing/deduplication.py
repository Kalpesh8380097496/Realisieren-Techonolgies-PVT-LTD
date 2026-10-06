def normalize_for_duplicate(value):
    if not value:
        return ""

    return " ".join(str(value).lower().split())


def deduplicate(records):

    unique_records = []
    duplicate_records = []

    seen = set()

    for record in records:

        title = normalize_for_duplicate(
            record.get("name_or_title")
        )

        source = normalize_for_duplicate(
            record.get("source")
        )

        key = (source, title)

        if key in seen:
            duplicate_records.append(record)
        else:
            seen.add(key)
            unique_records.append(record)

    return unique_records, duplicate_records