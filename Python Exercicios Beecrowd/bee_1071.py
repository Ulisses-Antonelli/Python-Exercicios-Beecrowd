
a, b = int(input()), int(input())
soma = 0
if a > b:
    b, a = a, b
lista_intervalo = range((a + 1), b)
for i in lista_intervalo:
    if i % 2 != 0:
        soma = soma + i
print(soma)

'''
lista_1 = list(range(0, int(input())))
lista_2 = list(range(0, int(input())))

print(lista_2, lista_1)
'''

#resolver o problema de inverter as variaveis