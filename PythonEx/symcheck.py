#A string checking function that checks if each alphabetical letter in a string is surrounded by a +. 
#String cannot be empty and must have at least one alphabetical character
#Returns either True or False. First and last letters don't have to be surrounded from both sides

def symCheck(str):
    #Capture the length of the string
    length = len(str)
    #At the beginning we haven't yet seen eany alphabetical characters so we set the variable to False
    hasCharacters = False
    for i in range(length):
        #The absolute values is needed to transform -1 value to just 1 
        prev = str[abs(i-1)]
        if (i < length-1):
            nxt = str[i+1]
        #If this is the last iteration we just set the next element to previous since there are no next elements    
        else:
            nxt = prev
        #Only check for surrounding + if it is an alphabetical character and also assure that the string has alphabetical characters    
        if str[i].isalpha():
            hasCharacters = True
            if prev != "+" and nxt != "+":
                return False
    #If there were no alphabetical characters return False        
    if (not hasCharacters):
        return False
    #If everything was ok return True
    return True

#Some checks
print symCheck("r+a+l+f+s")
print symCheck("ralfs")
print symCheck("+++++")
print symCheck("++r++")