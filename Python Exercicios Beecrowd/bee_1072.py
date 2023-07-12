a, b = int(input()), int(input())
soma = 0
if a > b:
    b, a = a, b
lista_intervalo = range(a + 1, b)
for i in lista_intervalo:
    if i % 2 != 0:
        soma = soma + i
print(soma)

