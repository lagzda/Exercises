#A function that shifts the letter by one position (ie. c becomes d, z becomes a) and then transorms lower case vowels to uppercase.

#This is a helper funtion that allows me to work with asci values to add the 1 position for letter
def transform(char):
    #I check for lower or upper because they are in different positions in the asci table and I need to know how much to subtract.
    if char.isupper():
        #This is a bit scary looking function and I probably could have made this a bit better but here's what it does:
        #1. The chr says that we are going to return a character value
        #2. ord function converts a char to an int asci value for example B becomes 66
        #3. It subtracts the 65 so we could deal with the alphabet counting from 0 to 26 (and for the modulo to work)
        #4. +1 is the wanted modification 
        #5. Now as there are 26 characters in the alphabet we need to make the alphabet wrap around 26 so z+1 would become a for example (modulo or % 26)
        #6. Add back the 65 so it holds a real alphabetical character value
        return chr(((ord(char) - 65) + 1) % 26 + 65)
    else:
        return chr(((ord(char) - 97) + 1) % 26 + 97)

#This is the main function    
def letChange(str):
    #Variable to store the new string
    newStr = ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(str)):
        #Temporary holder for value
        temp = str[i]
        #If the current character is alphabetical lets transform it with the help of the helper function
        if temp.isalpha():
            temp = transform(temp)
            #Check if the character is a lower case vowel and if it is transform it to upper case
            #If you don't want it do so manually you can easily use - if temp in vowels - instead of the for loop
            for j in range(len(vowels)):
                if temp == vowels[j]:
                    temp = chr(ord(temp)-32)
        #Add the new character to the resulting string    
        newStr += temp
    return newStr    

#the z is intentional to demonstrate how it wraps iver the alphabet
str = "Ralfs Lagzda iz my name"
print letChange(str)