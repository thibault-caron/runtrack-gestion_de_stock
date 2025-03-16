import customtkinter as ctk

class ErrorPopup(ctk.CTkToplevel):
    def __init__(self, parent, message):
        super().__init__(parent)
        self.title("Error")
        self.geometry("300x150")
        self.transient(parent)  # Set the parent window
        self.lift()  # Bring the popup to the front

        label = ctk.CTkLabel(self, text=message)
        label.pack(pady=20)

        ok_button = ctk.CTkButton(self, text="OK", command=self.destroy)
        ok_button.pack(pady=10)
