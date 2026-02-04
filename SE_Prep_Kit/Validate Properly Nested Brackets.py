#
# Complete the 'areBracketsProperlyMatched' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code_snippet as parameter.
#

#can't just count the number of brackets and see if they match. 
# This will require a full loop, when encountering a bracket, continue through the string and check to see if the next bracket is the current one's mate
# Could create series of if statements. 
# Ok, loop through...If it is an open bracket, add it to the checkstring. If it's an closed bracket, check the last index of the check_string, if it is its mate, remove the last index from the string and move on, else return 0. 

def areBracketsProperlyMatched(code_snippet):
    # Write your code here
    checkString = ''
    for index, char in enumerate(code_snippet):
        
        if char in ('({['):
            checkString = checkString + char
            
        elif char in (')}]'):
            if len(checkString) == 0:
                return 0
            mate = checkString[-1]
            
            if char == ')' and mate != '(':
                return 0
                
            if char == '}' and mate != '{':
                return 0
                
            if char == ']' and mate != '[':
                return 0
            
            checkString = checkString[:-1]
    
    if len(checkString) > 0:
        return 0
    else:
        return 1
