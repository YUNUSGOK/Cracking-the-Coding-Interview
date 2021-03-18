


def layered(arr):
    n = len(arr)

    if n > 1:
        m = len(arr[0])
        if n != m:
            return
    else:
        return
    for l in range(n//2):
        
        for i in range(l, n-l-1):
            last = n - 1 -l 
            first = l
            top = arr[first][i]
            arr[first][i] = arr[last-i][first]
            arr[last-i][first] = arr[last][last-i]
            arr[last][last-i] = arr[i][last]
            arr[i][last] = top








