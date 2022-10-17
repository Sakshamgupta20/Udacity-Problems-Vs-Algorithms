Here we are using recrsion with help of binary search algoritm

I have modified binary search to include roteted array search
    In case of rotated array there can be 2 conditions in binary search

    ARRAY = [0,1,2,4,5,6,7]
    1. Middle element is part of right side of arrays end element
        Pivot = 4 => [4,5,6,7,0,1,2] 
    2. Middle element is part of left side of arrays first element
        Pivot = 5 => [5,6,7,0,1,2,4]
    
Time complexity =>
    O(logN) because we have just addied 2 more conditions in binary search

Space complexity =>
    O(1) as we are not  using any extra space