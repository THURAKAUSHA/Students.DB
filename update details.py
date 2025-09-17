import sqlite3 as sql

con = sql.connect('students.db')
cur = con.cursor()

student_id = int(input("Enter student ID: "))
subject = input("Enter subject (marks1/marks2/marks3): ")
new_mark = int(input("Enter new mark: "))

# Update subject mark
q = f"UPDATE Students SET {subject} = ? WHERE student_id = ?"
cur.execute(q, (new_mark, student_id))

# Fetch updated marks
q = "SELECT marks1, marks2, marks3 FROM Students WHERE student_id = ?"
cur.execute(q, (student_id,))
data = cur.fetchone()

if data:
    m1, m2, m3 = data
    gpa = round((m1 + m2 + m3) / 3, 2)

    # Update GPA
    q = "UPDATE Students SET gpa = ? WHERE student_id = ?"
    cur.execute(q, (gpa, student_id))
    print("Marks and GPA updated successfully!")
else:
    print("❌ No student found with that ID.")

con.commit()
con.close()



