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

        # Create a frame to contain the product_table and the scrollbar
        table_frame = ctk.CTkFrame(self)
        table_frame.pack(fill=ctk.BOTH, expand=True)

        self.product_table = ttk.Treeview(table_frame, columns=("ID", "Name", "Description", "Price", "Quantity", "Category"), show='headings', style="Treeview")
        self.product_table.heading("ID", text="ID", command=lambda: self.sort_table("ID"))
        self.product_table.heading("Name", text="Name", command=lambda: self.sort_table("Name"))
        self.product_table.heading("Description", text="Description", command=lambda: self.sort_table("Description"))
        self.product_table.heading("Price", text="Price", command=lambda: self.sort_table("Price"))
        self.product_table.heading("Quantity", text="Quantity", command=lambda: self.sort_table("Quantity"))
        self.product_table.heading("Category", text="Category", command=lambda: self.sort_table("Category"))

        # Set column widths and stretch properties
        self.product_table.column("ID", width=50, stretch=tk.NO)
        self.product_table.column("Name", width=150, stretch=tk.YES)
        self.product_table.column("Description", width=300, stretch=tk.YES)
        self.product_table.column("Price", width=100, stretch=tk.YES)
        self.product_table.column("Quantity", width=80, stretch=tk.NO)
        self.product_table.column("Category", width=140, stretch=tk.YES)

        # Create a scrollbar and link it to the product_table
        self.scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.product_table.yview)
        self.product_table.configure(yscroll=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.product_table.pack(fill=ctk.BOTH, expand=True)

        # Create a frame for the buttons
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(fill=ctk.X, pady=10)

        self.add_button = ctk.CTkButton(button_frame, text="Add Product", command=self.show_add_product_popup)
        self.add_button.pack(side=ctk.LEFT, padx=10)

        self.update_button = ctk.CTkButton(button_frame, text="Update Product", command=self.show_update_product_popup)
        self.update_button.pack(side=ctk.LEFT, padx=10)

        self.delete_button = ctk.CTkButton(button_frame, text="Delete Product", command=self.show_delete_product_popup)
        self.delete_button.pack(side=ctk.LEFT, padx=10)

        self.sort_column = None
        self.sort_order = True

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
            ErrorPopup(self, "You must select a product to update.")

    def show_delete_product_popup(self):
        try:
            selected_item = self.product_table.selection()[0]
            product_id = self.product_table.item(selected_item)['values'][0]
            DeleteProductPopup(self.controller, product_id)
        except IndexError:
            ErrorPopup(self, "You must select a product to delete.")

    def sort_table(self, col):
        data = [(self.product_table.set(child, col), child) for child in self.product_table.get_children('')]
        data.sort(reverse=self.sort_order)
        for index, (val, child) in enumerate(data):
            self.product_table.move(child, '', index)
        self.sort_order = not self.sort_order
        self.sort_column = col
