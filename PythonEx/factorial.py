#A really easy recursive function for finding the factorial of n

def factorial(n):
    #If the number has been reduced to 1 e.g. the last number to multiple by return 1
    if n == 1:
        return 1
    #Return the current number times one smaller, again one smaller and so on until 1 is reached
    return n * factorial(n-1)

print factorial(8)