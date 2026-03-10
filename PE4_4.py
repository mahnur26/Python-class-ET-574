''' Create/Make PE4_4.py to do the following:
a) Create an empty list named grades.
b) Add any five grades one at a time to grades.
c) Print the current list.
d) Compute the total of these grades using the indexing to reference each number in grades.
e) Compute the average of these grades using the len () function.
f) Print the average with a precision of two decimal places.
g) Use two different methods to remove all failing grades (lower than 60) one at a time from the list.
h) Print the updated list.
i) Use the built-in functions, sum () and len () to compute the average with three decimal places and print
the updated result in one statement '''
#a
grades = []
#b
grades.append(92)
grades.append(51)
grades.append(83)
grades.append(37)
grades.append(72)
#c
print("current grades", grades)
#d
total = grades[1] + grades[2] + grades[3] + grades[4]
print(total)
#e
average = total/len(grades)
#f
print(f"average grade:{average:2f}")
#g
grades.pop(3)
grades.remove(51)
#h
print("updated list",grades)
#i
updatedaverage = sum(grades)/ len(grades)
print(f"updated average:{updatedaverage:3f}")