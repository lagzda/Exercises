#Take a string as a parameter and return all the characters in alphabetical order
#For this I use merge sort and comments can be found in my CS50/Algorithms/mergesort.c file
#Although that file is in c the algorithm is pretty much the same

def sort(str, min, mid, max):
    left = str[min:mid+1]
    right = str[mid+1:max+1]
    i = 0
    j = 0
    k = min
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            str[k] = left[i]
            i += 1
            k += 1
        else:
            str[k] = right[j]
            j += 1
            k += 1
    while i < len(left):
        str[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        str[k] = right[j]
        j += 1
        k += 1

def mergesort(str, min, max):        
    if (min < max):
        mid = (min + max)/2
        mergesort(str, min, mid)
        mergesort(str, mid+1, max)
        sort(str, min, mid, max)
        
def alphasoup(str):
    #Convert string to array so we can make modifications to it
    strarr = [i for i in str]
    #Execute mergesort
    mergesort(strarr, 0, len(strarr) - 1)
    #Join the array back to string
    print "".join(strarr)
    
alphasoup("cbadasd")    
    