
'''
num = []
nota_pond = 0
lista = [list(map(float, input().split())) for i in range(1, int(input()) + 1)]
num.append(lista)
print(lista)
'''


for i in range(1, int(input()) + 1):
    notas = list(map(float, input().split()))
    print(f"{(notas[0] * 2 + notas[1] * 3 + notas[2] * 5) / 10:.1f}")


