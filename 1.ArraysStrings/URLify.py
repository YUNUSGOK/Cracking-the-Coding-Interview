#  Write a method to replace all spaces in a string with '%20'. 
# You may assume that the string has sufficient space at the end 
# to hold the additional characters, and that you are given the 
# "true" length of the string. (Note: If implementing in Java, 
# please use a character array so that you can perform this o
# peration in place.)


# O(n) time complexity - O(n) space complexity
def shiftingToNewArray(s):
    index = 0
    res = ['']*(len(s))
    n = len(s)
    i = 0
    while(n > i):
        if(s[i] == ' '):
            res[index] = '%' 
            res[index+1] = '2' 
            res[index+2] = '0' 
            index += 3
            n -= 2

        else:
            res[index] = s[i]
            index += 1
        i += 1
    return ''.join(res)

# O(n) time complexity - O(1) space complexity
# Spaces at the end will be used as buffer to shift array    
def inplaceShifting(s):
    space_count = 0
    for c in s:
        if(c == ' '):
            space_count += 1

    i = len(s)-1- int(space_count*2/3)

    index = len(s)-1
    while(index >= 0):
        if(s[i] ==' '):
            s[index] = '0'
            s[index-1] = '2'
            s[index-2] = '%'
            index -=3

        else:
            s[index] = s[i]
            index -= 1
        i -= 1
        
    return ''.join(s)
        