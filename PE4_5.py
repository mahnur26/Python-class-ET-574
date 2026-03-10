''' Requests a name from the user.
a) Use Input() to prompt and request a full name.
b) After the user types the full name and presses the Enter (or Return) key,
display the first name and last name in two separate lines.
Input text can be any content. Just make sure to precisely match the output format below. '''
#a
name = input("Enter the full name of your favorite US president:" )
#b
namepart = name.split()
print("first name: ",namepart[0].title())
print("last name: ",namepart[-1].title())