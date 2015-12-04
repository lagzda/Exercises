#An implementation of a singly linked list (sorted).

#Definition of a single node that will be the atomic object in the linked list
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

#Definition of a list where all the nodes will be stored         
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def getHead(self):
        print self.head.value
    def getTail(self):
        print self.tail.value
    def insert(self):
        value = int(input("Enter a value you want to add: "))
        ptr = self.head
        #Create the node object
        node = Node(value)
        #First case - if the list is empty we insert the item as the head(start) as well as the tail(end)
        if ptr == None:
            self.head = node
            self.tail = node
        else:    
            #Second case - if the value we want to insert is the smallest value (prepend)
            if value < ptr.value:
                node.next = self.head
                self.head = node
            #Third case - if the value we want to insert is the bigest value (append)
            elif value > self.tail.value:
                self.tail.next = node
                self.tail = node
            #Fourth case - the value should go somewhere in the middle
            else:
                while ptr != self.tail:
                    if value > ptr.value and value <= ptr.next.value:
                        node.next = ptr.next
                        ptr.next = node
                    ptr = ptr.next 
            
    def traverse(self):
        print "The list is: "
        ptr = self.head
        while (ptr != None):
            print "%i " % ptr.value
            ptr = ptr.next

ll = LinkedList()            
selection = 0
while (selection != 5):
    print "1: Traverse; 2: Insert, 3: Get Head, 4: Get Tail, 5: Quit"
    try:
        selection = int(input("Your selection: "))
        if selection == 1:
            ll.traverse()
        elif selection == 2:
            ll.insert()
        elif selection == 3:
            ll.getHead()
        elif selection == 4:
            ll.getTail()
    except:
        print("Try again")
    