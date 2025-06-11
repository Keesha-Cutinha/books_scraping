import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import logging

logging.basicConfig(filename="scraper.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

BASE_URL = "http://books.toscrape.com/" # This is a test update for PR

CATALOGUE_URL = BASE_URL + "catalogue/"# testing

def get_soup(url):
    try:
        response = requests.get(url, timeout=10)# tester
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except requests.exceptions.RequestException as e:
        logging.error(f"HTTP error: {e} at {url}")
        return None

def extract_book_data(book):
    try:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.strip()
        rating_class = book.p["class"][1]
        rating = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}.get(rating_class, 0)
        availability = book.find("p", class_="instock availability").text.strip()
        partial_url = book.h3.a["href"]
        full_url = CATALOGUE_URL + partial_url.replace("../", "")
        return {
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "URL": full_url
        }
    except Exception as e:
        logging.error(f"Error extracting book: {e}")
        return None

def scrape_all_books():
    all_books = []
    page = 1
    while True:
        url = f"{CATALOGUE_URL}page-{page}.html"
        soup = get_soup(url)
        if soup is None:
            break

        books = soup.find_all("article", class_="product_pod")
        if not books:
            break

        for book in books:
            data = extract_book_data(book)
            if data:
                all_books.append(data)

        page += 1
        time.sleep(1)

    return all_books

def save_to_csv(data, filename="books_data.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"✅ Saved {len(data)} books to {filename}")

if __name__ == "__main__":
    books = scrape_all_books()
    save_to_csv(books)
