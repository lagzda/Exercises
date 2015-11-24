#The recursive algorithm for solving the hanoi towers puzzle
#Link to the puzzle - https://en.wikipedia.org/wiki/Tower_of_Hanoi

#Pole1 is the start pole from where the disks need to be moved
#Pole2 is the middle pole we use to temporarily place a disk
#Pole3 is the end/destination pole that the disks need to be moved to
#Size is the number of disks that are initially on the starting pole
def hanoi(pole1, pole2, pole3, size):
    #Checks if there are remaining disks that still need to be moved
    if size < 1:
        return
    #Starting from the size of the tower (lets say 2) it helps to think of it from bottom up
    #At the beginning we are looking at the bottom disk but it also needs to be the highest disk for us to be able to move it
    #So we call the function again by looking one disk higher (hence the size - 1)
    #The only thing is that we apply the logic that the highest element will have to be moved to the temporary pole
    hanoi(pole1, pole3, pole2, size-1)
    #At a specific moment this print line is the only thing that is happening since both recursive calls will just return (size<1)
    #And then the print line executes immediately after the first print since it was called in the above recursive call
    print "Moving the disk from %s to %s" %(pole1, pole2)
    #Now we just move the disk from temporary pole to the end pole
    hanoi(pole3, pole2, pole1, size-1)

#Call the function. The values can be anything we want including the size
#This way it just represents the movement of tower from first pole to the last
hanoi("Start","End","Middle",2);
