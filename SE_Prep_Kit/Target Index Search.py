#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'binarySearch' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

#first thought, simple answer, loop through array, return the index that the number is. 
# More efficient answer, when trying to find a target in a sorted array, perform a binary search 
# will need to set the left and right indices, 0 & length of array (-1 for index). Establish the mid, if that number is larger than the target number, move the right variable, otherwise move the left variable

def binarySearch(nums, target):
    
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = left + (right - left)//2
        
        if nums[mid] == target:
            return mid
        
        elif nums[mid] < target:
            left = mid +1
        
        else:
            right = mid - 1
    
    return -1

if __name__ == '__main__':
    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    target = int(input().strip())

    result = binarySearch(nums, target)

    print(result)
