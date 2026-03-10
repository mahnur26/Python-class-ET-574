""" Calculates the amount of a server’s tip. Save the code as PE3_2.py.
a) Prompt and request input the amount of the bill (in float) and the percentage of tip (in integer).
b) Calculate, set the result to two decimal places and print the result.
Input text can be any content. Just make sure to precisely match the output format below 
Example Output 1: Example Output 2:
Enter the amount of the bill: 36.99 Enter the amount of the bill: 100
Enter the percentage of tip: 18 Enter the percentage of tip: 20
Tip: $6.66 Tip: $20.00"""
billAmount = float(input("Enter the amount of the bill :$"))
tipPercent = int(input("Enter the tip Amount :"))
tipAmount = billAmount * tipPercent / 100
print ("Tip = $", round(tipAmount,2))