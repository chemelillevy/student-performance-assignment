import csv
from abc import ABC, abstractmethod

# ==========================================
# Task 2: Student base class & Encapsulation
# ==========================================
class Student(ABC):
    def __init__(self, student_id, fname, lname, programme, marks):
        self._student_id = student_id
        self._fname = fname
        self._lname = lname
        self._programme = programme
        self._set_marks(marks) # Validates marks during initialization

    # Encapsulation: Exposing data through properties
    @property
    def full_name(self):
        return f"{self._fname} {self._lname}"

    @property
    def student_id(self):
        return self._student_id
    
    @property
    def programme(self):
        return self._programme

    @property
    def marks(self):
        return self._marks

    def _set_marks(self, marks):
        for subject, score in marks.items():
            if not isinstance(score, (int, float)) or not 0 <= score <= 100:
                raise ValueError(f"Invalid mark for {subject}: {score}. Must be 0-100.")
        self._marks = dict(marks)

    # Task 6: Flexible interface in place of overloading
    @staticmethod
    def calculate_average(*marks):
        """Calculates average from a variable number of marks."""
        if not marks:
            raise ValueError("At least one mark is required")
        for m in marks:
            if not isinstance(m, (int, float)) or not 0 <= m <= 100:
                raise ValueError(f"Invalid mark: {m}")
        return sum(marks) / len(marks)

    def average(self):
        # Uses the flexible interface to calculate the average of this student's marks
        return self.calculate_average(*self._marks.values())

    def grade(self):
        avg = self.average()
        if avg >= 80: return 'A'
        elif avg >= 70: return 'B'
        elif avg >= 60: return 'C'
        elif avg >= 50: return 'D'
        else: return 'F'

    # Task 7: Base report generation
    def generate_report(self):
        report = (f"ID: {self.student_id} | Name: {self.full_name} | Programme: {self.programme}\n"
                  f"Marks: {self.marks}\n"
                  f"Average: {self.average():.2f} | Grade: {self.grade()}")
        return report

    @abstractmethod
    def describe(self):
        pass

class AIUStudent(Student):
    def describe(self):
        return f"{self.full_name} is a regular AIU student."

# ==========================================
# Task 4: Inheritance and Overriding
# ==========================================
class ScholarshipStudent(AIUStudent):
    def __init__(self, student_id, fname, lname, programme, marks, scholarship_amount=50000):
        # Using super() to call the parent class constructor
        super().__init__(student_id, fname, lname, programme, marks)
        self.scholarship_amount = scholarship_amount

    def is_eligible(self):
        return self.average() >= 85

    # Overriding the describe method for polymorphism
    def describe(self):
        return f"{self.full_name} is a Scholarship student (Award: KES {self.scholarship_amount})."

    # Task 7: Overriding report generation to add eligibility
    def generate_report(self):
        base_report = super().generate_report()
        eligibility = "Yes" if self.is_eligible() else "No"
        return f"{base_report}\nScholarship Eligible: {eligibility}"


# ==========================================
# Task 3: Performance Analyzer & Composition
# ==========================================
class PerformanceAnalyzer:
    def __init__(self, students):
        # Stores a collection of Student objects (Composition)
        self._students = students

    def highest_average(self):
        if not self._students: return None
        return max(self._students, key=lambda s: s.average())

    def lowest_average(self):
        if not self._students: return None
        return min(self._students, key=lambda s: s.average())

    def class_average(self):
        if not self._students: return 0
        return sum(s.average() for s in self._students) / len(self._students)

    def generate_class_report(self):
        highest = self.highest_average()
        lowest = self.lowest_average()
        avg = self.class_average()
        
        report = "\n--- CLASS PERFORMANCE SUMMARY ---\n"
        if highest:
            report += f"Highest Average: {highest.full_name} ({highest.average():.2f})\n"
            report += f"Lowest Average: {lowest.full_name} ({lowest.average():.2f})\n"
            report += f"Overall Class Average: {avg:.2f}\n"
        return report


# ==========================================
# Main Execution: Loading CSV & Testing
# ==========================================
if __name__ == "__main__":
    students_list = []

    # 1. Load data from CSV
    try:
        with open("students.csv", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Extract marks
                marks = {
                    "Math": int(row["Math"]), 
                    "English": int(row["English"]), 
                    "Science": int(row["Science"])
                }
                
                # Calculate temporary average to decide object type
                temp_avg = sum(marks.values()) / len(marks)
                
                # Create ScholarshipStudent if average >= 85, else AIUStudent
                if temp_avg >= 85:
                    student = ScholarshipStudent(row["StudentID"], row["FName"], row["LName"], row["Programme"], marks)
                else:
                    student = AIUStudent(row["StudentID"], row["FName"], row["LName"], row["Programme"], marks)
                
                students_list.append(student)
                
    except FileNotFoundError:
        print("Error: students.csv not found. Please ensure it is in the same directory.")
        exit()

    # 2. Task 5: Demonstrate Polymorphism
    print("--- POLYMORPHISM DEMONSTRATION ---")
    for s in students_list:
        # Calls the appropriate describe() method based on the object's actual class at runtime
        print(s.describe())
    
    print("\n--- INDIVIDUAL STUDENT REPORTS ---")
    for s in students_list:
        print(s.generate_report())
        print("-" * 30)

    # 3. Analyze Performance (Task 3 & 7)
    analyzer = PerformanceAnalyzer(students_list)
    print(analyzer.generate_class_report())