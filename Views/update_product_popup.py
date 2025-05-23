import customtkinter as ctk
from Views.error_popup import ErrorPopup
import tkinter as tk

class UpdateProductPopup(ctk.CTkToplevel):
    def __init__(self, controller, product):
        super().__init__()
        self.controller = controller
        self.product = product
        self.title("Update Product")
        self.geometry("400x500")
        self.transient(controller.view)  # Set the parent window
        self.lift()  # Bring the popup to the front

        categories = self.controller.fetch_categories()
        self.category_dict = {name: id for id, name in categories}

        name_label = ctk.CTkLabel(self, text="Name")
        name_label.pack(pady=5)
        self.name_entry = ctk.CTkEntry(self)
        self.name_entry.insert(0, product[1])
        self.name_entry.pack(pady=5)

        description_label = ctk.CTkLabel(self, text="Description")
        description_label.pack(pady=5)
        self.description_entry = ctk.CTkEntry(self)
        self.description_entry.insert(0, product[2])
        self.description_entry.pack(pady=5)

        price_label = ctk.CTkLabel(self, text="Price")
        price_label.pack(pady=5)
        self.price_entry = ctk.CTkEntry(self)
        self.price_entry.insert(0, product[3])
        self.price_entry.pack(pady=5)

        quantity_label = ctk.CTkLabel(self, text="Quantity")
        quantity_label.pack(pady=5)
        self.quantity_entry = ctk.CTkEntry(self)
        self.quantity_entry.insert(0, product[4])
        self.quantity_entry.pack(pady=5)

        category_label = ctk.CTkLabel(self, text="Category")
        category_label.pack(pady=5)
        self.category_var = tk.StringVar(self)
        self.category_menu = ctk.CTkOptionMenu(self, variable=self.category_var, values=list(self.category_dict.keys()))
        self.category_menu.set(product[5])  # Set the current category
        self.category_menu.pack(pady=5)

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=10)

        update_button = ctk.CTkButton(button_frame, text="Update", command=self.update_product)
        update_button.pack(side=ctk.LEFT, padx=10)

        back_button = ctk.CTkButton(button_frame, text="Back", command=self.destroy)
        back_button.pack(side=ctk.LEFT, padx=10)

    def update_product(self):
        name = self.name_entry.get()
        description = self.description_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()
        category_name = self.category_var.get()

        if not name or not description or not price or not quantity or not category_name:
            ErrorPopup(self, "All fields must be filled.")
            return

        try:
            price = float(price)
            quantity = int(quantity)
            category_id = self.category_dict[category_name]
        except ValueError:
            ErrorPopup(self, "Price and Quantity must be valid numbers.")
            return

        self.controller.update_product(self.product[0], name, description, price, quantity, category_id)
        self.destroy()
