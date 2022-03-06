def binary_search(list, item):
    low = 0
    high = len(list) -1
    

    while low <= high:
        mid = (low + high)
        print "mid ", mid
        guess = list[mid]
        print "guess is", guess
        if guess == item:
            return "you go it", mid
        if guess > item:
            high = mid - 1
            print "too high now high is", high
        else:
            low = mid + 1
            print "else now low is", low
        return None

my_list = [1, 3, 5, 7, 9]

print binary_search(my_list, 3)
print
print binary_search(my_list, -1)
print 
print binary_search(my_list, 10)
print 
print binary_search(my_list, 9)
print 
