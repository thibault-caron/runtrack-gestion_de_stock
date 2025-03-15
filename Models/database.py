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
        ''' Establish the database connection '''
        self.conn = mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database=self.db_name
        )
        self.cursor = self.conn.cursor()

    def populate_categories(self):
        '''Insert categories'''
        categories = [
            ("Electronics",),
            ("Clothing",),
            ("Books",)
        ]
        self.cursor.executemany("INSERT INTO category (name) VALUES (%s)", categories)
        self.conn.commit()

    def populate_products(self):
        '''Insert products'''
        products = [
            ("Laptop", "A high performance laptop", 999.99, 10, 1),
            ("T-Shirt", "A comfortable cotton t-shirt", 19.99, 50, 2),
            ("Novel", "A best-selling novel", 14.99, 30, 3)
        ]
        self.cursor.executemany("INSERT INTO product (name, description, price, quantity, Id_category) VALUES (%s, %s, %s, %s, %s)", products)
        self.conn.commit()

    def fetch_products(self):
        '''Fetch all products'''
        self.connect()
        self.cursor.execute("SELECT * FROM product")
        return self.cursor.fetchall()

    def add_product(self, name, description, price, quantity, category_id):
        '''Add a new product'''
        self.cursor.execute(
            "INSERT INTO product (name, description, price, quantity, Id_category) VALUES (%s, %s, %s, %s, %s)",
            (name, description, price, quantity, category_id)
        )
        self.conn.commit()

    def update_product(self, product_id, name, description, price, quantity, category_id):
        '''Update an existing product'''
        self.cursor.execute(
            "UPDATE product SET name=%s, description=%s, price=%s, quantity=%s, Id_category=%s WHERE id=%s",
            (name, description, price, quantity, category_id, product_id)
        )
        self.conn.commit()

    def delete_product(self, product_id):
        '''Delete a product'''
        self.cursor.execute("DELETE FROM product WHERE id=%s", (product_id,))
        self.conn.commit()

    def close(self):
        '''close the connection'''
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    db = Database("Store_rtp")
    db.connect()
    # db.populate_categories()
    # db.populate_products()
    db.close()
