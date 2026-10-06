import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


BASE_URL = "https://books.toscrape.com/"


def get_page(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def scrape_books():
    books = []
    page_url = BASE_URL

    while page_url:

        print(f"Scraping: {page_url}")

        try:
            soup = get_page(page_url)

            book_cards = soup.select("article.product_pod")

            for book in book_cards:

                title_element = book.select_one("h3 a")
                price_element = book.select_one(".price_color")
                availability_element = book.select_one(".availability")
                rating_element = book.select_one("p.star-rating")

                title = (
                    title_element.get("title", "").strip()
                    if title_element else ""
                )

                price = (
                    price_element.get_text(strip=True)
                    if price_element else ""
                )

                availability = (
                    availability_element.get_text(" ", strip=True)
                    if availability_element else ""
                )

                rating = ""

                if rating_element:
                    rating_classes = rating_element.get("class", [])
                    if len(rating_classes) > 1:
                        rating = rating_classes[1]

                relative_url = (
                    title_element.get("href")
                    if title_element else ""
                )

                product_url = (
                    urljoin(page_url, relative_url)
                    if relative_url else ""
                )

                books.append({
                    "source": "Books to Scrape",
                    "source_url": product_url,
                    "name_or_title": title,
                    "category": "",
                    "price": price,
                    "rating": rating,
                    "author": "",
                    "tags": "",
                    "description": "",
                    "availability": availability
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

    return books