import hashlib
import random
import string
import tkinter as tk
from tkinter import messagebox

# Import the authentication, password generation, and password storage modules
from authentication import UserAuthentication
from password_generation import PasswordGenerator
from password_storage import PasswordStorage

class PasswordManagerGUI:
    def __init__(self):
        self.user_auth = UserAuthentication()
        self.password_gen = PasswordGenerator()
        self.password_store = PasswordStorage()

        self.window = tk.Tk()
        self.window.title("Password Manager")

        # Create and configure the GUI elements
        self.username_label = tk.Label(self.window, text="Username:")
        self.username_entry = tk.Entry(self.window)
        self.password_label = tk.Label(self.window, text="Password:")
        self.password_entry = tk.Entry(self.window, show="*")
        self.login_button = tk.Button(self.window, text="Login", command=self.login)
        self.register_button = tk.Button(self.window, text="Register", command=self.register)
        self.generate_password_button = tk.Button(self.window, text="Generate Password", command=self.generate_password)
        self.website_label = tk.Label(self.window, text="Website:")
        self.website_entry = tk.Entry(self.window)
        self.website_username_label = tk.Label(self.window, text="Username:")
        self.website_username_entry = tk.Entry(self.window)
        self.website_password_label = tk.Label(self.window, text="Password:")
        self.website_password_entry = tk.Entry(self.window, show="*")
        self.save_password_button = tk.Button(self.window, text="Save Password", command=self.save_password)
        self.retrieve_password_button = tk.Button(self.window, text="Retrieve Password", command=self.retrieve_password)

        # Position the GUI elements using the grid layout
        self.username_label.grid(row=0, column=0)
        self.username_entry.grid(row=0, column=1)
        self.password_label.grid(row=1, column=0)
        self.password_entry.grid(row=1, column=1)
        self.login_button.grid(row=2, column=0)
        self.register_button.grid(row=2, column=1)
        self.generate_password_button.grid(row=3, column=0, columnspan=2)
        self.website_label.grid(row=4, column=0)
        self.website_entry.grid(row=4, column=1)
        self.website_username_label.grid(row=5, column=0)
        self.website_username_entry.grid(row=5, column=1)
        self.website_password_label.grid(row=6, column=0)
        self.website_password_entry.grid(row=6, column=1)
        self.save_password_button.grid(row=7, column=0)
        self.retrieve_password_button.grid(row=7, column=1)

        # Create an instance of the main PasswordManager class
        self.password_manager = PasswordManager()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if self.password_manager.login_user(username, password):
            messagebox.showinfo("Success", "Login successful!")
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        self.password_manager.register_user(username, password)
        messagebox.showinfo("Success", "Registration successful!")

    def generate_password(self):
        password = self.password_manager.generate_password(length=12)
        self.website_password_entry.delete(0, tk.END)
        self.website_password_entry.insert(tk.END, password)

    def save_password(self):
        website = self.website_entry.get()
        username = self.website_username_entry.get()
        password = self.website_password_entry.get()
        
        self.password_manager.add_password(website, username, password)
        messagebox.showinfo("Success", "Password saved!")

    def retrieve_password(self):
        website = self.website_entry.get()
        username = self.website_username_entry.get()
        password = self.password_manager.get_password(website, username)
        
        if password:
            self.website_password_entry.delete(0, tk.END)
            self.website_password_entry.insert(tk.END, password)
        else:
            messagebox.showerror("Error", "Password not found.")

    def run(self):
        self.window.mainloop()

class PasswordManager:
    def __init__(self):
        self.user_auth = UserAuthentication()
        self.password_gen = PasswordGenerator()
        self.password_store = PasswordStorage()

    def login_user(self, username, password):
        return self.user_auth.login_user(username, password)

    def register_user(self, username, password):
        self.user_auth.register_user(username, password)

    def generate_password(self, length=12):
        return self.password_gen.generate_password(length)

    def add_password(self, website, username, password):
        self.password_store.add_password(website, username, password)

    def get_password(self, website, username):
        return self.password_store.get_password(website, username)

# Create an instance of the PasswordManagerGUI class and run it
if __name__ == '__main__':
    password_manager_gui = PasswordManagerGUI()
    password_manager_gui.run()
