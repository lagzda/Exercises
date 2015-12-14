"""Have the function WordCount(str) take the str string parameter being passed and 
return the number of words the string contains (ie. "Never eat shredded wheat" would return 4).
Words will be separated by single spaces."""

def word_count(str):
    #Initiate a variable that will store one previous value
    prev = ' '
    #Word count
    words = 0
    for i in str:
        #Check if the previous character is a space before an alphabetical character
        if i.isalpha() and prev == ' ':
            words+=1
        #Update previous value    
        prev = i
    return words

#Test
str = "My name is Ralfs Lagzda"
print word_count(str)
            