from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from BarangayService import Service
import tkinter.font as tkFont
from prettytable import PrettyTable
from tkinter import ttk
from tkinter.ttk import Combobox
logo = "./images/logo.png"
bg = "./images/background.jpg"


def on_enter(button, color):
    button['background'] = color


def on_leave(button, color):
    button['background'] = color
class BarangaySystem:
    def __init__(self,tk):
        self.service = Service()
        self.window = tk

        self.logo_image = None

    def start(self):
        self.window.title("Barangay Management System")

        # Define the window dimensions
        window_width = 900
        window_height = 700
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Calculate the position of the window to center it
        x_offset = (screen_width // 2) - (window_width // 2)
        y_offset = (screen_height // 2) - (window_height // 2)

        # Set the window size and position
        self.window.geometry(f"{window_width}x{window_height}+{x_offset}+{y_offset}")
        self.window.resizable(False, False)

        # Add background image


        # Start with the login screent
        self.login_screen()

        self.window.mainloop()
    def logo_image(self):
        image = Image.open(logo)
        image = image.resize((200, 200))  # Resize image
        image = ImageTk.PhotoImage(image)

        logo_image = Label(self.window, image=image)
        logo_image.image = image  # Keep a reference to avoid garbage collection
        logo_image.pack()

    def login_screen(self):
        self.clear_window()  # Clear any existing widgets
        self.window.resizable(False, False)

        # Create a resizable frame
        frame = Frame(self.window,borderwidth=3,highlightcolor="blue",highlightthickness=3,highlightbackground="blue")
        frame.pack(expand=True, fill="both", padx=100, pady=100)  # Allow the frame to expand and fill the space


        # Resize the image properly
        image = Image.open(logo)
        image = image.resize((100, 100))  # Resize image
        image = ImageTk.PhotoImage(image)

        logo_image = Label(frame, image=image)
        logo_image.image = image  # Keep a reference to avoid garbage collection
        logo_image.pack()
        title = Label(frame, text="Barangay Management System" ,font=("Arial", 17),fg="blue")
        title.pack(pady=10)

        # Username and password entry widgets
        self.username_label = Label(frame, text="Username:", font=("Arial", 12))
        self.username_label.pack(pady=10)

        self.username_entry = Entry(frame, font=("Arial", 14, "bold"))
        self.username_entry.pack(pady=10)

        self.password_label = Label(frame, text="Password:", font=("Arial", 12,'bold') )
        self.password_label.pack(pady=10)

        self.password_entry = Entry(frame, show="*", font=("Arial", 14))
        self.password_entry.pack(pady=10)

        # Login button
        self.login_button = Button(frame, text="Login", command=self.login, font=("Arial", 12, "bold"),
                                   bg="#4CAF50", fg="white")
        self.login_button.pack(pady=20)

        # Register button
        self.register_button = Button(frame, text="Register", command=self.register_screen, font=("Arial", 12),
                                      bg="#2196F3", fg="white")
        self.register_button.pack(pady=5)

        # Allow the window to be resized
        self.window.resizable(True, True)  # Enable window resizing

    def register_screen(self):
        self.clear_window()
        # Create a resizable frame
        frame = Frame(self.window, borderwidth=3, highlightcolor="blue", highlightthickness=3,
                      highlightbackground="blue")
        frame.pack(expand=True, fill="both", padx=100, pady=100)  # Allow the frame to expand and fill the space

        image = Image.open("./images/logo.png")
        image = image.resize((100, 100))  # Resize image to desired dimensions (width, height)
        image = ImageTk.PhotoImage(image)

        self.logo_image = image  # Keep a reference to the image
        logo_image = Label(frame, image=self.logo_image)
        logo_image.pack()

        self.username_label = Label(frame, text="Username:", bg="white", font=("Arial", 12))
        self.username_label.pack(pady=10)
        self.username_entry = Entry(frame, font=("Arial", 12))
        self.username_entry.pack(pady=10)

        self.password_label = Label(frame, text="Password:", bg="white", font=("Arial", 12))
        self.password_label.pack(pady=10)
        self.password_entry = Entry(frame, show="*", font=("Arial", 12))
        self.password_entry.pack(pady=10)

        self.register_button = Button(frame, text="Register", command=self.register, font=("Arial", 12, "bold"),
                                      bg="#FF5722", fg="white")
        self.register_button.pack(pady=20)

        self.login_button = Button(frame, text="Back to Login", command=self.login_screen, font=("Arial", 12),
                                   bg="#FFEB3B", fg="black")
        self.login_button.pack(pady=5)
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.service.start_connection()
        if self.service.login(username, password):
            messagebox.showinfo("Login Successful", f"Welcome {username}")
            self.main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def register(self):

       try:

           username = self.username_entry.get()
           password = self.password_entry.get()
           print("****",username,password)
           if username and password:
               self.service.start_connection()
               res = self.service.register(username, password)
               messagebox.showinfo("Registration Successful", f"{res}")
               self.login_screen()
           else:
               messagebox.showerror("Error", "Please fill in both fields.")
       except Exception as e:
            print(e)

    def main_menu(self):
        # Clear the window to reset the view
        self.clear_window()

        # Set background color for the window
        self.window.configure(bg="#f4f4f4")

        # Title Label for the Main Menu (Large Font, Centered)
        title_label = Label(self.window, text="Main Menu", font=("Arial", 24, "bold"), bg="#f4f4f4", fg="#333")
        title_label.grid(row=0, column=0, columnspan=3, pady=30)

        # Create a frame for the buttons to make them more aligned and structured
        button_frame = Frame(self.window, bg="#f4f4f4")
        button_frame.grid(row=1, column=0, padx=20, pady=20, columnspan=3)

        # Button styles (Modern Design with rounded edges and consistent color scheme)
        button_style = {
            "font": ("Arial", 14, "bold"),
            "width": 20,
            "height": 2,
            "relief": RAISED,
            "bd": 3,
            "padx": 10,
            "pady": 10
        }

        # Add buttons to the layout with a 2-column grid
        buttons = [
            ("View Streets", self.view_streets, "#4CAF50"),
            ("View Projects", self.view_projects, "#2196F3"),
            ("Update Funds", self.update_funds, "#FF9800"),
            ("Add Project", self.add_project, "#8BC34A"),
            ("View Needs", self.view_needs, "#FFEB3B"),
            ("Add Need", self.add_needs, "#FF5722"),
            ("Logout", self.logout, "#F44336")
        ]

        # Position buttons in a 2-column grid
        row = 0
        col = 0
        for text, command, color in buttons:
            button = Button(button_frame, text=text, command=command, bg=color, fg="white", **button_style)
            button.grid(row=row, column=col, padx=10, pady=10, sticky="ew")
            # Move to the next row and column
            col += 1
            if col > 1:  # Move to the next row after 2 columns
                col = 0
                row += 1
        # for button in button_frame.winfo_children():
        #     button.bind("<Enter>", lambda event, button=button: on_enter(button, "#388E3C"))
        #     button.bind("<Leave>", lambda event, button=button: on_leave(button, "#4CAF50"))
        # Button hover effect (optional)




        # Footer Label for copyright (subtle and centered at the bottom)
        footer_label = Label(self.window, text="© 2024 Street Management System", font=("Arial", 10), bg="#f4f4f4",
                             fg="#555")
        footer_label.grid(row=row + 1, column=0, columnspan=3, pady=10)

        # Set window size (optional for uniformity)
        # self.window.geometry("600x600")

    def view_streets(self):
        # Clear the window to reset the view
        self.clear_window()

        # Fetch the list of streets from the service (assuming the service returns a list of tuples or dictionaries)
        try:
            self.service.start_connection()
            streets = self.service.get_streets()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load streets: {e}")
            return

        # Set the column names for the Treeview
        columns = ["ID", "Street Name", "Current Funds"]

        # Create a Treeview widget with modern styling
        tree = ttk.Treeview(self.window, columns=columns, show="headings", height=10)

        # Define column properties with enhanced styling
        tree.heading("ID", text="ID", anchor="center")
        tree.heading("Street Name", text="Street Name", anchor="center")
        tree.heading("Current Funds", text="Current Funds", anchor="center")

        # Set column width and text alignment for better visual appeal
        tree.column("ID", width=80, anchor="center")
        tree.column("Street Name", width=250, anchor="center")
        tree.column("Current Funds", width=120, anchor="center")

        # Add a modern color scheme for treeview appearance
        style = ttk.Style(self.window)
        style.configure("Treeview",
                        background="#f4f4f4",
                        foreground="black",
                        rowheight=25,
                        font=("Arial", 12))
        style.configure("Treeview.Heading",
                        background="#4CAF50",
                        foreground="black",
                        font=("Arial", 12, "bold"))
        style.map("Treeview", background=[('selected', '#a3d8a0')])

        # Insert the rows into the Treeview
        for street in streets:
            tree.insert("", "end", values=street)

        # Create a Scrollbar for the Treeview
        scrollbar = Scrollbar(self.window, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Place the Treeview in the window with padding and layout management
        tree.pack(padx=20, pady=20, fill=BOTH, expand=True)

        # Add a Back Button with modern design and padding
        back_button = Button(self.window, text="Back", command=self.main_menu,
                             font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief=RAISED, bd=2)
        back_button.pack(pady=20, fill=X, padx=50)

        # Optional: Add a title label for clarity
        title_label = Label(self.window, text="Streets Information", font=("Arial", 16, "bold"), bg="#f4f4f4")
        title_label.pack(pady=10)

    def get_streets_names(self):
        try:
            self.service.start_connection()
            streets = self.service.get_streets()
            return streets
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load streets: {e}")
            return []

    def update_funds(self):
        self.clear_window()

        # Frame for content
        form_frame = Frame(self.window, bg="#f4f4f4")
        form_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Street selection
        street_options = []  # Replace with dynamic street names
        streets = self.get_streets_names()
        for street in streets:
            street_options.append(street[1])
        self.street_id_label = Label(form_frame, text="Street:", bg="#f4f4f4", font=("Arial", 12))
        self.street_id_label.grid(row=0, column=0, sticky="w", pady=8)
        self.street_id_entry = Combobox(form_frame, values=street_options, font=("Arial", 15), state="readonly")
        self.street_id_entry.grid(row=0, column=1, pady=8, sticky="ew")

        # New Funds input
        self.new_funds_label = Label(form_frame, text="New Funds:", bg="#f4f4f4", font=("Arial", 12))
        self.new_funds_label.grid(row=1, column=0, sticky="w", pady=8)
        self.new_funds_entry = Entry(form_frame, font=("Arial", 12))
        self.new_funds_entry.grid(row=1, column=1, pady=8, sticky="ew")

        # Buttons
        self.update_button = Button(self.window, text="Update", command=self.apply_funds_update,
                                    font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief="flat", bd=0)
        self.update_button.pack(pady=20, ipadx=20, ipady=10, fill="x")

        self.back_button = Button(self.window, text="Back", command=self.main_menu, font=("Arial", 12),
                                  bg="#FFEB3B", fg="black", relief="flat", bd=0)
        self.back_button.pack(pady=5, ipadx=20, ipady=10, fill="x")

    def apply_funds_update(self):
        try:
            street_id = self.street_id_entry.get()
            new_funds = float(self.new_funds_entry.get())
            self.service.start_connection()
            message = self.service.add_funds(street_id, new_funds)
            messagebox.showinfo("Funds Update", message)
            self.main_menu()
        except Exception as e:
            print(e)
            messagebox.showerror("Invalid Input", "Please enter valid street ID and funds.")

    def add_project(self):
        self.clear_window()

        # Frame for content
        form_frame = Frame(self.window, bg="#f4f4f4")
        form_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Street selection
        street_options = []  # Replace with dynamic street names
        streets = self.get_streets_names()
        for street in streets:
            street_options.append(street[1])
        self.street_label = Label(form_frame, text="Street:", bg="#f4f4f4", font=("Arial", 12))
        self.street_label.grid(row=0, column=0, sticky="w", pady=8)
        self.street_entry = Combobox(form_frame, values=street_options, font=("Arial", 15), state="readonly")
        self.street_entry.grid(row=0, column=1, pady=8, sticky="ew")

        # Project input
        self.project_label = Label(form_frame, text="Project:", bg="#f4f4f4", font=("Arial", 12))
        self.project_label.grid(row=1, column=0, sticky="w", pady=8)
        self.project_entry = Entry(form_frame, font=("Arial", 15))
        self.project_entry.grid(row=1, column=1, pady=8, sticky="ew")

        # Spend Amount input
        self.spend_label = Label(form_frame, text="Spend Amount:", bg="#f4f4f4", font=("Arial", 12))
        self.spend_label.grid(row=2, column=0, sticky="w", pady=8)
        self.spend_entry = Entry(form_frame, font=("Arial", 15))
        self.spend_entry.grid(row=2, column=1, pady=8, sticky="ew")

        # Service selection
        services = ['Health', 'Education', 'Social Welfare']
        self.service_label = Label(form_frame, text="Service:", bg="#f4f4f4", font=("Arial", 12))
        self.service_label.grid(row=3, column=0, sticky="w", pady=8)
        self.service_entry = Combobox(form_frame, values=services, font=("Arial", 15), state="readonly")
        self.service_entry.grid(row=3, column=1, pady=8, sticky="ew")

        # Area selection
        areas = ['Road', 'Water', 'Drainage']
        self.area_label = Label(form_frame, text="Area:", bg="#f4f4f4", font=("Arial", 12))
        self.area_label.grid(row=4, column=0, sticky="w", pady=8)
        self.area_entry = Combobox(form_frame, values=areas, font=("Arial", 15), state="readonly")
        self.area_entry.grid(row=4, column=1, pady=8, sticky="ew")

        # Buttons
        self.add_button = Button(self.window, text="Add Project", command=self.apply_add_project,
                                 font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief="flat", bd=0)
        self.add_button.pack(pady=20, ipadx=20, ipady=10, fill="x")

        self.back_button = Button(self.window, text="Back", command=self.main_menu, font=("Arial", 12),
                                  bg="#FFEB3B", fg="black", relief="flat", bd=0)
        self.back_button.pack(pady=5, ipadx=20, ipady=10, fill="x")

    def apply_add_need(self):
        street_name = self.street_name_entry.get()  # Get the selected street ID
        need_name = self.need_name_entry.get()  # Get the need name from the entry
        service = self.service_entry.get()  # Get the service type from the entry


        if street_name and need_name and service :
            try:
                result = self.service.add_street_needs(street_name, need_name, service)
                messagebox.showinfo("Need Added", result)
            except ValueError:
                messagebox.showerror("Invalid Input", "Priority must be an integer.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def on_tree_item_select(self,event):
        selected_item = event.widget.selection()  # Get the selected item
        if selected_item:
            # Get the 'Need' or 'Location' value for prioritization
            need_id = event.widget.item(selected_item[0], 'values')[0]  # Assuming ID is the first column
            street = event.widget.item(selected_item[0], 'values')[1]  # Assuming Location is in column 5
            # Ask if the user wants to set the priority for this item
            response = messagebox.askyesno("Set Priority", f"Are you sure to set Status Finished for {street} street?")
            if response:
                # Call set_priority function if confirmed
                res = self.service.update_status(need_id)
                if res:
                    self.view_needs()
    def view_needs(self):
        # Clear the window to reset the view
        self.clear_window()

        try:
            needs = self.service.get_needs()  # Assuming this fetches needs from DB or API
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load community needs: {e}")
            return

        columns = ["ID","Street", "Need", "Service", "Date", "Status"]

        tree = ttk.Treeview(self.window, columns=columns, show="headings", height=10)
        tree.heading("ID", text="ID", anchor="center")
        tree.heading("Street", text="Street", anchor="center")
        tree.heading("Need", text="Need", anchor="center")
        tree.heading("Service", text="Service", anchor="center")
        tree.heading("Date", text="Date", anchor="center")
        tree.heading("Status", text="Status", anchor="center")

        tree.column("ID", width=50, anchor="center")
        tree.column("Street", width=50, anchor="center")
        tree.column("Need", width=150, anchor="center")
        tree.column("Service", width=200, anchor="center")
        tree.column("Date", width=150, anchor="center")
        tree.column("Status", width=120, anchor="center")

        style = ttk.Style(self.window)
        style.configure("Treeview", background="#f4f4f4", foreground="black", rowheight=25, font=("Arial", 12))
        style.configure("Treeview.Heading", background="#4CAF50", foreground="black", font=("Arial", 12, "bold"))
        style.map("Treeview", background=[('selected', '#a3d8a0')])

        # Insert the rows into the Treeview
        for need in needs:
            tree.insert("", "end", values=need)

        # Create a Scrollbar for the Treeview
        scrollbar = Scrollbar(self.window, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Place the Treeview in the window
        tree.pack(padx=20, pady=20, fill=BOTH, expand=True)

        # Add a Back Button
        back_button = Button(self.window, text="Back", command=self.main_menu,
                             font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief="raised", bd=2)
        back_button.pack(pady=20, fill=X, padx=50)

        # Optional: Add a title label
        title_label = Label(self.window, text="Community Needs Information", font=("Arial", 16, "bold"), bg="#f4f4f4")
        title_label.pack(pady=10)

        # Bind the Treeview selection event to the set_priority function
        tree.bind("<ButtonRelease-1>", self.on_tree_item_select)

    def on_tree_item_select_2(self, event):
        selected_item = event.widget.selection()  # Get the selected item
        if selected_item:
            # Get the 'Street', 'Project' and 'Spend' values for prioritization
            project_id = event.widget.item(selected_item[0], 'values')[0]  # Assuming ID is the first column
            street = event.widget.item(selected_item[0], 'values')[1]  # Assuming Street is in column 2
            spend = float(event.widget.item(selected_item[0], 'values')[3])  # Assuming Spend is in column 4

            # Ask if the user wants to mark the project as done and decrease the funds
            response = messagebox.askyesno("Mark Project as Done",
                                           f"Do you want to mark the project at {street} as done and decrease funds by {spend}?")
            if response:
                # Call the update_funds function and mark project as done
                self.service.update_funds(street, spend)
                self.service.mark_project_as_done(project_id)

    def view_projects(self):
        # Clear the window to reset the view
        self.clear_window()

        # Fetch the list of projects from the service
        try:
            projects = self.service.get_projects()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load projects: {e}")
            return

        # Define the column names for the Treeview
        columns = ["ID", "Street", "Project", "Spend", "Service", "Area", "Date","Status"]

        # Create the Treeview widget with modern styling
        tree = ttk.Treeview(self.window, columns=columns, show="headings", height=10)

        # Define column properties with enhanced styling
        tree.heading("ID", text="ID", anchor="center")
        tree.heading("Street", text="Street", anchor="center")
        tree.heading("Project", text="Project", anchor="center")
        tree.heading("Spend", text="Spend", anchor="center")
        tree.heading("Service", text="Service", anchor="center")
        tree.heading("Area", text="Area", anchor="center")
        tree.heading("Date", text="Date", anchor="center")
        tree.heading("Status", text="Status", anchor="center")

        # Set column width and text alignment for better visual appeal
        tree.column("ID", width=50, anchor="center")
        tree.column("Street", width=150, anchor="center")
        tree.column("Project", width=200, anchor="center")
        tree.column("Spend", width=100, anchor="center")
        tree.column("Service", width=150, anchor="center")
        tree.column("Area", width=150, anchor="center")
        tree.column("Date", width=150, anchor="center")
        tree.column("Status", width=150, anchor="center")

        # Add a modern color scheme for Treeview appearance
        style = ttk.Style(self.window)
        style.configure("Treeview", background="#f4f4f4", foreground="black", rowheight=25, font=("Arial", 12))
        style.configure("Treeview.Heading", background="#4CAF50", foreground="black", font=("Arial", 12, "bold"))
        style.map("Treeview", background=[('selected', '#a3d8a0')])

        # Insert the rows into the Treeview
        for project in projects:
            # Assuming each project is a tuple: (ID, Street, Project, Spend, Date, Service, Area)
            tree.insert("", "end", values=project)

        # Create a Scrollbar for the Treeview
        scrollbar = Scrollbar(self.window, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Place the Treeview in the window with padding and layout management
        tree.pack(padx=20, pady=20, fill=BOTH, expand=True)

        # Add a Back Button with modern design and padding
        back_button = Button(self.window, text="Back", command=self.main_menu,
                             font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief="raised", bd=2)
        back_button.pack(pady=20, fill=X, padx=50)

        # Optional: Add a title label for clarity
        title_label = Label(self.window, text="Projects Information", font=("Arial", 16, "bold"), bg="#f4f4f4")
        title_label.pack(pady=10)

        # Bind the Treeview selection event to the mark_as_done function
        tree.bind("<ButtonRelease-1>", self.on_tree_item_select_2)

    def add_needs(self):
        self.clear_window()

        # Frame for content
        form_frame = Frame(self.window, bg="#F4F7FC")
        form_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Fetch street options
        street_options = []  # Replace with dynamic street names
        streets = self.get_streets_names()
        for street in streets:
            street_options.append(street[1])
        # Set modern font styles
        label_font = tkFont.Font(family="Roboto", size=15)
        entry_font = tkFont.Font(family="Roboto", size=15)

        # Street Name Label
        self.street_id_label = Label(form_frame, text="Street Name", bg="#F4F7FC", font=label_font, fg="#333")
        self.street_id_label.grid(row=0, column=0, sticky="w", pady=10)

        # Street Name Combobox
        self.street_name_entry = Combobox(form_frame, values=street_options, font=entry_font, state="readonly",
                                          width=20)
        self.street_name_entry.grid(row=0, column=1, pady=10, sticky="ew")
        self.street_name_entry.config(height=2, style="TCombobox")

        # Street Need Label
        self.need_name_label = Label(form_frame, text="Street Need", bg="#F4F7FC", font=label_font, fg="#333")
        self.need_name_label.grid(row=1, column=0, sticky="w", pady=10)

        # Street Need Entry
        self.need_name_entry = Entry(form_frame, font=entry_font, bd=2, relief="solid", highlightthickness=0)
        self.need_name_entry.grid(row=1, column=1, pady=10, sticky="ew")
        self.apply_shadow(self.need_name_entry)

        # Service Label
        self.service_label = Label(form_frame, text="Service", bg="#F4F7FC", font=label_font, fg="#333")
        self.service_label.grid(row=2, column=0, sticky="w", pady=10)

        # Service Combobox
        services = ['Health', 'Education', 'Social Welfare']
        self.service_entry = Combobox(form_frame, values=services, font=entry_font, state="readonly", width=20)
        self.service_entry.grid(row=2, column=1, pady=10, sticky="ew")
        self.service_entry.config(height=2, style="TCombobox")

        # Add Need Button
        self.add_need_button = Button(self.window, text="Add Need", command=self.apply_add_need,
                                      font=("Arial", 12, "bold"), bg="#2196F3", fg="white", relief="flat", padx=30,
                                      pady=12)
        self.add_need_button.pack(pady=(10, 20))
        self.apply_button_gradient(self.add_need_button)

        # Back Button
        self.back_button = Button(self.window, text="Back", command=self.main_menu, font=("Arial", 12),
                                  bg="#FFEB3B", fg="black", relief="flat", padx=30, pady=12)
        self.back_button.pack(pady=(0, 30))
        self.apply_button_gradient(self.back_button)

    def apply_shadow(self, widget):
        """ Adds a shadow effect to a widget (e.g., Entry fields). """
        widget.bind("<FocusIn>", lambda event: widget.config(highlightbackground="gray", highlightthickness=2))
        widget.bind("<FocusOut>", lambda event: widget.config(highlightbackground="lightgray", highlightthickness=1))

    def apply_button_gradient(self, button):
        """ Applies a gradient background to buttons. """
        button.config(relief="flat")
        button.config(bg="#2196F3", fg="white")
        # This can be enhanced with a gradient color effect if you use an image or advanced techniques in Tkinter.

    def apply_shadow(self, widget):
        """ Adds a shadow effect to a widget (e.g., Entry fields). """
        widget.bind("<FocusIn>", lambda event: widget.config(highlightbackground="gray", highlightthickness=2))
        widget.bind("<FocusOut>", lambda event: widget.config(highlightbackground="lightgray", highlightthickness=1))

    def apply_button_gradient(self, button):
        """ Applies a gradient background to buttons. """
        button.config(relief="flat")
        button.config(bg="#2196F3", fg="white")
        # This can be enhanced with a gradient color effect if you use an image or advanced techniques in Tkinter.
    def apply_add_project(self):
        street = self.street_entry.get()
        project = self.project_entry.get()
        try:
            self.service.start_connection()
            spend = float(self.spend_entry.get())
            service = self.service_entry.get()
            area = self.area_entry.get()

            message = self.service.add_projects(street, project, spend, service, area)
            messagebox.showinfo("Add Project", message)
            self.main_menu()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid spend amount.")

    def show_data(self, title, data):
        self.clear_window()
        data_label = Label(self.window, text=f"{title}:\n{data}", bg="white", font=("Arial", 12))
        data_label.pack(pady=10)

        back_button = Button(self.window, text="Back", command=self.main_menu, font=("Arial", 12), bg="#FFEB3B",
                             fg="black")
        back_button.pack(pady=10)

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def logout(self):
        self.clear_window()
        self.login_screen()


if __name__ == "__main__":
    tk = Tk()
    tk.resizable(False,False)
    system = BarangaySystem(tk)
    system.start()
