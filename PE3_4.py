""" Sort three input numbers.
a) Prompt and request three integer numbers one by one from the console.
b) Sort these numbers and print them from smallest to largest.
Input text can be any content. Just make sure to precisely match the output format below.
Hint: You can use the built in functions max() and min() 
Example Output:
Please enter the first integer: 7
Please enter the second integer: 8
Please enter the third integer: 1
Before sorting: 7 8 1
After sorting: 1 7 8 """

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
print("Before sorting: ", num1, num2, num3)
smallest = min(num1 , num2, num3)
largest = max(num1, num2, num3)
middle = largest - smallest 
print("After sorting:", smallest, middle, largest)