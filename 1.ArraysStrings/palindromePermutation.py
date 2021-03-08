# Palindrome Permutation: Given a string, write a function to check if it 
# is a permutation of a palin­drome. A palindrome is a word or phrase that 
# is the same forwards and backwards. A permutation is a rearrangement of 
# letters. The palindrome does not need to be limited to just dictionary words. 



# O(n) time complexity - O(n) space complexity
def hashTableSolution(string):
    string = string.lower()
    charset = [0]*128
    odd_count = 0 
    for char in string:
        if((char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z')):
            continue
        charset[ord(char)] += 1

    for count in charset:
        if(count % 2 == 1):
            odd_count += 1
    
    if odd_count > 1:
        return False
    return True 
