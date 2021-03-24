


def stringRotation(s1,s2):
    conc = s1 + s1
    if len(s1) == len(s2) and len(s1) > 0:
        return s2 in conc
    return False
