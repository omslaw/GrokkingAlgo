##def count(list, x):
##    #total = 0
##    if list == []:
##        print "base case"
##        return ("asdf", 0)
##    print count(list [-1], x + 1)
##
##x = 0
##list = [1,2,3,4,5]
##count(list, x)

# again couldn't complete it on my own. answer from book
# i changed it a bit as it wasn't returning a value when ran

def count(list, y):
    if list == []:
        print y
        return y
    #print "asdf", list
    y = y + 1
    #print "y", y
    return 1 + count(list[1:], y)


y = 0
list = [1,2,4,4,4,3, 3, 3, 3, 3]
count(list, y)

