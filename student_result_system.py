import sqlite3
import csv

# ================= DATABASE =================
cur.execute("DROP TABLE IF EXISTS students")

cur.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    m1 INTEGER,
    m2 INTEGER,
    m3 INTEGER,
    total INTEGER,
    gpa REAL,
    grade TEXT
)
""")
conn.commit()

# ================= SAFE INPUT =================
def safe_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            val = int(input(prompt))
            if min_val is not None and val < min_val:
                print(f"⚠️ Value must be ≥ {min_val}")
                continue
            if max_val is not None and val > max_val:
                print(f"⚠️ Value must be ≤ {max_val}")
                continue
            return val
        except ValueError:
            print("⚠️ Invalid input! Enter a number.")

# ================= AUTH =================
def admin_login():
    return input("Username: ") == "admin" and input("Password: ") == "admin123"

# ================= GPA & GRADE =================
def calculate(m1, m2, m3):
    total = m1 + m2 + m3
    gpa = round(total / 30, 2)

    if gpa >= 9: grade = "A"
    elif gpa >= 8: grade = "B"
    elif gpa >= 6: grade = "C"
    elif gpa >= 5: grade = "D"
    else: grade = "F"

    return total, gpa, grade

# ================= CRUD =================
def student_exists(sid):
    cur.execute("SELECT id FROM students WHERE id=?", (sid,))
    return cur.fetchone() is not None

def add_student():
    sid = safe_int("Student ID: ", 1)
    if student_exists(sid):
        print("❌ Student ID already exists")
        return

    name = input("Name: ")
    m1 = safe_int("Marks 1 (0-100): ", 0, 100)
    m2 = safe_int("Marks 2 (0-100): ", 0, 100)
    m3 = safe_int("Marks 3 (0-100): ", 0, 100)

    total, gpa, grade = calculate(m1, m2, m3)

    cur.execute(
        "INSERT INTO students VALUES (?,?,?,?,?,?,?,?)",
        (sid, name, m1, m2, m3, total, gpa, grade)
    )
    conn.commit()
    print("✔ Student added")

def view_students():
    cur.execute("SELECT * FROM students ORDER BY total DESC")
    rows = cur.fetchall()
    print("\nID Name Total GPA Grade Rank")
    for i, r in enumerate(rows, 1):
        print(r[0], r[1], r[5], r[6], r[7], i)

def update_marks():
    sid = safe_int("Student ID to update: ", 1)
    if not student_exists(sid):
        print("❌ Student not found")
        return

    m1 = safe_int("New Marks 1: ", 0, 100)
    m2 = safe_int("New Marks 2: ", 0, 100)
    m3 = safe_int("New Marks 3: ", 0, 100)

    total, gpa, grade = calculate(m1, m2, m3)

    cur.execute("""
        UPDATE students SET m1=?, m2=?, m3=?, total=?, gpa=?, grade=?
        WHERE id=?
    """, (m1, m2, m3, total, gpa, grade, sid))
    conn.commit()
    print("✔ Marks updated")

def delete_student():
    sid = safe_int("Student ID to delete: ", 1)
    if not student_exists(sid):
        print("❌ Student not found")
        return

    cur.execute("DELETE FROM students WHERE id=?", (sid,))
    conn.commit()
    print("✔ Student deleted")

def export_csv():
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    with open("results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID","Name","M1","M2","M3","Total","GPA","Grade"])
        writer.writerows(rows)
    print("📁 results.csv exported")

# ================= STUDENT VIEW =================
def student_view():
    sid = safe_int("Enter your Student ID: ", 1)
    cur.execute("SELECT * FROM students WHERE id=?", (sid,))
    r = cur.fetchone()

    if not r:
        print("❌ Record not found")
        return

    print("\n--- YOUR RESULT ---")
    print("Name:", r[1])
    print("Marks:", r[2], r[3], r[4])
    print("Total:", r[5])
    print("GPA:", r[6])
    print("Grade:", r[7])

# ================= MENUS =================
def admin_menu():
    while True:
        print("\n1.Add 2.View 3.Update 4.Delete 5.Export CSV 6.Exit")
        ch = input("Choice: ")

        if ch == "1": add_student()
        elif ch == "2": view_students()
        elif ch == "3": update_marks()
        elif ch == "4": delete_student()
        elif ch == "5": export_csv()
        elif ch == "6": break
        else: print("⚠️ Invalid option")

# ================= MAIN =================
if __name__ == "__main__":
    while True:
        print("\n=== STUDENT RESULT MANAGEMENT SYSTEM ===")
        print("1.Admin Login")
        print("2.Student Login")
        print("3.Exit")

        choice = input("Select option: ")

        if choice == "1":
            if admin_login():
                admin_menu()
            else:
                print("❌ Invalid admin credentials")
        elif choice == "2":
            student_view()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("⚠️ Invalid choice")
