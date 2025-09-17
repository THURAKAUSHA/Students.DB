import sqlite3 as sql

# Connect to database
con = sql.connect('students.db')
cur = con.cursor()

# Prepare query
q = 'SELECT gpa FROM students WHERE name = ?'
name = input('Enter the student name: ')
t1 = (name,)

# Execute using cursor (not connection)
cur.execute(q, t1)

# Fetch the result
data = cur.fetchone()

# Check if student exists
if data:
    gpa = data[0]  # data is a tuple like (gpa,)
    if gpa >= 60:
        print('pass')
    else:
        print('fail')
else:
    print('Invalid name')

# Close connection
con.close()
