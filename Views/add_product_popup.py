import customtkinter as ctk

class AddProductPopup(ctk.CTkToplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Add Product")
        self.geometry("400x300")

        name_label = ctk.CTkLabel(self, text="Name")
        name_label.pack(pady=5)
        self.name_entry = ctk.CTkEntry(self)
        self.name_entry.pack(pady=5)

        description_label = ctk.CTkLabel(self, text="Description")
        description_label.pack(pady=5)
        self.description_entry = ctk.CTkEntry(self)
        self.description_entry.pack(pady=5)

        price_label = ctk.CTkLabel(self, text="Price")
        price_label.pack(pady=5)
        self.price_entry = ctk.CTkEntry(self)
        self.price_entry.pack(pady=5)

        quantity_label = ctk.CTkLabel(self, text="Quantity")
        quantity_label.pack(pady=5)
        self.quantity_entry = ctk.CTkEntry(self)
        self.quantity_entry.pack(pady=5)

        category_label = ctk.CTkLabel(self, text="Category ID")
        category_label.pack(pady=5)
        self.category_entry = ctk.CTkEntry(self)
        self.category_entry.pack(pady=5)

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=10)

        add_button = ctk.CTkButton(button_frame, text="Add", command=self.add_product)
        add_button.pack(side=ctk.LEFT, padx=10)

        back_button = ctk.CTkButton(button_frame, text="Back", command=self.destroy)
        back_button.pack(side=ctk.LEFT, padx=10)

    def add_product(self):
        self.controller.add_product(
            self.name_entry.get(),
            self.description_entry.get(),
            self.price_entry.get(),
            self.quantity_entry.get(),
            self.category_entry.get()
        )
        self.destroy()
