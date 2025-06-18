# 📘 Book Scraper Project

A Python-based web scraper that extracts book details from [Books to Scrape](http://books.toscrape.com) for analysis and reporting.

---

## 🎯 Goal

Scrape all books listed across multiple pages and collect:

- 📗 **Title**
- 💷 **Price**
- ⭐ **Rating** (1 to 5)
- 📦 **Availability**
- 🔗 **Product URL**


---

## 🔍 Data Extracted

- `title` – Book title  
- `price` – Price in GBP  
- `rating` – Star rating (converted to 1–5)  
- `availability` – In stock or not  
- `url` – Link to book's detail page  

---

## 🛠 Setup

### 📦 Install Requirements

Run the following command to install required packages:


pip install -r requirements.txt

---

## ▶️ Run Scraper

To run the scraper, execute:

python scraper.py
The extracted data will be saved as books_data.csv in the project directory.

---

## 🧪 Testing
To run unit tests, use:

python -m unittest tests/test_main.py

✅ Test coverage includes:
Verifying page scraping

Handling pagination

Validating data structure

Ensuring clean CSV output

---


## 📁 Project Structure

book_scraper_project/

scraper.py

books_data.csv

requirements.txt

README.md

scraper.log

tests/

test_scraper.py



 ---

### 👩‍💻 Author

Keesha Cutinha
Bachelor’s in Artificial Intelligence & Data Science
NMAM Institute of Technology
---
