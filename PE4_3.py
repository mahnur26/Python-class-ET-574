''' 3. Write the codes and precisely produce the output format below.
a) Create a list called courses containing the names of your current courses.
b) Print the list of courses.
c) Use the len method to print “I am taking X courses” where X is the number of courses in the list.
d) Using indexes to print the first and last item from the list.
e) Using slicing to print the first four classes.
f) Using slicing to print the last four classes.
g) Using slicing to print the classes except for the first and last classes. '''
#a)
courses = ["math", "Eng", "python", "SOC","PSY"]
#b
print(courses)
#c
print(f"I am taking {len(courses)} courses")
#d
first = courses[0]
last = courses[len(courses) - 1]
print(first, last)
#e
print(courses[:4])
#f
print(courses[1:])
#g
print(courses[1:4])