Python Web Scraping Assignment

Project

This project collects data from two websites:

1. Books to Scrape
2. Quotes to Scrape

The data is scraped using Python, cleaned, validated, and combined into one CSV file.

Technologies

- Python
- Requests
- BeautifulSoup
- Pandas

How to Run

Run:

python main.py

Scraping

The scraper automatically handles multiple pages from both websites.

Cleaning

The project:

- Removes extra spaces
- Converts prices to numbers
- Standardizes ratings
- Handles missing values

Validation

Records are checked for valid source, title/text, URL, price, and rating.

Duplicate Detection

Duplicate records are detected using normalized text and source information.

Output

The project creates:

- output/final_dataset.csv
- output/summary_report.json

Result

Books collected: 1000
Quotes collected: 100
Total records: 1100
Records after cleaning: 1100
Rejected records: 0
Duplicates: 1
Final records: 1099