# In recursive approach there is a stack of data

#Q. find the factorial of a given number

#recursive :

def recursiveNum(n):
    if n == 1:
        return 1
    else:
        return n*recursiveNum(n-1)

print(recursiveNum(5))

# the recursive methos is more complex in nature. calling the function again and again makes this approach slower and reverse engineering is also complex

#iterative yk, for loop