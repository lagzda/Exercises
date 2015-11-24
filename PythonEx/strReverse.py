#A simple recursive function for reversing a string

#As each function has it's own stack frame you can really think of this recursive function as an elegant way to implementing the stack data structure.

#I could have omitted the size parameter and do it with slices but I wanted to do it this way
def reverse(string, size):
    #If the last character is reached return just that character
    if size < 1:
        return string[0]
    #Return the last character and decrease the size of string by one
    #The + is O(n) time
    return string[size] + reverse(string, size - 1)

string = "Whatever you like"
#Length is -1 because we start to count elements from 0 
print reverse(string, len(string)-1)
