def processCouponStackOperations(operations):
    # Write your code here
    
    stack = []
    min_stack = []
    results = []
    
    for operation in operations: 
        # print("operation: ", operation)
        
        if 'push' in operation:
            name, value = operation.split(' ')
            val = int(value)
            stack.append(val)
            if not min_stack or val <= min_stack[-1]:
                min_stack.append(val)
            else:
                min_stack.append(min_stack[-1])
            # print('stack after push: ', stack)
            
        elif len(stack) > 0:
            # print("in len(stack > 0)")
            if 'pop' in operation:
                stack.pop()
                min_stack.pop()
            elif 'top' in operation:
                results.append(stack[-1])
            elif 'getMin' in operation:
                # print('appending min to results: ', min)
                results.append(min_stack[-1])
    
    return results
