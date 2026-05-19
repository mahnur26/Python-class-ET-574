"""b. Create the Student_display() method to print instance variables:  name and id.

with prefix = 'QCC-ET-' 

Paste your code for this method below."""
def Student_display(self): #Creating the Student_display() method
    print("Name:", self.name)
    print("Id: QCC-ET-" + str(self.student_id))