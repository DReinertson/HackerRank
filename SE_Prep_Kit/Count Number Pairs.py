def countAffordablePairs(prices, budget):
    # Write your code here
    # print('prices, budget: ', prices, budget)
    # print('length: ', len(prices))
    valid_pairs_count = 0
    
    if len(prices) <= 1:
        return 0
    
    i = 0
    j = 1
    
    while i < len(prices)-1:
        
        if prices[i] + prices[j] <= budget:
            valid_pairs_count += 1
        
        j += 1
        
        # print ('i, j before: ', i, j)
        if j == len(prices):
            i += 1
            j = i + 1
        # print ('i, j after: ', i, j)
                    
                    
    return valid_pairs_count
