def processCouponStackOperations(operations):
    # Write your code here
    
    # class Stack (list):
        
    #     def push(self, item):
    #         self.append(item)
        
    #     def pop(self):
    #         return self.pop()
        
    #     def top(self):
    #         return self[-1]
            
    stack = []
    results = []
    # min = None
    
    for operation in operations: 
        # print("operation: ", operation)
        
        if 'push' in operation:
            name, value = operation.split(' ')
            stack.append(int(value))
            # if min is None:
            #     min = value
            # elif value < min:
            #     min = value
            # print('stack after push: ', stack)
            
        elif len(stack) > 0:
            # print("in len(stack > 0)")
            if 'pop' in operation:
                stack.pop()
            elif 'top' in operation:
                results.append(stack[-1])
            elif 'getMin' in operation:
                # print('appending min to results: ', min)
                results.append(min(stack))
    
    return results
