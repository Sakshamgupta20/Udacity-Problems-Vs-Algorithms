# %%
"""
Rearrange Array Elements
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.
"""

# %%
def rearrange_digits(input_list):
    if input_list is None:
        return []
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
print("\nTest Case 3: List with 2 items")
test_function([[1,2], [2,1]]) # Expected output = [2,1]

# Edge Case 1
print("\nEdge Case 1: Empty/None List")
test_function([None, []]) # Expected output = []
test_function([[], []]) # Expected output = []

# Edge Case 1
print("\nEdge Case 2: Big List")
test_function([[i for i in range(200,500)] + [i for i in range(0,200)], [49949749549349148948748548348147947747547347146946746546346145945745545345144944744544344143943743543343142942742542342141941741541341140940740540340139939739539339138938738538338137937737537337136936736536336135935735535335134934734534334133933733533333132932732532332131931731531331130930730530330129929729529329128928728528328127927727527327126926726526326125925725525325124924724524324123923723523323122922722522322121921721521321120920720520320119919719519319118918718518318117917717517317116916716516316115915715515315114914714514314113913713513313112912712512312111911711511311110910710510310199979593918987858381797775737169676563615957555351494745434139373533312927252321191715131197531, 
49849649449249048848648448248047847647447247046846646446246045845645445245044844644444244043843643443243042842642442242041841641441241040840640440240039839639439239038838638438238037837637437237036836636436236035835635435235034834634434234033833633433233032832632432232031831631431231030830630430230029829629429229028828628428228027827627427227026826626426226025825625425225024824624424224023823623423223022822622422222021821621421221020820620420220019819619419219018818618418218017817617417217016816616416216015815615415215014814614414214013813613413213012812612412212011811611411211010810610410210098969492908886848280787674727068666462605856545250484644424038363432302826242220181614121086420]])


