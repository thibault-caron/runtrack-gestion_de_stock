from Models.database import Database
from Views.dashboard_view import DashboardView
from Views.add_product_popup import AddProductPopup
from Views.update_product_popup import UpdateProductPopup
from Views.error_popup import ErrorPopup

class DashboardController:
    def __init__(self):
        self.model = Database("Store_rtp")
        self.view = DashboardView(self)
        self.fetch_products()
        self.view.mainloop()

    def fetch_products(self):
        try:
            products = self.model.fetch_products()
            self.view.display_products(products)
        except Exception as e:
            ErrorPopup(self.view, str(e))

    def fetch_categories(self):
        try:
            return self.model.fetch_categories()
        except Exception as e:
            ErrorPopup(self.view, str(e))

    def add_product(self, name, description, price, quantity, category_id):
        try:
            self.model.add_product(name, description, price, quantity, category_id)
            self.fetch_products()
        except Exception as e:
            ErrorPopup(self.view, str(e))

    def update_product(self, product_id, name, description, price, quantity, category_id):
        try:
            print(f"Controller: Updating product ID {product_id}")
            self.model.update_product(product_id, name, description, price, quantity, category_id)
            self.fetch_products()
        except Exception as e:
            ErrorPopup(self.view, str(e))

    def delete_product(self, product_id):
        try:
            print(f"Controller: Deleting product ID {product_id}")
            self.model.delete_product(product_id)
            self.fetch_products()
        except Exception as e:
            ErrorPopup(self.view, str(e))
