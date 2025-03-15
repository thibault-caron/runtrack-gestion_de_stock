from Models.database import Database
from Views.dashboard_view import DashboardView

class DashboardController:
    def __init__(self):
        self.model = Database("Store_rtp")
        self.view = DashboardView(self)
        self.fetch_products()  # Move this line here
        self.view.mainloop()

    def fetch_products(self):
        products = self.model.fetch_products()
        self.view.display_products(products)

    def add_product(self):
        # Logic to add a product (e.g., open a dialog to get product details)
        pass

    def update_product(self):
        # Logic to update a product (e.g., open a dialog to get new product details)
        pass

    def delete_product(self):
        # Logic to delete a product (e.g., get selected product and delete it)
        pass
