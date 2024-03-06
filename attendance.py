import sqlite3

# Function to create tables
def create_tables():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()

    # Create students table
    c.execute("""CREATE TABLE IF NOT EXISTS students
                 (id INTEGER PRIMARY KEY, name TEXT, grade TEXT)""")

    # Create attendance table
    c.execute("""CREATE TABLE IF NOT EXISTS attendance
                 (id INTEGER PRIMARY KEY, date TEXT, student_id INTEGER,
                  status TEXT,
                  FOREIGN KEY(student_id) REFERENCES students(id))""")

    conn.commit()
    conn.close()

# Function to add a student to the database
def add_student(name, grade):
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("INSERT INTO students (name, grade) VALUES (?, ?)", (name, grade))
    conn.commit()
    conn.close()

# Function to take student attendance
def take_attendance(date, student_id, status):
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("INSERT INTO attendance (date, student_id, status) VALUES (?, ?, ?)", (date, student_id, status))
    conn.commit()
    conn.close()

# Function to calculate total attendance days for a student
def calculate_total_attendance_days(student_id):
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("SELECT status FROM attendance WHERE student_id = ?", (student_id,))
    records = c.fetchall()
    total_days = len(records)
    present_days = sum(1 for r in records if r[0] == "P")
    absent_days = total_days - present_days
    return (present_days, absent_days)

# Function to calculate attendance percentage for a student
def calculate_attendance_percentage(student_id):
    present_days, absent_days = calculate_total_attendance_days(student_id)
    total_days = present_days + absent_days
    percentage = (present_days / total_days) * 100
    return percentage

# Function to display list of defaulters
def display_defaulters(attendance_threshold):
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("SELECT s.name, s.grade FROM students s")
    records = c.fetchall()
    defaulters = []
    for r in records:
        student_id = r[0]
        percentage = calculate_attendance_percentage(student_id)
        if percentage < attendance_threshold:
            defaulters.append(r)
    print("Defaulters:")
    for defaulter in defaulters:
        print(defaulter[0], defaulter[1])

    conn.close()

