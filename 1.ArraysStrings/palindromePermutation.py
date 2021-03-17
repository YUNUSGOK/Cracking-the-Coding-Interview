# Palindrome Permutation: Given a string, write a function to check if it 
# is a permutation of a palin­drome. A palindrome is a word or phrase that 
# is the same forwards and backwards. A permutation is a rearrangement of 
# letters. The palindrome does not need to be limited to just dictionary words. 



# O(n) time complexity - O(n) space complexity
def hashTableSolution(string):
    lst = list(string.lower())
    charset = [0]*128
    odd_count = 0 

    for c in lst:

        if((c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z')):
            charset[ord(c)] += 1


    for count in charset:
        
        if(count % 2 == 1):
 
            odd_count += 1
    
    if odd_count > 1:
        return False
    return True 

