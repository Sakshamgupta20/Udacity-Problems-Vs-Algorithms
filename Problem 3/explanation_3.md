Here i have used merge sort to get the output, Merge sort divides the array into parts and then combines them

We have the same use case we need to generate numbers which results in highest sum

During combination process of merge sort we can generate maximum numbers by picking them 1 by 1
e.g  combine => [3,2,1] [6,5,0]
        max1 - 6 3 1
        max 2 - 5 2 0

    and returning it with merged sorted array

Time complexity - 
    O(nLogn) -> It will be same as merged sort as we have just added new conditions

Space complexity - 
    We are now using 2 strings to store max1 and max2
    O(N) -> Used which sorting to store merged array (auxiliary space)
    O(2) -> Used to store strings

    O(N) + O(2) => O(N)