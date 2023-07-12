
lista = []
while True:
    nota = float(input())
    if 0.0 <= nota <= 10.0:
        lista.append(nota)
        if len(lista) == 2:
            print(f"media = {(lista[0] + lista[1]) /2:.2f}")
            break
    else:
        print("nota invalida")



