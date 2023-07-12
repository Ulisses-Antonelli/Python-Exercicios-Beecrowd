lista = list(map(int, input().split())) #tratamento de tipo de dados( string = ordem incorreta )
lista_ordenada = sorted(lista) + lista
lista_ordenada[3:3] = [""]
for i in lista_ordenada:
    print(i)



#N4, N5, N6 = sorted(lista, reverse=True)