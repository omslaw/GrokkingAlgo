def sum(x):
    y = x
    
    #z = 0
    print "yo", x
    if len(x) == 0:
        print "base case"
    else:
        #print y + sum(x[-1])
        #print "in else for y", y[-1]
        #t = z(-1)

        z = y.pop(-1)
        #print "this is z", z
        #total + int(z[-1])
    
        #return sum(y)
        return x[0] + sum(x[:1])
        #print z + sum(y.pop(-2))
    print "outside of loop"

# Had to get answer from the book as i couldnt get it
##def sum(x):
##    if x == []:
##        return 0
##    return x [0] + sum(x[1:]) 
    

print sum([1,2,13])
