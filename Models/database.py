import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        # Establish the database connection
        self.conn = mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database=self.db_name
        )
        self.cursor = self.conn.cursor()

    def populate_categories(self):
        # Insert categories
        categories = [
            ("Electronics",),
            ("Clothing",),
            ("Books",)
        ]
        self.cursor.executemany("INSERT INTO category (name) VALUES (%s)", categories)

    def populate_products(self):
        # Insert products
        products = [
            ("Laptop", "A high performance laptop", 999.99, 10, 1),
            ("T-Shirt", "A comfortable cotton t-shirt", 19.99, 50, 2),
            ("Novel", "A best-selling novel", 14.99, 30, 3)
        ]
        self.cursor.executemany("INSERT INTO product (name, description, price, quantity, Id_category) VALUES (%s, %s, %s, %s, %s)", products)

    def close(self):
        # Commit the transaction and close the connection
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    db = Database("Store_rtp")
    db.connect()
    # db.populate_categories()
    # db.populate_products()
    db.close()
