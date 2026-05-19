"""Use Python code to accomplish the following; include comments.

Create a class ETStudent which is used to create instances (objects)
  of type ETStudent. 

  Use the  __init__() method to assign default values for student name and id

Paste the code in the area provided here"""
class ETStudent:
    def __init__(self, name="John", student_id="000000"): #by Using the  __init__() method
        self.name = name
        self.student_id = student_id