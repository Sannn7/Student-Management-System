from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk

def register():
    if username_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif username_entry.get() == 'saanika' and password_entry.get() == '1234':
        messagebox.showinfo('Success', 'Welcome')
        window.destroy()
        import details
    else:
        messagebox.showerror('Error', 'Please enter correct credentials')

def back():
    window.destroy()
    import Login
# Create a new Tkinter window
window = tk.Tk()

# Set window title and size
window.title("Sign Up")
window.geometry("800x400")

# Create pink background
bg_color = "#3A54D7"
bg_label = tk.Label(window, bg=bg_color)
bg_label.place(relwidth=1, relheight=1)

# Create white box around form
# Create white box around form
form_frame = tk.Frame(window, bg="white")
form_frame.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.7, anchor="center")


# Create labels and entry fields for username, email, and password
username_label = tk.Label(form_frame, text="Username:", font=("Arial", 22), bg="white")
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
username_entry = tk.Entry(form_frame, font=("Arial", 22))
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = tk.Label(form_frame, text="Password:", font=("Arial", 22), bg="white")
password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
password_entry = tk.Entry(form_frame, show="*", font=("Arial", 22))
password_entry.grid(row=1, column=1, padx=10, pady=10)


# Create sign-up button
sign_up_button = tk.Button(form_frame, text="Sign Up", font=("Arial", 22), command=register)
sign_up_button.grid(row=2, column=0, columnspan=2, pady=20)

go_back_button = tk.Button(form_frame, text="Back to Home page", font=("Arial", 22), command=back)
go_back_button.grid(row=3, column=0, columnspan=2, pady=10)



# Run the Tkinter event loop
window.mainloop()
