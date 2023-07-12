num = int(input())
num_2 = num


def repete(n=num_2):
    for i in range(0, 6):
        print(n)
        n += 2


if num % 2 == 0:
    num_2 = num + 1
    repete()
else:
    repete()
