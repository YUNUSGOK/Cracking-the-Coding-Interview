



def onePassSolution(s1, s2):
    delta = abs(len(s1) - len(s2))
    bigger = len(s1) > len(s2)
    i, j = 0, 0
    diff = 0
    if delta > 1: 
        return False

    while(i < len(s1) and j < len(s2)):
        if (s1[i] ==  s2[j]):
            i += 1
            j += 1
            continue
        diff += 1
        if delta == 0:
            i += 1
            j += 1

        else:
            if bigger:
                i += 1
            else: 
                j +=1
        if diff > 1:
            return False
    return True
                