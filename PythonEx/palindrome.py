"""Have the function Palindrome(str) take the str       
parameter being passed and return the string true if the parameter is a palindrome, 
(the string is the same forward as it is backward) otherwise return the string      
false. For example: "racecar" is also "racecar" backwards. Punctuation and numbers  
will not be part of the string. """

#Just because the string will not contain punctuation and numbers (I assume whitespaces either) 
#it is possible to have a cool way of performing the function by checking both sides of the string 
#simultaneously until middle is reached.
#Although theoretically the function's time complexity is O(n) in reality it is only half of that
def palindrome(str):
    #Determine the halved size
    size = len(str)/2
    for i in range(size):
        #Check both sides at the sime time (i.e first - last and so on)
        if str[i] != str[-i-1]:
            #If the characters don't match return False and stop
            return False
    #If the loop completes we know that it is a palindrome    
    return True

#Tests
str = "abba"
str2 = "abcba"
str3 = "abbca"

print palindrome(str)
print palindrome(str2)
print palindrome(str3)

#Added note: A normalisation function could also be implemented such as one that 
#creates a new string containing only alphabetical characters of the old string.