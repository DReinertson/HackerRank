#
# Complete the 'findFirstOccurrence' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#
#Essentially binary search with added steps. As the instructions state, perform a standard Binary Search. If the target is found, search the array to the left of that index to see if the target appears before it. Will need to alter the if statement that determines if the target was found, if so, set the index of that target to a variable (that will be later returned) and set the right value to the mid point, so that the binary search continues. 

def findFirstOccurrence(nums, target):
    # Write your code here
    
    left = 0
    right = len(nums) - 1
    lowest = None
    
    
    while left <= right:
        mid = left + (right - left)//2
        
        if nums[mid] == target:
            lowest = mid
            right = mid - 1
        
        elif nums[mid] < target:
            left = mid +1
        
        else:
            right = mid - 1
    
    if lowest is None:
        return -1
    else:
        return lowest
