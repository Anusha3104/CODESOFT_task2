import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip  # For copy-to-clipboard functionality

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        
        # Variables
        self.password_var = tk.StringVar()
        self.length_var = tk.IntVar(value=12)
        self.upper_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.special_var = tk.BooleanVar(value=True)
        
        # UI Setup
        self.setup_ui()
    
    def setup_ui(self):
        # Main Frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        ttk.Label(
            main_frame, 
            text="Password Generator", 
            font=('Helvetica', 16, 'bold')
        ).pack(pady=10)
        
        # Password Length
        length_frame = ttk.Frame(main_frame)
        length_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(length_frame, text="Password Length:").pack(side=tk.LEFT)
        length_slider = ttk.Scale(
            length_frame,
            from_=8,
            to=64,
            variable=self.length_var,
            command=lambda v: self.length_var.set(int(float(v)))
        )
        length_slider.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=10)
        length_value = ttk.Label(length_frame, textvariable=self.length_var)
        length_value.pack(side=tk.LEFT)
        
        # Complexity Options
        options_frame = ttk.LabelFrame(main_frame, text="Options", padding=10)
        options_frame.pack(fill=tk.X, pady=10)
        
        ttk.Checkbutton(
            options_frame,
            text="Include Uppercase Letters (A-Z)",
            variable=self.upper_var
        ).pack(anchor=tk.W)
        
        ttk.Checkbutton(
            options_frame,
            text="Include Digits (0-9)",
            variable=self.digits_var
        ).pack(anchor=tk.W)
        
        ttk.Checkbutton(
            options_frame,
            text="Include Special Characters (!@#...)",
            variable=self.special_var
        ).pack(anchor=tk.W)
        
        # Generate Button
        ttk.Button(
            main_frame,
            text="Generate Password",
            command=self.generate_password
        ).pack(pady=10)
        
        # Password Display
        ttk.Label(main_frame, text="Generated Password:").pack()
        
        password_entry = ttk.Entry(
            main_frame,
            textvariable=self.password_var,
            font=('Courier', 12),
            state='readonly',
            justify='center'
        )
        password_entry.pack(fill=tk.X, pady=5)
        
        # Copy Button
        ttk.Button(
            main_frame,
            text="Copy to Clipboard",
            command=self.copy_to_clipboard
        ).pack(pady=5)
    
    def generate_password(self):
    
        length = self.length_var.get()
        chars = string.ascii_lowercase
        
        if self.upper_var.get():
            chars += string.ascii_uppercase
        if self.digits_var.get():
            chars += string.digits
        if self.special_var.get():
            chars += string.punctuation
        
        password = ''.join(random.choice(chars) for _ in range(length))
        self.password_var.set(password)
    
    def copy_to_clipboard(self):
        """Copy generated password to clipboard"""
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password generated yet!")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    app.run()
