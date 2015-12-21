""" Have the function ExOh(str) take the str parameter
being passed and return True if there is an equal number of x's and o's,
otherwise return False. Only these two letters will be entered in the 
string, no punctuation or numbers. For example: if str is "xooxxxxooxo" then the 
output should return False because there are 6 x's and 5 o's. """

def exoh(str):
    #Initiate two counters
    x_count = 0
    o_count = 0
    #Iterate through string checking if character is 'x'or 'o'and incrementing the coresponding counter
    for i in str.lower():
        if i == 'x':
            x_count += 1
        elif i == 'o':
            o_count += 1
        #Just for pedantic purposes really make sure if the string contains only 'x'es and 'o'es     
        else:
            return "You didn't follow the rules"
    #Return the evaluation of both counter equality
    return x_count == o_count

#Tests
str = "XoxoxO"
str2 = "xxxxxoox"
str3 = "You don't tell me what to do"
print exoh(str)
print exoh(str2)
print exoh(str3)