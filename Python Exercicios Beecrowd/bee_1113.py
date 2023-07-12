
while True:                                         # enquanto verdade
    lista = list(map(int, input().split()))         # input -> separação e tratamento -> lista
    if lista[0] == lista[1]:                        # X e Y == encerrar
        break
    print("Decrescente" if lista[0] > lista[1] else "Crescente")
