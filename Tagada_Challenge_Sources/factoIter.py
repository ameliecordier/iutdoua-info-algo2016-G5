def factoIter(n):
    '''
    Adaptation de facto pour étudier les problèmes de place mémoire avec cProfile
    '''
    res = 1
    i = 1
    tab = []
    while i <= n:
        res = res*i
        i = i+1
        for j in range(res):
            tab.append(res)
    return res

print(factoIter(10))
