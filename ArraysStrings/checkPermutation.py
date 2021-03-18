# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.


# O(nlogn) time complexity - O(n) space complexity
# Botteneck is the sorting part. After sorting,s comperison complexity will be O(n)
# Comperision comlexity can be reduced to O(n) by counting sort since charset 
# has fixed length counter array size will be limited.

def sortedSolution(s1, s2):
    if(len(s1) != len(s2)):
        return False
    
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)
    for i in range(len(s1)):
        if(s1_sorted[i] != s2_sorted[i]):
            return False
    return True

# O(n) time complexity - O(n) space complexity
def hashTableSolution(s1, s2): 
    charset = [0]*256
    for c in s1:
        charset[ord(c)] += 1
    for c in s2:
        if(charset[ord(c)]==0):
            return False
        charset[ord(c)] -= 1
    for i in range(256):
        if(charset[i] != 0):
            return False
    return True
    