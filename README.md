# Student Performance Analysis System

## Overview
The Student Performance Analysis System is a Python-based Object-Oriented Programming (OOP) project. It loads student records from a CSV dataset, calculates academic averages, assigns grades, determines scholarship eligibility, and generates comprehensive class performance reports.

## OOP Concepts Demonstrated
* **Encapsulation:** Protecting student attributes (e.g., `_marks`) and exposing them via `@property` decorators with validation.
* **Abstraction:** Utilizing the `abc` module to create an abstract `Student` base class that mandates subclasses to implement the `describe()` method.
* **Composition:** Designing a `PerformanceAnalyzer` class that aggregates a collection of student objects to calculate class-wide metrics.
* **Inheritance:** Extending the base `Student` class into `AIUStudent`, and further extending it into `ScholarshipStudent`.
* **Polymorphism & Method Overriding:** Executing class-specific behaviors uniformly through shared method names.

## How to Run
1. Ensure Python 3.x is installed on your system.
2. Verify that `students.csv` and `main.py` are located in the same directory.
3. Execute the script from the terminal:
   ```bash
   python main.py