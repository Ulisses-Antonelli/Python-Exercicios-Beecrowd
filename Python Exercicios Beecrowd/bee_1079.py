'''
num_2 = []
num_casos = int(input())

for i in range(1, num_casos + 1):
    for j in range(1, 4):
        num = float(input())
        num_2.append(num)
print(num_2)
'''

num = []
nota_pond = 0

for i in range(1, int(input()) + 1):            # primeiro input determina a quant de ciclos
    lista = list(map(float, input().split()))   # cada input separa os valores por "espaço"
    num.append(lista)                           # cria uma lista de listas
for j in range(0, len(num)):                    #
    nota_pond = (num[j][0] * 2 + num[j][1] * 3 + num[j][2] * 5) / 10   # num[j]     <- det. o index da lista
    print(f"{nota_pond:.1f}")                                                       # num[j][0]  <- det. o index da list da list

'''
n = int(input())

for i in range(1 , n + 1 ):
    x = input().split()
    a,b,c = x
    print('{:.1f}'.format((float (a) * 2 + float(b) * 3 + float(c) * 5) / 10

'''