

#lista = [input().split() for i in range(1, int(input()) + 1)]

b = []
for i in range(1, int(input()) + 1):
    a = list(map(int, input().split()))
    if a[0] > a[1]:
        a[0], a[1] = a[1], a[0]
    for j in range(a[0] + 1, a[1]):
        if j % 2 != 0:
            b.append(j)
    print(sum(b))
    b = []
    #a = list(map(int, input().split()))




