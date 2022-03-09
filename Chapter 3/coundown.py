def countdown(i):
    print i
    # Base case
    if i <= 0:
        return
    # Recursive case
    else:
        countdown (i -1)

countdown(10)
