# A – C, identify the errors and rewrite the statements in the correct syntax.
#A
'''myList = ['apple','banana','cherry']
print(myList[3] ''' # it always starts counting from 0, there is no 3 index
myList = ['apple','banana','cherry']
print(myList[2])
#B
''' print(myList[-1:-4]) ''' # there is no -4 so after starting from -1' it can not return it will become an empty string.
print(myList[::-1])
#C
''' word = 'sea'
word[0] = 'p'
print(word) ''' # convert to a list
word = ["s","e","a"] 
word[0] = 'p'
print(word)
#D
'''n = [1, "two", 'three', 4] 
print(" ".join(n)) '''#list of strings - convert numbers to strings
n = ['1', "two", 'three', '4'] 
print(" ".join(n))