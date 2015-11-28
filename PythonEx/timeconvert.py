#A function that takes in a parameter as seconds and converts it to hours:minutes

def timeConvert(sec):
    #Mitutes are calculated by diving seconds with 60 and wraping it around another 60 since there are 60 minutes in an hour
    minutes = sec // 60.0 % 60
    #Hours are calculated by diving the seconds and then minutes
    hours = sec // 60.0 // 60.0
    print "%i:%i" %(hours, minutes)
#Test    
timeConvert(7200)    