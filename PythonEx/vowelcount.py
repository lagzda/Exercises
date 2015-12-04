#  Vowel Count                                                                         
#  Have the function VowelCount(str) take the str
#  string parameter being passed and return the number of vowels the string contains  
#  (ie. "All cows eat grass" would return 5). Do not count y as a vowel for this
#  challenge.

def vowelCount(str):
    #Convert the string to lower for easier comparison
    str.lower()
    #Define the vowels
    vowels = "aeiou"
    #Initiate the count to 0
    count = 0
    #Compare each character to each vowel
    for i in str:
        #Although it is a nested loop the time complexity ultimately is O(n*5) = O(n)
        for j in vowels:
            if i == j:
                count += 1
    return count

print vowelCount("aeiou")
print vowelCount("Ralfs")
print vowelCount("zxcvbnm")