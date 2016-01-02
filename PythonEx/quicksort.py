#The main function that calls all the subsequent functions
def quicksort(A):
    #Index of last element
    last = len(A)-1
    #Call the helper functin which is gong to be recursive
    helper(A, 0, last)
    
def helper(A, first, last):
    #While index of first element is smaller than last find the splitpoint for a selected pivot
    if first < last:
        #Split the list
        splitpoint = partition(A, first, last)
        #Perform the same to left side of list
        helper(A, first, splitpoint-1)
        #Perform the same to the right side of list
        helper(A, splitpoint+1, last)
        
def partition(A,first, last):
    #Pivot can be anything. I chse the first element of the list
    pivot = A[first]
    #Left side starts from just the next element from pivot
    left = first + 1
    #Right side starts from the last element in the list
    right = last
    #Assume that the list is not sorted at the beginning
    done = False
        
    while(not done):
        #While left side index doesn't overpass the right side index and while left side value is smaller than the pivot
        #increment left side index
        while left <= right and A[left] <= pivot:
            left += 1
        #While left side index doesn't overpass the right side index and while right side value is bigger than the pivot
        #decrement right side index
        while left <= right and A[right] >= pivot:
            right -= 1
        #If left index is bigger than right we have found a splitpoint and checking is done   
        if left > right:
            done = True
        else:
            #Swap the left and right index values after the check
            temp = A[left]
            A[left] = A[right]
            A[right] = temp
    #Swap the pivot value with the right index as that is the place where the pivot belongs        
    temp = pivot 
    A[first] = A[right]
    A[right] = temp
    #Return the new pivot's index
    return right

A = [54,26,93,17,77,31,44,55,20]
quicksort(A)
print(A)
        