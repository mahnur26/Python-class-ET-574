""" A – D, identify the errors and rewrite the statement in the correct syntax. """
""" phoneNum = 718-710-4756
print("QCC phone number is " + phoneNum + '.')"""
#A
phoneNum = ("718-710-4756")
print("QCC phone number is: " + phoneNum + '.') # because at first I wasn't using string, they mistook it as subtraction in the numers.
#B 
""" finally = "happily ever after."
print("They lived " + finally) """
finally_ = "happily ever after."
print("They lived " + finally_) #because finally is a keyword itself. that's why I used finally_
#C
""" age = 20
print("I am " + age + " years old.") """
age = 20
print("I am " + str(age) + " years old.") # to join a string with a integer, I have to use str function.
#D
""" age = input("Enter your age: ")
print("Next year you will be " + (age+1)) """
age = int(input("Enter your age: "))
print("Next year you will be " + str(age+1)) # to do math, I have to convert the input to int and to print I have to convert the int into str function
