from Models import database

def main():
    db = database.Database("Store_rtp")
    db.connect()
    # db.populate_categories()
    # db.populate_products()
    db.close()