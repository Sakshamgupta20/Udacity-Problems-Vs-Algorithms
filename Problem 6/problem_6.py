# %%
"""
Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.
"""

# %%
def get_min_max(ints):
    if ints is None or len(ints) == 0:
        return (None,None)

    min_num = ints[0]
    max_num = ints[0]

    for num in ints:
        if num < min_num:
            min_num = num
        
        if num > max_num:
            max_num = num
    return (min_num,max_num)



# %%
## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

#Case 1 

print("\nTest Case 1: Random numbers")
print ("Pass with output: " + str(get_min_max(l)) if ((0, 9) == get_min_max(l)) else "Fail") #(0, 9)

#Case 2
print("\nTest Case 2: Empty array")
print ("Pass with output: " + str(get_min_max([])) if ((None,None) == get_min_max([])) else "Fail") #(None,None)


#Case 3
print("\nTest Case 3: Array with same numbers")
print ("Pass with output: " + str(get_min_max([4,4,4,4,4,4,4,4,4,4])) if ((4,4) == get_min_max([4,4,4,4,4,4,4,4,4,4])) else "Fail") #(4,4)

#Edge Case 1
print("\nEdge Case 1: None array")
print ("Pass with output: " + str(get_min_max(None)) if ((None,None) == get_min_max(None)) else "Fail") #(None,None)

#Edge Case 2
print("\nEdge Case 2: Big list")
import random
arr = [i for i in range(501,5000)]
random.shuffle(arr)
print ("Pass with output: " + str(get_min_max(arr)) if ((501,4999) == get_min_max(arr)) else "Fail") #(None,None)

# %%



