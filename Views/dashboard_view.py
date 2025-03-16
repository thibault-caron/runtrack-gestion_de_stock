import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from Views.add_product_popup import AddProductPopup
from Views.update_product_popup import UpdateProductPopup
from Views.delete_product_popup import DeleteProductPopup
from Views.error_popup import ErrorPopup

class DashboardView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Stock Management Dashboard")
        self.geometry("800x600")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", 
                        background="black", 
                        foreground="white", 
                        fieldbackground="black", 
                        rowheight=30,
                        font=('Helvetica', 12))
        style.configure("Treeview.Heading", 
                        background="black", 
                        foreground="white",
                        font=('Helvetica', 13, 'bold'))
        style.map("Treeview", 
                  background=[('selected', 'gray')],
                  foreground=[('selected', 'black')])

        self.product_table = ttk.Treeview(self, columns=("ID", "Name", "Description", "Price", "Quantity", "Category"), show='headings', style="Treeview")
        self.product_table.heading("ID", text="ID")
        self.product_table.heading("Name", text="Name")
        self.product_table.heading("Description", text="Description")
        self.product_table.heading("Price", text="Price")
        self.product_table.heading("Quantity", text="Quantity")
        self.product_table.heading("Category", text="Category")

        # Set column widths and stretch properties
        self.product_table.column("ID", width=50, stretch=tk.NO)
        self.product_table.column("Name", width=150, stretch=tk.YES)
        self.product_table.column("Description", width=300, stretch=tk.YES)
        self.product_table.column("Price", width=100, stretch=tk.YES)
        self.product_table.column("Quantity", width=80, stretch=tk.NO)
        self.product_table.column("Category", width=140, stretch=tk.YES)

        self.product_table.pack(fill=ctk.BOTH, expand=True)

        self.add_button = ctk.CTkButton(self, text="Add Product", command=self.show_add_product_popup)
        self.add_button.pack(side=ctk.LEFT, padx=10, pady=10)

        self.update_button = ctk.CTkButton(self, text="Update Product", command=self.show_update_product_popup)
        self.update_button.pack(side=ctk.LEFT, padx=10, pady=10)

        self.delete_button = ctk.CTkButton(self, text="Delete Product", command=self.show_delete_product_popup)
        self.delete_button.pack(side=ctk.LEFT, padx=10, pady=10)

    def display_products(self, products):
        for row in self.product_table.get_children():
            self.product_table.delete(row)
        for product in products:
            self.product_table.insert("", tk.END, values=product)

    def show_add_product_popup(self):
        AddProductPopup(self.controller)

    def show_update_product_popup(self):
        try:
            selected_item = self.product_table.selection()[0]
            product = self.product_table.item(selected_item)['values']
            UpdateProductPopup(self.controller, product)
        except IndexError:
            ErrorPopup("You must select a product to update.")

    def show_delete_product_popup(self):
        selected_item = self.product_table.selection()[0]
        product_id = self.product_table.item(selected_item)['values'][0]
        DeleteProductPopup(self.controller, product_id)
