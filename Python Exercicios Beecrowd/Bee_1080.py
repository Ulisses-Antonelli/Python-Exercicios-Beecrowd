'''
import random

# var list[ expressão FOR variavel IN intervalo ]
num_max = [random.randint(1, 10000) for num in range(1, 11)]
print(max(num_max), num_max.index(max(num_max)))
# num_max = [i if i > lista_aleatoria[0] else lista_aleatoria.remove(i) for i in lista_aleatoria]
'''

lista = [int(input()) for i in range(1, 101)]
print(max(lista))
print(lista.index(max(lista)) + 1)
