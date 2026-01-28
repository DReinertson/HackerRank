#how do you define if something is a rotation of something else? 
#Could manually rotate s1 and see if it matches s2, but this would exhausting, I guess it would just be a while loop for the length of the string?

def isNonTrivialRotation(s1, s2):
    # Write your code here
    
    n = len(s1)
    i = 0
    
    if s1 == s2 or len(s1) != len(s2):
        return 0
    
    while i <= n:
        # print ("before mods: ", s1)
        if s1 == s2:
            return 1
        else:
            s1 = s1[1:] + s1[0]
            # print("after mods:", s1)
            i += 1
            
    return 0
