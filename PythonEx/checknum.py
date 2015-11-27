#Using the Python language, have the function CheckNums(num1,num2) take 
#both parameters being passed and return the string true if num2 is greater
#than num1, otherwise return the string false. If the parameter values are
#equal to each other then return the string -1.

#Well this function is pretty straight forward - it just compares the two numbers.
def CheckNums(num1, num2):
    if num1 > num2:
        return "true"
    elif num2 > num1:
        return "false"
    else:
        return "-1"

# Check if the user complies with the rules e.g. User has to input number instead of a character     
ok = False    
while(not ok):
    #Try to complete the function as normal and if it succeeds set ok to true 
    try:
        num1 = float(input("First number please: "))
        num2 = float(input("Second number please: "))
        ok = True
    #If the user inputs a character or something uncompatible catch the error and rerun the loop  
    except:
        print "Please enter numbers only"
#Run the function               
print CheckNums(num1, num2)