#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

#basic solution would be to loop through the array, inside the loop, call another for loop that sums all the numbers leading to the current index and find the average

def countResponseTimeRegressions(responseTimes):
    # Write your code here
    
    #initialize count
    count = 0
    
    for index, time in enumerate(responseTimes, start=1):
        sub_list = responseTimes[:index]
        average = sum(sub_list) / len(sub_list)
        if time > average:
            count += 1
            
            
    return count
