import tkinter as tk
from grade import Grade

class PowerIndex(tk.Toplevel):
    def __init__(self, parent):
        super(PowerIndex, self).__init__(parent)
        self.title("Calculate Power Index")
        self.parent = parent
        self.geometry('+%d+%d' % (self.parent.winfo_x() + 175, self.parent.winfo_y() + 200))
        self.power_index = {
            'Aerospace Engineering': ['Average', 'Math', 'Science', 'Technology', 'AP CSP'],
            'Applied Mathematics': ['Average', 'Math', 'Math'],
            'Architectural Engineering': ['Average', 'Math', 'Technology', 'Technology'],
            'Biological Sciences': ['Average', 'Science', 'Science'],
            'Chemical Engineering': ['Average', 'Math', 'Science', 'Science'],
            'Civil Engineering': ['Average', 'Math', 'Science', 'Technology'],
            'Electrical Engineering': ['Average', 'Math', 'Technology', 'AP CSP'],
            'Environmental Science': ['Average', 'Science', 'Science'],
            'Finance': ['Average', 'Math', 'Social Studies'],
            'Industrial Design': ['Average', 'Technology', 'Technology'],
            'Law & Society': ['Average', 'Social Studies', 'Social Studies', 'English'],
            'LIU PharmD': ['Average', 'English', 'Social Studies', 'Science', 'Science', 'Math', 'Math'],
            'LIU Advanced Health Professions': ['Average', 'English', 'Social Studies', 'Science', 'Science', 'Math'],
            'Mechatronics & Robotics': ['Average', 'Math', 'Technology', 'AP CSP'],
            'Media Communications': ['Average', 'Technology', 'Technology'],
            'Physics': ['Average', 'Science', 'Math', 'Math'],
            'Social Science Research': ['Average', 'Social Studies', 'Social Studies', 'English'],
            'Software Engineering': ['Average', 'Math', 'AP CSP', 'English']
        }
        self.create_window()
    
    def create_window(self):
        """Creates and adds all the elements in the window"""
        self.major_var = tk.StringVar(self)
        self.major_label = tk.Label(self, text='Major Category').grid(row=0, column=0, sticky='w')
        self.major_option = tk.OptionMenu(self, self.major_var, *[i for i, _ in self.power_index.items()]).grid(row=0, column=1, sticky='e')
        """Calls the calculate_power_index function and displays result"""
        self.submit_button = tk.Button(self, text='Calculate Power Index', 
                                        command= lambda: self.calculate_power_index(major=self.major_var.get())).grid(row=1, column=1, sticky='e')
    
    def calculate_power_index(self, major):
        """Calculates the power index for the given major"""
        major_formula = self.power_index[major]
        average_list = []

        try:
            for category in major_formula:
                if category == 'Average':
                    average_list.append((sum(grade.weighted_score for grade in Grade.instances)/len(Grade.instances)))
                else:
                    courses_in_category = list(filter(lambda x: x.category == category, Grade.instances))
                    average_list.append(sum(grade.score for grade in courses_in_category)/len(courses_in_category))
            self.display_power_index(power_index=f'Your power index is {sum(average_list)}')
        except ZeroDivisionError:
            self.display_power_index(power_index='You do not have the required courses for this major')    
            
    def display_power_index(self, power_index):
        """Displays the given message for the power index"""
        if len(self.winfo_children()) < 4:
            power_index_label = tk.Label(self, text=power_index).grid(row=1, column=0)
        else:
            power_index_label = self.winfo_children()[3]
            power_index_label.config(text=power_index)