#you can store the result or outcome of a function in the form of cache so if you need to run the 
# funtion agian and again, it will just show the result of previously stored value.
import time
import functools
@functools.lru_cache(maxsize = 2) #the maximum number of times it will store the calling of this function
def someComplexFunc(n) -> str:
    time.sleep(n)  #assume this is some complex function which takes a lot of time and resources
    return f"It took {n} seconds to complete this command"

print(someComplexFunc(3))
print(someComplexFunc(3))
print(someComplexFunc(3)) # on the 3rd time 
print(someComplexFunc(4))
print(someComplexFunc(4))  # we are needing to call the func again and again
