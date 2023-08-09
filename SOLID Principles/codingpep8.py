""" Create a Python program that manages student records. The program should have the
following functionalities:
- Create a function that can add new students to the records with their student_id, name, age, and grade. 
    The records should be saved to “json” file and each time new record is added, it should be saved to same “json” file
- Allow searching for a student by student_id or name. The data should return age and grade from the saved file.
- Allow updating a student's information by using student_id or name(age or grade)

Ensure to follow PEP8 Coding Guidelines for following criterias:
- Proper Indentation
- Maximum Line Length
- Prescriptive Naming conventions (Package and Module Names, Class Names, Exception Names, Global Variable Names, 
    Function and Variable Names, Method Names and Instance Variables, Constants)
- Source File Encoding while accessing the JSON file
- Add NumPy Docstring to each function. """

import json

class StudentManager:
    """
    A class to manage student records.

    Attributes:
        records (list): List to store student records.

    Methods:
        add_student(student_id, name, age, grade): Add a new student record.
        search_student(identifier): Search for a student by student_id or name.
        update_student(identifier, key, value): Update student's information by student_id or name.
    """
    def __init__(self, file_name):
        """
        Initialize the StudentManager with the specified JSON file.

        Args:
            file_name (str): Name of the JSON file to save records.
        """
        self.file_name = file_name
        self.records = self._load_records()

    def _load_records(self):
        try:
            with open(self.file_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _save_records(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.records, file)

    def add_student(self, student_id, name, age, grade):
        """
        Add a new student record.

        Args:
            student_id (int): Student's ID.
            name (str): Student's name.
            age (int): Student's age.
            grade (str): Student's grade.

        Returns:
            None
        """
        student = {
            'student_id': student_id,
            'name': name,
            'age': age,
            'grade': grade
        }
        self.records.append(student)
        self._save_records()

    def search_student(self, identifier):
        """
        Search for a student by student_id or name.

        Args:
            identifier (int or str): Student's ID or name.

        Returns:
            dict or None: Student's record (including age and grade) if found, otherwise None.
        """
        for student in self.records:
            if student['student_id'] == identifier or student['name'] == identifier:
                return {'age': student['age'], 'grade': student['grade']}
        return None

    def update_student(self, identifier, key, value):
        """
        Update a student's information by student_id or name.

        Args:
            identifier (int or str): Student's ID or name.
            key (str): Attribute to update ('age' or 'grade').
            value: New value for the specified attribute.

        Returns:
            bool: True if the student's information was updated, False if not found.
        """
        for student in self.records:
            if student['student_id'] == identifier or student['name'] == identifier:
                student[key] = value
                self._save_records()
                return True
        return False

if __name__ == "__main__":
    manager = StudentManager('student_records.json')

    manager.add_student(1, 'Alice', 20, 'A')
    manager.add_student(2, 'Bob', 21, 'B')
    manager.add_student(3, 'Charlie', 19, 'C')

    student_info = manager.search_student(2)
    if student_info:
        print(f"Student ID: {student_info['student_id']}, Name: {student_info['name']}, Age: {student_info['age']}, Grade: {student_info['grade']}")
    else:
        print("Record not found.")

    updated = manager.update_student('Bob', 'age', 22)
    if updated:
        print("Updated successfully.")
    else:
        print("Record not found.")

