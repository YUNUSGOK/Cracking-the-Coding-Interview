def bruteForce(s):
    for i in range(len(s)):
        for j in range(len(s)):
            if( i != j and s[i] == s[j] ):
                return False
    return True


def hashTableSolution(s):
    charset = [False]*256
    for c in s:
        if(charset[ord(c)]):
            return False
        charset[ord(c)] = True
    return True


