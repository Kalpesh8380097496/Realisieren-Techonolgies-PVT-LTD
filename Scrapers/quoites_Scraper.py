import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


BASE_URL = "https://quotes.toscrape.com/"


def get_page(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def scrape_quotes():
    quotes = []
    page_url = BASE_URL

    while page_url:

        print(f"Scraping: {page_url}")

        try:
            soup = get_page(page_url)

            quote_blocks = soup.select(".quote")

            for quote in quote_blocks:

                text_element = quote.select_one(".text")
                author_element = quote.select_one(".author")
                tag_elements = quote.select(".tags .tag")

                text = (
                    text_element.get_text(strip=True)
                    if text_element else ""
                )

                author = (
                    author_element.get_text(strip=True)
                    if author_element else ""
                )

                tags = ", ".join(
                    tag.get_text(strip=True)
                    for tag in tag_elements
                )

                quotes.append({
                    "source": "Quotes to Scrape",
                    "source_url": page_url,
                    "name_or_title": text,
                    "category": "",
                    "price": "",
                    "rating": "",
                    "author": author,
                    "tags": tags,
                    "description": "",
                    "availability": ""
                })

            next_button = soup.select_one("li.next a")

            if next_button:
                next_url = next_button.get("href")
                page_url = urljoin(page_url, next_url)
            else:
                page_url = None

        except requests.RequestException as error:
            print(f"Request failed: {error}")
            page_url = None

    return quotes


if __name__ == "__main__":
    data = scrape_quotes()

    print("Total quotes:", len(data))

    for quote in data[:5]:
        print(quote)