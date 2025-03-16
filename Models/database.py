import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Database:
    def __init__(self, db_name):
        self.db_name = db_name

    def connect(self):
        ''' Establish the database connection '''
        try:
            conn = mysql.connector.connect(
                host=os.getenv("HOST"),
                user=os.getenv("USER"),
                password=os.getenv("PASSWORD"),
                database=self.db_name
            )
            return conn
        except Error as e:
            print(f"Error: {e}")
            return None

    def populate_categories(self):
        '''Insert categories'''
        with self.connect() as conn:
            if conn:
                cursor = conn.cursor()
                categories = [
                    ("Electronics",),
                    ("Clothing",),
                    ("Books",)
                ]
                cursor.executemany("INSERT INTO category (name) VALUES (%s)", categories)
                conn.commit()

    def populate_products(self):
        '''Insert products'''
        with self.connect() as conn:
            if conn:
                cursor = conn.cursor()
                products = [
                    ("Laptop", "A high performance laptop", 999.99, 10, 1),
                    ("T-Shirt", "A comfortable cotton t-shirt", 19.99, 50, 2),
                    ("Novel", "A best-selling novel", 14.99, 30, 3)
                ]
                cursor.executemany("INSERT INTO product (name, description, price, quantity, Id_category) VALUES (%s, %s, %s, %s, %s)", products)
                conn.commit()

    def fetch_products(self):
        '''Fetch all products with category names'''
        with self.connect() as conn:
            if conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT product.Id_product, product.name, product.description, product.price, product.quantity, category.name AS category_name
                    FROM product
                    LEFT JOIN category ON product.Id_category = category.Id_category
                """)
                products = cursor.fetchall()
                return products

    def fetch_categories(self):
        '''Fetch all categories'''
        with self.connect() as conn:
            if conn:
                cursor = conn.cursor()
                cursor.execute("SELECT Id_category, name FROM category")
                categories = cursor.fetchall()
                return categories

    def add_product(self, name, description, price, quantity, category_id):
        '''Add a new product'''
        with self.connect() as conn:
            if conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO product (name, description, price, quantity, Id_category) VALUES (%s, %s, %s, %s, %s)",
                    (name, description, price, quantity, category_id)
                )
                conn.commit()

    def update_product(self, product_id, name, description, price, quantity, category_id):
        '''Update an existing product'''
        with self.connect() as conn:
            if conn:
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE product SET name=%s, description=%s, price=%s, quantity=%s, Id_category=%s WHERE Id_product=%s",
                    (name, description, price, quantity, category_id, product_id)
                )
                conn.commit()

    def delete_product(self, product_id):
        '''Delete a product'''
        with self.connect() as conn:
            if conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM product WHERE Id_product=%s", (product_id,))
                conn.commit()

if __name__ == "__main__":
    db = Database("Store_rtp")
    # db.populate_categories()
    # db.populate_products()
