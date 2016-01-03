def intersection(arr1, arr2):
    #This is so we always use the smallest array
    if len(arr1) > len(arr2): arr1, arr2 = arr2, arr1
    #Initialise the intersection holder    
    inter = []
    for i in arr1:
        #If it is an intersection and avoid duplicates
         if i in arr2 and i not in inter:
            inter.append(i)
    return inter

#Test
arr1 = [54,26,93,17,77,31,44,55,20]
arr2 = [54, 93, 93, 7]
print intersection(arr1, arr2)
