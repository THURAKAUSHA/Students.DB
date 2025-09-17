import sqlite3 as sql
name = input("Enter student name: ")
branch = input("Enter branch: ")
marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))
marks3 = int(input("Enter marks for subject 3: "))
gpa = (marks1 + marks2 + marks3) / 3
conn = sql.connect("students.db")
cursor = conn.cursor()
cursor.execute("INSERT INTO Students (name, branch, marks1, marks2, marks3, gpa) VALUES (?, ?, ?, ?, ?, ?)",
                   (name, branch, marks1, marks2, marks3, gpa))
conn.commit()
conn.close()
print("✅ Student added successfully!\n")

