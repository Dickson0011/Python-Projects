import tkinter as tk

class CGPACalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("CGPA Calculator")

        self.cumulative_gpa = 0.0
        self.semester_count = 0

        self.create_widgets()

    def create_widgets(self):
        self.label_subjects = tk.Label(self.root, text="Note: Grades are A, B, C, D, E, and F")
        self.label_subjects.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.label_subjects = tk.Label(self.root, text="Number of Subjects:")
        self.label_subjects.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.entry_subjects = tk.Entry(self.root)
        self.entry_subjects.grid(row=0, column=3, columnspan=3, padx=10, pady=10)

        self.label_subject_names = tk.Label(self.root, text="Course code:")
        self.label_subject_names.grid(row=2, column=0, padx=10, pady=10)

        self.label_course_unit = tk.Label(self.root, text="Course_unit:")
        self.label_course_unit.grid(row=2, column=1, padx=10, pady=10)

        self.label_grades = tk.Label(self.root, text="Grades:")
        self.label_grades.grid(row=2, column=2, padx=10, pady=10)

        self.entry_subject_names = [tk.Entry(self.root) for _ in range(10)]
        self.entry_course_unit = [tk.Entry(self.root) for _ in range(10)]
        self.entry_grades = [tk.Entry(self.root) for _ in range(10)]

        for i in range(10):
            self.entry_subject_names[i].grid(row=i + 3, column=0, padx=10, pady=5)
            self.entry_course_unit[i].grid(row=i + 3, column=1, padx=10, pady=5)
            self.entry_grades[i].grid(row=i + 3, column=2, padx=10, pady=5)

        self.calculate_button = tk.Button(self.root, text="Calculate GPA", command=self.calculate_gpa)
        self.calculate_button.grid(row=13, column=0, columnspan=3, pady=10)

        self.calculate_cgpa_button = tk.Button(self.root, text="Calculate CGPA", command=self.calculate_cgpa)
        self.calculate_cgpa_button.grid(row=14, column=0, columnspan=3, pady=10)

        self.add_semester_button = tk.Button(self.root, text=f"Add New Semester ({self.semester_count + 1})", command=self.add_semester)
        self.add_semester_button.grid(row=15, column=0, columnspan=3, pady=10)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=16, column=0, columnspan=3, pady=10)

    def calculate_gpa(self):
        total_subjects = int(self.entry_subjects.get())
        total_points = 0

        for i in range(total_subjects):
            course_unit = float(self.entry_course_unit[i].get())
            score = self.entry_grades[i].get()

            grade_points = {"A": 5.0, "B": 4.0, "C": 3.0, "D": 2.0, "E": 1.0, "F": 0.0}
            grade_point = grade_points.get(score, 0.0)

            total_points += grade_point * course_unit

        gpa = total_points / sum([float(self.entry_course_unit[i].get()) for i in range(total_subjects)])
        self.result_label.config(text=f"Your GPA is: {gpa:.2f}")

    def calculate_cgpa(self):
        current_gpa = float(self.result_label.cget("text").split(":")[-1])
        self.semester_count += 1
        self.cumulative_gpa = ((self.cumulative_gpa * (self.semester_count - 1)) + current_gpa) / self.semester_count

        self.result_label.config(text=f"Your CGPA is: {self.cumulative_gpa:.2f}")

    def add_semester(self):
        self.calculate_gpa()

        # Destroy all widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        self.create_widgets()

if __name__ == "__main__":
    root = tk.Tk()
    app = CGPACalculator(root)
    root.mainloop()
