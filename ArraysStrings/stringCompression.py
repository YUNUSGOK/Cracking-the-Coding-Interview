

def onePassSolution(s):
    if len(s) == 0:
        return "" 
    res = ""
    count = 1
    curr = s[0]
    repeatedChar = False
    
    for i in range(1, len(s)):
        if curr == s[i]:
            count += 1
            repeatedChar = True
        else:
            res += curr + str(count)
            curr = s[i]
            count = 1
    
    res += curr + str(count)
    if not repeatedChar:
        res = s 

    return res
