# %%
"""
Finding the Square Root of an Integer
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))
"""

# %%
def square_root(num):
    return square_root_sol(num,1,num,None)

def square_root_sol(num,start,end,ans):
    if start >= end:
        return ans

    mid = (end + start) // 2

    if mid * mid == num:
        return mid

    if mid * mid > num:
        return square_root_sol(num,start,mid - 1,ans)
    else:
        ans = mid
        return square_root_sol(num,mid + 1,end,ans)

# %%
#CASE 1
print("\nTest Case 1: Number is a perfect square")
print(square_root(196)) #Expected output 13

#CASE 2
print("\nTest Case 1: Number is not a perfect square")
print(square_root(417)) #Expected output 20

#CASE 3
print("\nTest Case 1: Number is very big")
square_root(19873124322121) #Expected output 4457927



# %%



