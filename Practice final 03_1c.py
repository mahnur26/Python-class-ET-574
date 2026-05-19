"""1c. Instantiate objects of the ETStudent class by calling the class with your own name and id:987654. 

      Then print the return values. Paste your code in the space below.

Example Output:

Name: John Smith

Id: QCC-ET-987654"""
# Create a class named ETStudent
class ETStudent:

    # Constructor method
    def __init__(self, name, student_id ):
        self.name = name
        self.student_id = student_id

    # Method to display student information
    def Student_display(self):
        print("Name:", self.name)
        print("Id: QCC-ET-" + str(self.student_id))


# Instantiate an object of ETStudent
student1 = ETStudent("John Smith", 987654)

# Print the values
student1.Student_display()