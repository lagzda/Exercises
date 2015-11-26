#A function that adds up all the numbers from 1 to num

def numAdd(num): 
    #A great explanation of why this works can be found here - http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/runsums/triNbProof.html
    return (num*(num+1)) / 2
    #Much better than a for loop.
print numAdd(4)    
