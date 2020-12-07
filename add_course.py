import tkinter as tk
from grade import Grade

class AddCourse(tk.Toplevel):
    def __init__(self, parent):
        super(AddCourse, self).__init__(parent)
        self.parent = parent
        self.title("Add Course")
        self.resizable(False, False)
        self.geometry('+%d+%d' % (self.parent.winfo_x()+175, self.parent.winfo_y()+200))
        self.course_categories = [
                            'ELA',
                            'Math',
                            'Social Studies',
                            'Science',
                            'LOTE',
                            'Technology',
                            'AP CSP'
                        ]
        self.create_window()
    
    def create_window(self):
        """Creates and adds all elements to the window"""
        self.course_name_var = tk.StringVar(self)
        self.course_score_var = tk.StringVar(self)
        self.course_category_var = tk.StringVar(self)

        self.course_name_var.trace("w", self.filled)
        self.course_score_var.trace("w", self.filled)
        self.course_category_var.trace("w", self.filled)

        self.course_name_label = tk.Label(self, text='Course Name').grid(row=0, column=0)
        self.course_name_entry = tk.Entry(self, textvariable=self.course_name_var).grid(row=0, column=1)
        self.course_score_label = tk.Label(self, text='Course Score').grid(row=1, column=0)
        self.course_score_entry = tk.Entry(self, textvariable=self.course_score_var).grid(row=1, column=1)
        self.course_category_label = tk.Label(self, text='Course Category').grid(row=2, column=0)
        self.course_category_option = tk.OptionMenu(self, self.course_category_var, *self.course_categories).grid(row=2, column=1)
        self.course_is_weighted = tk.IntVar()
        self.course_honors = tk.Checkbutton(self, text='Honors', onvalue= 1, variable=self.course_is_weighted).grid(row=3, column=0)
        self.course_ap = tk.Checkbutton(self, text='AP', onvalue=2, variable=self.course_is_weighted).grid(row=3, column=1)

        self.button = tk.Button(self, text='Add Grade', command=self.add_course)
        self.button.config(state='disabled')
        self.button.grid(row=4, column=1, sticky='nesw')
    
    def add_course(self):
        """Adds a course"""
        course_name = self.course_name_var.get()
        course_score = self.course_score_var.get()
        course_weight = self.course_is_weighted.get()
        course_category = self.course_category_var.get()
        grade = Grade(course_name, int(course_score), course_category, course_weight)
        grade.add_database()
        self.destroy()
        self.parent.frame.destroy()
        self.parent.display_grades()
    
    def filled(self, *args):
        """Validates user input"""
        name = self.course_name_var.get()
        score = self.course_score_var.get()
        category = self.course_category_var.get()
        if name and score and category:
            if score.isnumeric():
                self.button.config(state='normal')
        else:
            self.button.config(state='disabled')