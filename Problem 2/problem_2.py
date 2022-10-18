# %%
"""
Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4


"""


# %%
def rotated_array_search(input_list, number):
    if input_list is None or len(input_list) == 0:
        return -1

    return rotared_array_search_sol(input_list, number, 0, len(input_list)-1)


def rotared_array_search_sol(input_list, number, begin_index, end_index):
    if begin_index > end_index:
        return -1

    mid = begin_index + ((end_index - begin_index) // 2)

    if input_list[mid] == number:
        return mid

    #It means array was partitioned here and the mid is the end number of right side
    #e.g. 4,5,6,7,0,1,2, here 7 is mid
    if (mid+1 <= end_index and input_list[mid] > input_list[mid + 1]) and (mid - 1 >= begin_index and input_list[mid] > input_list[mid - 1]):
        if input_list[end_index] > number:
            return rotared_array_search_sol(input_list, number, mid + 1, end_index)
        return rotared_array_search_sol(input_list, number, begin_index, mid - 1)

    #It means array was partitioned here and the mid is the first number of left side
    #e.g. 5,6,7,0,1,2,3 here 0 is mid
    if (mid+1 <= end_index and input_list[mid] < input_list[mid + 1]) and (mid - 1 >= begin_index and input_list[mid] < input_list[mid - 1]):
        if input_list[begin_index] < number:
            return rotared_array_search_sol(input_list, number, mid + 1, end_index)
        return rotared_array_search_sol(input_list, number, begin_index, mid - 1)

    if number < input_list[mid]:
        return rotared_array_search_sol(input_list, number, begin_index, mid - 1)

    else:
        return rotared_array_search_sol(input_list, number, mid + 1, end_index)

# %%
def linear_search(input_list, number):
    if input_list is None:
        return -1
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    output = rotated_array_search(input_list, number)
    if linear_search(input_list, number) == output:
        print("Pass with output: " + str(output))
    else:
        print("Fail")


#CASE 1
print("\nTest Case 1: Pivot element lies in between is of right side last element")
test_function([[16, 17, 18, 19, 10, 11, 12, 13, 14], 11]) #Expected output 5

#CASE 2
print("\nTest Case 2: Pivot element lies in between is of left side first element")
test_function([[5,6,7,0,1,2,4], 1]) #Expected output 4


#CASE 3
print("\nTest Case 3: Pivot element lies in between is of left side first element")
test_function([[5,6,7,0,1,2,4], 7]) #Expected output 2

#Edge CASE 1
print("\nTest Edge Case 1: Empty List/None List")
test_function([[], 1]) #Expected output -1

print("\nTest Edge Case 1: Empty List/None List")
test_function([None, 1]) #Expected output -1

#Edge CASE 2
print("\nTest Edge Case 2: Big List")
test_function([[i for i in range(200,500)] + [i for i in range(0,200)], 400]) #Expected output 200



# %%



