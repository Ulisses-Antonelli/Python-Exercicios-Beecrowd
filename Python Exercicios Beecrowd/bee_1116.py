# determina a quantidade de ciclos
for i in range(1, int(input()) + 1):
    # input -> separação / tratamento
    lista = list(map(int, input().split()))
    print("divisao impossivel" if lista[1] == 0 else float(lista[0]/lista[1]))

