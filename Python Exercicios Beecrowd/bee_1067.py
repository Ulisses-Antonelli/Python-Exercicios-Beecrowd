
num = int(input())
if num >= 1 and num <= 1000:
    for i in range(1, num + 1):
        if i % 2 != 0:
            print(i)
