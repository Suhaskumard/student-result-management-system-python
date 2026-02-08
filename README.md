🎓 Student Result Management System (Python + SQLite)

📌 Overview
The **Student Result Management System** is a console-based backend application developed using **Python and SQLite**.  
It allows administrators to manage student academic records and enables students to securely view their own results.

The system focuses on **database-driven design, input validation, and real-world academic workflows**.

 🎯 Objectives
- Store and manage student results using a database
- Calculate total marks, GPA, grades, and rank automatically
- Provide role-based access for Admin and Students
- Prevent invalid inputs and system crashes
- Export academic data for reporting


 🧠 Features

 🔐 Admin Module
- Admin login authentication
- Add new student records
- Update student marks
- Delete student records
- View all students with rank list
- Export results to CSV

 👨‍🎓 Student Module
- Student login using Student ID
- View individual result (marks, total, GPA, grade)
- Read-only access (secure)

 📊 Result Processing
- Automatic total calculation
- GPA calculation
- Grade assignment (A / B / C / D / F)
- Rank generation based on total marks

 💾 Database & Safety
- SQLite database (`results.db`)
- Persistent data storage
- Duplicate Student ID prevention
- Full input validation with re-prompting
- No crashes on invalid input


 🛠️ Tech Stack
- Language:Python
- Database:SQLite

  
  Concepts Used:
  - SQL (CRUD operations)
  - Defensive programming
  - Input validation
  - Backend logic
  - File handling (CSV export)


 📁 Project Structure

student-result-management-system-python/
│
├── student_result_system.py
├── results.db # Auto-generated
├── results.csv # Generated on export
└── README.md

🔐 Login Credentials
Admin
Username: admin
Password: admin123

Student
Login using valid Student ID

🧪 Tested Scenarios

Invalid menu input handling
Invalid marks and ID validation
Duplicate student ID protection
Empty database access
Correct GPA, grade, and rank generation
CSV export verification

🎓 Academic Relevance
This project demonstrates:
Practical application of DBMS concepts
Strong Python backend logic
Clean role-based system design
Real-world academic result processing

✔ Suitable for:
CSE Mini Projects
DBMS / Python coursework
Backend development practice
GitHub portfolio and resume projects

🔮 Future Enhancements
Student password-based login
Web version using Flask
Java + JDBC implementation
Graphical reports and analytics
Subject-wise grading

📜 License
This project is intended for academic and learning purposes only.
