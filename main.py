import sqlite3
from grade import Grade
from window import MainWindow

conn = sqlite3.connect('courses.db')
cursor = conn.cursor()

#Creates an sqlite table, if it doesn't already exist
with conn:
    cursor.execute('''
			CREATE TABLE IF NOT EXISTS courses
			(
				name text, 
				score integer,
				category text,
				weight integer,
				UNIQUE(name, score, category, weight)
			)''')

def load_grades():
    """Creates a new instance of the grade class for every row in the table"""
    try:
        with conn:
            cursor.execute('SELECT * FROM courses')
        courses = cursor.fetchall()
        for course in courses:
            Grade(course[0], course[1], course[2], course[3])
    except sqlite3.OperationalError:
        pass
    return 

#Loads grades and starts the program
if __name__ == '__main__':
    load_grades()
    window = MainWindow()
    window.mainloop()