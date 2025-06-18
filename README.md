📚 Book Scraper Project
A Python-based scraper that extracts book details from Books to Scrape for analysis and reporting.

🎯 Goal
To scrape all books listed across multiple pages and collect:

Title

Price

Rating (out of 5)

Availability

Product URL

🚀 Features
1. 📡 Data Retrieval
Iterates through all available pages on the website.

Fetches data from each book listing.

Handles broken pages or missing elements gracefully.

2. 🧾 Data Extracted
title: Book title

price: Price in GBP

rating: Star rating (converted to numeric 1–5)

availability: Stock status

url: Link to the book's detail page

3. 📦 Output Format
Data is saved as books_data.csv for easy analysis or ingestion into other tools.

🧰 Installation
📌 Prerequisites
Python 3.10 or higher

pip package manager

🧪 Setup Instructions
Clone the repository:


git clone https://github.com/yourusername/books_scraping.git
cd books_scraping
Create and activate a virtual environment (Windows):


python -m venv venv
venv\Scripts\activate
Install dependencies:


pip install -r requirements.txt
▶️ Usage
Run the scraper using:


python scraper.py
The extracted data will be saved as books_data.csv in the project directory.

🧪 Testing
To run the unit tests:

pytest tests/test_file.py
Test cases include:

✅ Verifying page scraping

✅ Handling pagination

✅ Validating data structure

✅ Ensuring clean CSV output

📂 Project Structure

books_scraping/
├── scraper.py            # Main scraping logic  
├── books_data.csv        # Output data (generated)  
├── requirements.txt      # Project dependencies  
├── README.md             # Project documentation  
├── scraper.log           # Runtime logs  
├── tests/
│   └── test_file.py      # Unit tests  
🤝 Contributions
Have improvements or ideas?
Feel free to fork this repo, raise issues, or create pull requests.

👩‍💻 Author
Keesha Cutinha
Bachelor's in Artificial Intelligence & Data Science
NMAM Institute of Technology

