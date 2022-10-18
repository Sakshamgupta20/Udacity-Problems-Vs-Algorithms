# %%
"""
Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.
"""

# %%
def sort_012(input_list):
    if input_list is None or len(input_list) <= 1:
        return input_list
    
    front_index = 0
    pos_0_index = 0
    pos_2_index = len(input_list) - 1

    while front_index <= pos_2_index:
        if input_list[front_index] == 0:
            input_list[front_index] = input_list[pos_0_index]
            input_list[pos_0_index] = 0
            front_index += 1
            pos_0_index += 1
        elif input_list[front_index] == 2:
            input_list[front_index] = input_list[pos_2_index]
            input_list[pos_2_index] = 2
            pos_2_index -= 1
        else:
            front_index += 1
    return input_list

# %%
def test_function(test_case):
    sorted_array = sort_012(test_case)
    if (test_case is None and sorted_array is None) or (sorted_array == sorted(test_case)):
        print("Pass with output: " + str(sorted_array))
    else:
        print("Fail with output: " + str(sorted_array))

#Case 1
print("\nTest Case 1: List with random 0,1,2 numbers")
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]) #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]

#Case 2
print("\nTest Case 2: List without any numbers")
test_function([]) #[]

#Case 3
print("\nTest Case 3: List with 1 number")
test_function([1]) #[1]

#Edge Case 1
print("\nEdge Case 1: None List")
test_function(None) #None

#Edge Case 2
print("\nEdge Case 2: Big list")
test_function([2]*50 + [0]*50 + [1] * 100)

# %%



