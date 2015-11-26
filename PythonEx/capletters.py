#A function to capitalise the first letter of each word

def capLetters(str):
    newstr = ""
    for i in range(len(str)):
        temp = str[i]
        if (str[i-1] == " " or i == 0) and temp.islower():
            temp = chr(ord(str[i])-32) #Or just temp.upper()
        newstr += temp    
    return newstr        
str = "ralfs lagzda is my name"
print capLetters(str)