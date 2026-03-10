""" Using string indices.
a) Prompt and request an input word with 6 letters from the console.
b) Display the letters of the word in reverse order.
Input text can be any content. Just make sure to precisely match output format below.
Example Output:
Please enter a 6-letter word: Python
Python
nohtyP """

word = input("Please enter a 6-letter word: ")
print(word)
print(word[5]+word[4]+word[3]+word[2]+word[1]+word[0])