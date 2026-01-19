sentence = "Coading in Python is fun "
sum = 0
vowels = ['a' , 'e' , 'i' , 'o' , 'u']
for char in sentence.lower():
    print (char)
    if(char in vowels):
        sum += 1
        
print (f" there are {sum} vowels in this sentence")