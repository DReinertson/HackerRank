def countAffordablePairs(prices, budget):
    # Write your code here
    # print('prices, budget: ', prices, budget)
    # print('length: ', len(prices))
    valid_pairs_count = 0
    
    if len(prices) <= 1:
        return 0
    
    else:
        for index, price in enumerate(prices):
            for j in range(index + 1, len(prices)):
                # print("i, j: ", i, j)
                # print("i")
                if prices[j] + price <= budget:
                    valid_pairs_count += 1
                    
                    
    return valid_pairs_count
