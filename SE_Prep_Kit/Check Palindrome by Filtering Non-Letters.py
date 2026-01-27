#ok, first thought, loop through string, create a new string, by removing the special characters, change it to lowercase and then compare left & right side of string, incrementing each loop. 
#remove all the special characters - create a dict of all the valid characters

def isAlphabeticPalindrome(code):
    # Write your code here
    #print('first_string: ', code)
    check_string = code.lower()
    my_string = ""
    
    for index, letter in enumerate(check_string):
        #print('letter: ', letter)
        if letter.isalpha():
            my_string += str(letter)
            #print('my_string + letter: ', my_string)

    reversed_string = list(reversed(my_string))
    #print('reversed_string: ', reversed_string)
        
    for index, letter in enumerate(my_string):
        #print('og letter: ', letter, 'reversed_index: ', reversed_string[index])
        if not letter == str(reversed_string[index]):
            #print('does not match')
            return 0
    
    #print('does match fully')
    return 1
