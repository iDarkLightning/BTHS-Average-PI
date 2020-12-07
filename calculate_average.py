import tkinter as tk
from grade import Grade

class CalculateAverage(tk.Toplevel):
    def __init__(self, parent):
        super(CalculateAverage, self).__init__(parent)
        self.parent = parent
        self.title("Calculate Average")
        self.resizable(False, False)
        self.geometry('+%d+%d' % (self.parent.winfo_x()+175, self.parent.winfo_y()+200))
        self.course_categories = [
                            'All',
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
        """Creates and adds all element to the window"""
        self.course_category_var = tk.StringVar(self)
        self.course_category_var.set(self.course_categories[0])

        self.course_category_label = tk.Label(self, text='Average Category' ).grid(row=0, column=0, sticky='w')
        self.course_category_option = tk.OptionMenu(self, self.course_category_var, *self.course_categories).grid(row=0, column=1, sticky='e')
        self.submit_button = tk.Button(self, text='Calculate Average', command=self.get_courses).grid(row=1, column=1, sticky='e')

    def get_courses(self):
        """Gets all the courses in the selected category"""
        self.category = self.course_category_var.get()

        if self.category != 'All':
            courses = list(filter(lambda x: x.category == self.category, Grade.instances))
        else:
            courses = Grade.instances

        if len(self.winfo_children()) < 4:
            average = tk.Label(self)
            self.calculate_average(courses, average)
        else:
            average = self.winfo_children()[3]
            self.calculate_average(courses, average)
    
    def calculate_average(self, courses, average_label):
        """Calculates and displays the average for the given category"""
        if len(courses) == 0:
            average_label.config(text='You do not have any courses in that category', fg='red')
        else:
            average_label.config(text=f'Your average is {round((sum([grade.weighted_score for grade in courses])/len(courses)), 2)}', fg='black')
        average_label.grid(row=1, column=0, sticky='w')