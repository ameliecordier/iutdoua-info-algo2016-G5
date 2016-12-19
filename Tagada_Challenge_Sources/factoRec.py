def factoRec(n):
    if n <= 1:
        return 1
    else:
        return n*factoRec(n-1)

print(factoRec(500))
