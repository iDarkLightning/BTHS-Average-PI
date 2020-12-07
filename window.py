import tkinter as tk
import tkinter.ttk
from grade import Grade
from add_course import AddCourse
from edit_course import EditCourse
from calculate_average import CalculateAverage
from power_index import PowerIndex

HEIGHT = 600
WIDTH = 600

class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.title("Average and PI Calculator")
        self.create_window()
        self.geometry(str(WIDTH) + "x" + str(HEIGHT))
        self.resizable(False, False)
        self.display_grades()

    def create_window(self):
        """Creates and adds all the elements in the pain window"""
        self.canvas_main = tk.Canvas(self, height=HEIGHT, width=WIDTH, bg='#989898')
        self.canvas_main.pack()

        add_course_button = tk.Button(self.canvas_main, text='Add a Course', command=lambda: AddCourse(self))
        add_course_button.place(x=500, y=15)

        calculate_average_button = tk.Button(self.canvas_main, text='Calculate Average', command=lambda: CalculateAverage(self))
        calculate_average_button.place(x=487, y=40)

        calculate_power_index_button = tk.Button(self.canvas_main, text='Calculate PI', command=lambda: PowerIndex(self))
        calculate_power_index_button.place(x=500, y=65)

    def display_grades(self):
        """Displays all the current instances of the Grade class"""
        self.frame = tk.Frame(self)
        self.frame.place(relheight=1.0, relwidth=0.8)
        self.frame.grid_columnconfigure((0), weight=8)
        self.frame.grid_columnconfigure(1, weight=1)

        row = 1
        #Loops over the grades and displays the name and the score
        for grade in Grade.instances:
            grade_name = tk.Button(self.frame, text=grade.name, font=('Times New Roman', 18), 
                                    borderwidth=2.5, relief='raise', command=lambda grade=grade: EditCourse(self, grade))
            grade_name.grid(row=row, column=0, sticky='nsew')
            grade_score = tk.Label(self.frame, text=grade.score, font=('Times New Roman', 18), 
                                    borderwidth=2.5, relief='raise', bg=self.get_color(grade))
            grade_score.grid(row=row, column=1, sticky='nesw')
            row += 1
    
    def get_color(self, grade):
        """Categorizes a grade by color based on the value"""
        if grade.score < 65:
            color = '#e64847'
        elif 65 < grade.score < 90:
            color = '#85fa89'
        elif grade.score > 90:
            color = '#81d4fa'
        return color