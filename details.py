from tkinter import *
from tkinter import messagebox
import tkinter as tk
import mysql.connector
# Create the main window
root = Tk()
root.title("Student Details")
root.geometry("800x1400")
bg_color = "#3A54D7"
bg_label = tk.Label(root, bg=bg_color)
bg_label.place(relwidth=1, relheight=1)
form_frame = tk.Frame(root, bg="white")
form_frame.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.7, anchor="center")



# Define function to add student details
def add_student():
    # Get student details from the input fields
    id = id_entry.get()
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    gender = gender_var.get()
    dob = dob_entry.get()

    # Check if any of the fields are empty
    if id == "" or name == "" or phone == "" or email == "" or address == "" or gender == "" or dob == "":
        messagebox.showerror("Error", "Please fill in all fields")
    else:
        # Connect to MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="yourdatabase"
        )
        cursor = db.cursor()

        # Insert student details into the database
        sql = "INSERT INTO students (id, name, phone, email, address, gender, dob) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (id, name, phone, email, address, gender, dob)
        cursor.execute(sql, values)
        db.commit()

        # Display the details in a message box
        message = f"ID: {id}\nName: {name}\nPhone: {phone}\nEmail: {email}\nAddress: {address}\nGender: {gender}\nDOB: {dob}"
        messagebox.showinfo("Student Details", message)

        # Clear the input fields
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        phone_entry.delete(0, END)
        email_entry.delete(0, END)
        address_entry.delete(0, END)
        dob_entry.delete(0, END)
        gender_var.set("")


# Create input fields for student details
id_label = Label(form_frame, text="ID:", font=("Arial", 22))
id_label.pack(pady=10)
id_entry = Entry(form_frame, font=("Arial", 22))
id_entry.pack(pady=5)

name_label = Label(form_frame, text="Name:", font=("Arial", 22))
name_label.pack(pady=10)
name_entry = Entry(form_frame, font=("Arial", 22))
name_entry.pack(pady=5)

phone_label = Label(form_frame, text="Phone:", font=("Arial", 22))
phone_label.pack(pady=10)
phone_entry = Entry(form_frame, font=("Arial", 22))
phone_entry.pack(pady=5)

email_label = Label(form_frame, text="Email:", font=("Arial", 22))
email_label.pack(pady=10)
email_entry = Entry(form_frame, font=("Arial", 22))
email_entry.pack(pady=5)

address_label = Label(form_frame, text="Address:", font=("Arial", 22))
address_label.pack(pady=10)
address_entry = Entry(form_frame, font=("Arial", 22))
address_entry.pack(pady=5)

gender_label = Label(form_frame, text="Gender:", font=("Arial", 22))
gender_label.pack(pady=10)

# Create radio buttons for gender
gender_var = StringVar()
male_radio = Radiobutton(form_frame, text="Male", variable=gender_var, value="Male", font=("Arial", 16))
male_radio.pack()
female_radio = Radiobutton(form_frame, text="Female", variable=gender_var, value="Female", font=("Arial", 16))
female_radio.pack()

dob_label = Label(form_frame, text="Date of Birth:", font=("Arial", 22))
dob_label.pack(pady=10)
dob_entry = Entry(form_frame, font=("Arial", 22))
dob_entry.pack(pady=5)

# Create button to add student details
add_button = Button(form_frame, text="Add Details", font=("Arial", 22), command=add_student)
add_button.pack(pady=22)

# Run the Tkinter event loop
root.mainloop()
