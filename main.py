from Models import database

def main():
    db = database.Database("Store_rtp")
    db.connect()
    print("Connected to the database")
    # db.populate_categories()
    # db.populate_products()
    db.close()

if __name__ == "__main__":
    main()