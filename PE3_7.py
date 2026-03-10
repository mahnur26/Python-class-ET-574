# A – J, determine and explain the output displayed by the lines of code. 
#A
str0 = "py"
print(str0[0])
print(str0[-1])
print(str0[:])
print(str0[0], str0[-1],
str0[:], sep = ' ')
""" 
p # it means index 0 which is the first letter
y # it means index -1 which is the last letter
py # a slice with colon means the entire string
p y py """ # prints the same thing in one line separated by single space.
#B
print('C'[0])
print("C"[-1])
print('C'[:])
print('C'[0], 'C'[-1],
'C'[:], sep = '\t')
""" 
C # the first slice is C
C # the last slice is also C
C # the whole slice is also C
C       C       C """ # all the C are separated by \t which is tab
#C
str1 = "coDE"
print(str1.capitalize()+'\n'+str1.upper()+'\n'+str1.lower())
print(str1)
""" Code #here it is capitalization, capitalize the first letter and lowerize the rest
CODE # all uppercase
code # all lowercase
coDE """ # the whole str1 
#D
str2 = "computer science"
print(str2.title(),'|',str2[0:8],'|',str2[:3],'|',
str2[-5:-1], '|', str2[-2:] )
print(str2.title(), str2[0:8], str2[:3],
str2[-5:-1], str2[-2:], sep = ' | ')
""" Computer Science | computer | com | ienc | ce  
Computer Science | computer | com | ienc | ce """
# first, it capitalized the first letter of every word, then it went 0 through 7. then from the first to 2
# it started from -5 untill -1 then it went 2 to the end