class max_heap():
    def __init__(self, items = []):
        #Initialise the 0th element just as zero because we will ignore it (for finding purposes)
        self.heap = [0]
        #Add each element to the list via push which sorts it correctly
        for i in items:
            self.push(i)
            
    #For the print function to ouput the proper heap list        
    def __str__(self):
        return str(self.heap[1 : len(self.heap)])
    
    #Add element to the heap's end initially and find the right location for it via float_up
    def push(self, i):
        self.heap.append(i)
        self.__float_up(len(self.heap) - 1)
        
    #Get the max value if the heap is not empty    
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
        
    def pop(self):
        #If the heap contains more than one element swap the last element with the biggest and pop the biggest which is 
        #now at the end. After bubble down the top element which was swapped to the correct location via bubble_down
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap)-1)
            max = self.heap.pop()
            self.__bubble_down(1)
        #If the heap contains just one element just pop it (remember the ignored 0)   
        elif len(self.heap) == 2:
            max = self.heap.pop()
        #If the heap is empty return false    
        else:
            max = False
        return max
    #A helper swap function that does just that
    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    #When inserted find the right location for value    
    def __float_up(self, i):
        #Get the parent node's index for the new inserted element
        parent = i // 2
        #If is the only element return
        #Also this is the base case for the recursion
        if i <= 1:
            return
        #If child is bigger than parent then swap
        elif self.heap[i] > self.heap[parent]:
            self.__swap(i, parent)
            #Recursion continues with parent but it actually is the same value from before because of the swap(i <-> parent)
            self.__float_up(parent)
            
    def __bubble_down(self, i):
        #Get node's left child
        left = i * 2
        #Get node's right child
        right = i * 2 + 1
        #Initially asume that the peek value is indeed the largest
        largest = i
        #If the node has a left child compare it and if child is greater then swap
        if len(self.heap) > left and self.heap[left] > self.heap[largest]:
            largest = left
        #If the node has a right child compare it and if child is greater then swap    
        if len(self.heap) > right and self.heap[right] > self.heap[largest]:
            largest = right
        #If there have been found new larger values than the initial largest value swap down and repeat recursion    
        if largest != i:
            self.__swap(i, largest)
            #Again the largest value is actually the value that we started with because of the swap(i <-> largest)
            self.bubble_down(largest)

#Tests            
m_h = max_heap([1,7,4])
print m_h
m_h.push(10)
print m_h
        
            