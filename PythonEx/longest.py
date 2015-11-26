#A function for finding the longest word in a sentence 

#Note : I could have implemented the isAlpha() funtion myself by checking ASCI ranges but it doesn't really affect the purpose of this exercise.
def longest(sent):
    #Variable to store the current longest number
    word = ""
    #Variable to store the temporary word
    temp = ""
    #Iterate through every character
    for i in range(len(sent)):
        #If the character is alphabetical add it to temporary word
        if sent[i].isalpha():
            temp += sent[i]
        #If the temporary word is longer than the longest make temporary word the longest    
        if len(temp)>len(word):
            word = temp
            #If the character is not alphabetical it probably indicates that the current word has finished so we change temp back to emtpy
        if sent[i].isalpha() == False:
            temp = ""
    return word        
        
            
sent = "Ralfs Lagzda is my name"    
print longest(sent)            
        