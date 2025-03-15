import customtkinter as ctk

class UpdateProductPopup(ctk.CTkToplevel):
    def __init__(self, controller, product):
        super().__init__()
        self.controller = controller
        self.product = product
        self.title("Update Product")
        self.geometry("400x300")

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

        category_label = ctk.CTkLabel(self, text="Category ID")
        category_label.pack(pady=5)
        self.category_entry = ctk.CTkEntry(self)
        self.category_entry.insert(0, product[5])
        self.category_entry.pack(pady=5)

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=10)

        update_button = ctk.CTkButton(button_frame, text="Update", command=self.update_product)
        update_button.pack(side=ctk.LEFT, padx=10)

        back_button = ctk.CTkButton(button_frame, text="Back", command=self.destroy)
        back_button.pack(side=ctk.LEFT, padx=10)

    def update_product(self):
        print(f"Updating product ID {self.product[0]}")
        self.controller.update_product(
            self.product[0],
            self.name_entry.get(),
            self.description_entry.get(),
            self.price_entry.get(),
            self.quantity_entry.get(),
            self.category_entry.get()
        )
        self.destroy()
