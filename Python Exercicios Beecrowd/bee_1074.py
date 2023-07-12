num = 0
lista = []
for i in range(1, int(input()) + 1):    # determina a quantidade de ciclos
    num = int(input())                  # entrada dos numeros que serão verificados

    cond = {"ODD NEGATIVE": num % 2 != 0 and num < 0,
            "ODD POSITIVE": num % 2 != 0 and num > 0,
            "EVEN NEGATIVE": num % 2 == 0 and num < 0,
            "EVEN POSITIVE": num % 2 == 0 and num > 0,
            "NULL": num == 0}
    for chave, valor in cond.items():           # laço no dict
        lista.append(chave) if valor else None  # operador ternario - criar uma lista se valor for verdadeiro
for j in lista:                                 # printar valores da lista
    print(j)

'''
lista = ["ODD NEGATIVE", "ODD POSITIVE", "EVEN NEGATIVE", "EVEN POSITIVE", "NULL"]

odd_negative = list(filter(lambda x: n % 2 == 0 and n < 0, lista[0]))
'''





