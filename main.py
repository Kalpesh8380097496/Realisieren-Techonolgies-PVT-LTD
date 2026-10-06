import json
import time
from datetime import datetime

import pandas as pd

from Scrapers.Book_Scraper import  scrape_books
from Scrapers.quoites_Scraper import scrape_quotes

from Processing.cleaning import normalize_record
from Processing.validation import validate_record
from Processing.deduplication import deduplicate


def main():

    start_time = time.time()

    print("Starting scraper...")

    books = scrape_books()
    quotes = scrape_quotes()

    print(f"Books collected: {len(books)}")
    print(f"Quotes collected: {len(quotes)}")

    all_records = books + quotes

    cleaned_records = []

    for record in all_records:
        record = normalize_record(record)

        record["scraped_at"] = datetime.now().isoformat()

        cleaned_records.append(record)

    valid_records = []
    rejected_records = []

    for record in cleaned_records:

        is_valid, errors = validate_record(record)

        if is_valid:
            valid_records.append(record)
        else:
            rejected_records.append({
                "record": record,
                "errors": errors
            })

    unique_records, duplicate_records = deduplicate(
        valid_records
    )

    df = pd.DataFrame(unique_records)

    df.to_csv(
        "output/final_dataset.csv",
        index=False
    )

    execution_time = time.time() - start_time

    summary = {
        "books_collected": len(books),
        "quotes_collected": len(quotes),
        "total_records_collected": len(all_records),
        "records_after_cleaning": len(cleaned_records),
        "records_rejected": len(rejected_records),
        "duplicates_detected": len(duplicate_records),
        "final_record_count": len(unique_records),
        "execution_time_seconds": round(
            execution_time, 2
        )
    }

    with open(
        "output/summary_report.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            summary,
            file,
            indent=4
        )

    print("\nScraping completed.")
    print(json.dumps(summary, indent=4))


if __name__ == "__main__":
    main()