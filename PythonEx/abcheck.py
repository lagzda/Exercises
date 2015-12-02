#Have the function ABCheck(str) take the str parameter being passed and return true if the characters a and b are
#separated by exactly 3 places anywhere in the string at least once (ie. "lane borrowed" would result in true because there is
#exactly three characters between a and b). Otherwise return the string false.

def abcheck(str):
    #Capture the size
    size = len(str)
    #Just so it is easier to compare I transform the string to lowercase
    str = str.lower()
    #No point to iterate through whole string if there may not be enough space
    for i in range(size-4):
        #If the letter is a check if 4 letters after comes b
        if str[i] == 'a' and str[i+4] == 'b':
            return True
    return False    

#Tests        
print abcheck("Rlfasa") 
print abcheck("Ralfsb")