import customtkinter as ctk

class DeleteProductPopup(ctk.CTkToplevel):
    def __init__(self, controller, product_id):
        super().__init__()
        self.controller = controller
        self.product_id = product_id
        self.title("Delete Product")
        self.geometry("250x150")
        self.transient(controller.view)  # Set the parent window
        self.lift()  # Bring the popup to the front

        label = ctk.CTkLabel(self, text=f"Are you sure you want to delete product ID {product_id}?")
        label.pack(pady=20)

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=10)

        confirm_button = ctk.CTkButton(button_frame, text="Confirm", command=self.delete_product)
        confirm_button.pack(side=ctk.LEFT, padx=10)

        back_button = ctk.CTkButton(button_frame, text="Back", command=self.destroy)
        back_button.pack(side=ctk.LEFT, padx=10)

    def delete_product(self):
        print(f"Deleting product ID {self.product_id}")
        self.controller.delete_product(self.product_id)
        self.destroy()
