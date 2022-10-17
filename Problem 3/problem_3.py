# %%
"""
Rearrange Array Elements
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.
"""

# %%
def rearrange_digits(input_list):
    sorted_list,result = merge_sort(input_list)

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return (arr,[])

    mid = len(arr) // 2
    left,result = merge_sort(arr[:mid])
    right,result = merge_sort(arr[mid:])

    return combine_left_right(left,right)

def combine_left_right(left,right):
    left_index = 0
    right_index = 0
    merged = []

    index = 0
    max1 = "" #To store maximum number 1
    max2 = "" #To store maximum number 2
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

        if index % 2 == 0:
            max1 += str(merged[index])
        else:
            max2 += str(merged[index])
        index += 1

        
    while left_index < len(left):
        merged.append(left[left_index])
        if index % 2 == 0:
            max1 += str(merged[index])
        else:
            max2 += str(merged[index])
        index += 1
        left_index += 1
    
    while right_index < len(right):
        merged.append(right[right_index])
        if index % 2 == 0:
            max1 += str(merged[index])
        else:
            max2 += str(merged[index])
        index += 1
        right_index += 1

    return (merged,[int(max1),int(max2)])


# %%
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass with output: " +  str(output))
    else:
        print("Fail with output: " +  str(output))

#Case 1
print("\nTest Case 1: List with increasing numbers till 5")
test_function([[1, 2, 3, 4, 5], [542, 31]]) # Expected output = [964,852]

#Case 2
print("\nTest Case 2: List with random multiple numbers")
test_function([[1,2,3,6,9,8,7,4,3,2,1,2,3,9,9,9,9], [999743221, 99863321]]) # Expected output = [[999743221, 99863321]

#Case 3
print("\nTest Case 3: Empty List")
test_function([[], []]) # Expected output = []

#Case 4
print("\nTest Case 4: List with 2 items")
test_function([[1,2], [2,1]]) # Expected output = [2,1]