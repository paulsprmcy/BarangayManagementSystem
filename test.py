import tkinter as tk
from tkinter import font as tkFont
from tkinter.ttk import Combobox
from tkinter import Button, Label, Entry

class MyApp:
    def __init__(self, window):
        self.window = window
        self.window.configure(bg="#F4F7FC")
        self.add_needs()

    def add_needs(self):
        self.clear_window()

        # Fetch street options
        street_options = [street[1] for street in self.get_streets_names()]

        # Set modern font styles
        label_font = tkFont.Font(family="Roboto", size=12)
        entry_font = tkFont.Font(family="Roboto", size=12)

        # Street Name Label
        self.street_id_label = Label(self.window, text="Street Name", bg="#F4F7FC", font=label_font, fg="#333")
        self.street_id_label.pack(pady=(30, 10), anchor='w', padx=30)

        # Street Name Combobox (with rounded corners and subtle shadow)
        self.street_name_entry = Combobox(self.window, values=street_options, font=entry_font, state="readonly", width=20)
        self.street_name_entry.pack(pady=(0, 20), padx=30)
        self.street_name_entry.config(height=2, style="TCombobox")
        self.apply_shadow(self.street_name_entry)

        # Street Need Label
        self.need_name_label = Label(self.window, text="Street Need", bg="#F4F7FC", font=label_font, fg="#333")
        self.need_name_label.pack(pady=5, anchor='w', padx=30)

        # Street Need Entry (with rounded corners and shadow effect)
        self.need_name_entry = Entry(self.window, font=entry_font, bd=2, relief="solid", highlightthickness=0)
        self.need_name_entry.pack(pady=(0, 20), padx=30)
        self.apply_shadow(self.need_name_entry)

        # Service Label
        self.service_label = Label(self.window, text="Service", bg="#F4F7FC", font=label_font, fg="#333")
        self.service_label.pack(pady=5, anchor='w', padx=30)

        # Service Combobox (with rounded corners)
        services = ['Health', 'Education', 'Social Welfare']
        self.service_entry = Combobox(self.window, values=services, font=entry_font, state="readonly", width=20)
        self.service_entry.pack(pady=(0, 20), padx=30)
        self.service_entry.config(height=2, style="TCombobox")
        self.apply_shadow(self.service_entry)

        # Add Need Button (with modern gradient effect and hover effect)
        self.add_need_button = Button(self.window, text="Add Need", command=self.apply_add_need,
                                      font=("Roboto", 12, "bold"), bg="#2196F3", fg="white", relief="flat", padx=30, pady=12)
        self.add_need_button.pack(pady=(10, 20))
        self.apply_button_gradient(self.add_need_button)

        # Back Button (with rounded corners and hover effect)
        self.back_button = Button(self.window, text="Back", command=self.main_menu, font=("Roboto", 12), bg="#FFEB3B", fg="black", relief="flat", padx=30, pady=12)
        self.back_button.pack(pady=(0, 30))
        self.apply_button_gradient(self.back_button)

    def apply_shadow(self, widget):
        """Adds a shadow effect to a widget (e.g., Entry fields)."""
        widget.bind("<FocusIn>", lambda event: widget.config(highlightbackground="gray", highlightthickness=2))
        widget.bind("<FocusOut>", lambda event: widget.config(highlightbackground="lightgray", highlightthickness=1))

    def apply_button_gradient(self, button):
        """Applies a gradient background to buttons."""
        button.config(relief="flat")
        button.config(bg="#2196F3", fg="white")
        # If you have the capability, apply a gradient effect here (using images or advanced methods)
        button.bind("<Enter>", lambda e: button.config(bg="#1E88E5"))  # Hover effect
        button.bind("<Leave>", lambda e: button.config(bg="#2196F3"))  # Reset on mouse leave

    def clear_window(self):
        """Clears the window to add new widgets."""
        for widget in self.window.winfo_children():
            widget.destroy()

    def get_streets_names(self):
        """This is a mock function to simulate street names retrieval."""
        return [(1, "Main Street"), (2, "Second Avenue"), (3, "Elm Street")]

    def apply_add_need(self):
        """Dummy function to handle Add Need button click."""
        print("Adding need...")

    def main_menu(self):
        """Dummy function for the back button action."""
        print("Returning to main menu...")

# Example of how to use this class
if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
