
lista, n = [], None
while True:
    nota = float(input())
    if 0.0 <= nota <= 10.0:
        lista.append(nota)
        if len(lista) == 2:
            print(f"media = {(lista[0] + lista[1]) /2:.2f}")
            while n not in range(1, 3):
                #  print("novo calculo (1-sim 2-nao)")
                n = int(input("novo calculo (1-sim 2-nao) "))
            if n == 2:
                break
            else:
                lista, n = [], None
    else:
        print("nota invalida")






