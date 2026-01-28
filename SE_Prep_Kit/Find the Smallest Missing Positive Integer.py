# Complete the 'findSmallestMissingPositive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY orderNumbers as parameter.
#


def findSmallestMissingPositive(orderNumbers):
    # Write your code here
    
    n = len(orderNumbers)
    x = 0
    
    while x < n:
        correct_position = orderNumbers[x] - 1
        if 1 <= orderNumbers[x] <= n and orderNumbers[x] != orderNumbers[correct_position]:
            orderNumbers[x], orderNumbers[correct_position] = orderNumbers[correct_position], orderNumbers[x]
        else:
            x += 1
            
    for x in range(n):
        if orderNumbers[x] != x + 1:
            return x + 1
    
    return n + 1
