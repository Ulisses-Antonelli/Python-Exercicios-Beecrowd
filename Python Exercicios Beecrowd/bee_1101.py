lista_intervalo = []

while True:                                       # enquanto verdade
    lista = list(map(int, input().split()))       # input -> separado e tratado -> convertido em list

    if lista[0] <= 0 or lista[1] <= 0:            # se index[0] e index[1] forem menores ou iguais a 0 -> break
        break

    if lista[0] > lista[1]:
        lista[0], lista[1] = lista[1], lista[0]   # troca de posição

    for valor in range(lista[0], lista[1] + 1):   # variavel para o intervalo de index
        print(valor, end=" ")                                       
        lista_intervalo.append(valor)

    print(f"Sum={sum(lista_intervalo)}")
    lista_intervalo = []

