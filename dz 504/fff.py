a = [5,1,4,6,2,3,7,9,8]
res = []
fin = []
for i in range(len(a)-1):
    res.append(a[i])
    k = a[i]
    for j in range(i + 1, len(a)):
        if k+1 in a[j:]:
            tmp = a.index(k+1, j)
            res.append(a[tmp])
            k = a[tmp]
    print (*res)
    res = []
            