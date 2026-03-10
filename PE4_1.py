#A – C, determine the output displayed by the lines of code.
#A
print("Python") #Python
print("Python"[0]) #P
print("Python"[-1])#n
print("Python"[:]) #Python
#B
str = "Python 123"
print(str)   #Python 123
print(str[0]) #p
print(str[-1]) #3
print(str[:])  #Python 123
#C
strNum = "0, 1, 2, 3, 4, 5, 6, 7, 8, 9"
print(strNum[1], strNum[-1], len(strNum)) #, 9 28
print(strNum[:len(strNum)]) #0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print(strNum[1]+strNum[-3]) #,,