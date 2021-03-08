# Is Unique: Implement an algorithm to determine if a string has all unique characters. 

# O(n^2) time complexity 
def bruteForce(s):
    for i in range(len(s)):
        for j in range(len(s)):
            if( i != j and s[i] == s[j] ):
                return False
    return True

# O(n) time complexity - O(n) space complexity
def hashTableSolution(s):
    charset = [False]*256
    for c in s:
        if(charset[ord(c)]):
            return False
        charset[ord(c)] = True
    return True


