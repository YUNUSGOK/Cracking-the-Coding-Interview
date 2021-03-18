


def layered(arr):
    n = len(arr)

    for l in range(n//2):
        
        for i in range(l, n-l-1):
            last = n - 1 -l 
            first = l
            top = arr[first][i]
            arr[first][i] = arr[last-i][first]
            arr[last-i][first] = arr[last][last-i]
            arr[last][last-i] = arr[i][last]
            arr[i][last] = top


arr = [[1,2,3],[4,5,6],[7,8,9]]
layered(arr)
print(arr)





