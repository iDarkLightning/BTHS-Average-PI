import tkinter as tk
import sqlite3
from grade import Grade

class EditCourse(tk.Toplevel):
    def __init__(self, parent, grade):
        super(EditCourse, self).__init__(parent)
        self.parent = parent
        self.title("Edit Course")
        self.resizable(False, False)
        self.geometry('+%d+%d' % (self.parent.winfo_x()+175, self.parent.winfo_y()+200))
        self.grade = grade
        self.course_categories = [
                            'ELA',
                            'Math',
                            'Social Studies',
                            'Science',
                            'LOTE',
                            'Technology',
                            'AP CSP'
                        ]
        self.conn = sqlite3.connect('courses.db')
        self.cursor = self.conn.cursor()
        self.create_window()
    
    def create_window(self):
        """Creates and adds all elements to the window"""
        self.info = tk.Label(self, text=f'{(self.grade.name).capitalize()} Course Information', font=('Helvetica 18 bold', 12)).grid(row=0, column=0, padx=30)
        self.info_name = tk.Label(self, text=f'Course Category: {self.grade.category.capitalize()}', font=('Helvetica 18 bold', 12)).grid(row=1, column=0)
        self.info_score = tk.Label(self, text=f'Course Score: {self.grade.score}', font=('Helvetica 18 bold', 12)).grid(row=2, column=0)
        self.info_level = tk.Label(self, text=f'Course Level: {self.grade.level}', font=('Helvetica 18 bold', 12)).grid(row=3, column=0)
        self.info_weighted_score = tk.Label(self, text=f'Course Weighted Score: {self.grade.weighted_score}', font=('Helvetica 18 bold', 12)).grid(row=4, column=0)
        tk.Button(self, text='Delete Course', command=self.delete_course).grid(row=5, column=0, sticky='nesw')
        tk.Button(self, text='Edit Course', command=self.edit_course).grid(row=6, column=0, sticky='nesw')

    def delete_course(self):
        """Deletes a course"""
        Grade.instances.remove(self.grade)
        self.destroy()
        with self.conn:
            self.cursor.execute('DELETE FROM courses WHERE name= ?', (self.grade.name,))
        self.parent.frame.destroy()
        self.parent.display_grades()
    
    def edit_course(self):
        """Edits a course"""
        for element in self.winfo_children():
            element.destroy()
                
        self.edit_name_val = tk.StringVar(self, value=self.grade.name)
        self.edit_score_val = tk.StringVar(self, value=self.grade.score)
        self.edit_category_val = tk.StringVar(self, value=self.grade.category)

        self.edit_name_val.trace('w', self.filled)
        self.edit_score_val.trace('w', self.filled)
        self.edit_category_val.trace('w', self.filled)

        self.edit_name_label = tk.Label(self, text='Edit Name').grid(row=0, column=0)
        self.edit_name_entry = tk.Entry(self, textvariable=self.edit_name_val).grid(row=0, column=1)
        self.edit_score_label = tk.Label(self, text='Edit Score').grid(row=1, column=0)
        self.edit_score_entry = tk.Entry(self, textvariable=self.edit_score_val).grid(row=1, column=1)
        self.edit_score_label = tk.Label(self, text='Edit Category').grid(row=2, column=0)
        self.edit_score_entry = tk.OptionMenu(self, self.edit_category_val, *self.course_categories).grid(row=2, column=1)

        if self.grade.level.lower() == 'honors':
            check_val = 1
        elif self.grade.level.lower() == 'ap':
            check_val = 2
        else:
            check_val = 0
        
        self.course_is_weighted = tk.IntVar(value=check_val)
        self.course_honors = tk.Checkbutton(self, text='Honors', onvalue= 1, variable=self.course_is_weighted).grid(row=3, column=0)
        self.course_ap = tk.Checkbutton(self, text='AP', onvalue=2, variable=self.course_is_weighted).grid(row=3, column=1)

        self.button = tk.Button(self, text='Save Changes', command=self.save_changes)
        self.button.grid(row=4, column=0, sticky='nesw')

    def filled(self, *args):
        """Validates user input"""
        name = self.edit_name_val.get()
        score = self.edit_score_val.get()
        category = self.edit_category_val.get()
        if name and score and category:
            if score.isnumeric():
                self.button.config(state='normal')
        else:
            self.button.config(state='disabled')
    
    def save_changes(self):
        """Saves the changes from editing"""
        with self.conn:
            self.cursor.execute('DELETE FROM courses WHERE name= ? and score=?', (self.grade.name,self.grade.score))
        Grade.instances.remove(self.grade)
        grade = Grade(self.edit_name_val.get(), int(self.edit_score_val.get()), self.edit_category_val.get(), self.course_is_weighted.get())
        # self.grade.name = self.edit_name_val.get()
        # self.grade.score = int(self.edit_score_val.get())
        # self.grade.category = self.edit_category_val.get()
        # self.grade.weighted(self.course_is_weighted.get())
        grade.add_database()
        self.destroy()
        self.parent.frame.destroy()
        self.parent.display_grades()