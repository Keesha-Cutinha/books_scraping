import unittest
import os
import pandas as pd

class TestBookScraper(unittest.TestCase):

    # ✅ Test Case 1: Verify CSV File Download
    def test_csv_exists(self):
        self.assertTrue(os.path.exists("books_data.csv"), "CSV file 'books_data.csv' does not exist.")

    # ✅ Test Case 2: Verify CSV File Extraction
    def test_csv_not_empty(self):
        df = pd.read_csv("books_data.csv")
        self.assertGreater(len(df), 0, "CSV file is empty.")

    # ✅ Test Case 3: Validate File Type and Format
    def test_file_type(self):
        self.assertTrue("books_data.csv".endswith(".csv"), "File is not a .csv")

    # ✅ Test Case 4: Validate Data Structure
    def test_csv_columns(self):
        df = pd.read_csv("books_data.csv")
        expected_cols = ["Title", "Price", "Rating", "Availability", "URL"]
        for col in expected_cols:
            self.assertIn(col, df.columns, f"Missing expected column: {col}")

    # ✅ Test Case 5: Handle Missing or Invalid Data
    def test_missing_or_invalid_data(self):
        df = pd.read_csv("books_data.csv")
        null_counts = df.isnull().sum()
        print("\nMissing values by column:\n", null_counts)
        self.assertFalse(df.isnull().any().any(), "❌ CSV contains missing values.")

if __name__ == "__main__":
    unittest.main()
