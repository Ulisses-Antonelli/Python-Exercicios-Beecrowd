while True:
    pos = list(map(int, input().split()))                   # input -> separação -> tratamento -> list
    if pos[0] == 0 or pos[1] == 0:                          # se == 0 -> interromper
        break
    quadrante = {"primeiro": pos[0] > 0 and pos[1] > 0,     # chave: valor
                 "segundo": pos[0] < 0 and pos[1] > 0,
                 "terceiro": pos[0] < 0 and pos[1] < 0,
                 "quarto": pos[0] > 0 and pos[1] < 0}
    for chave, valor in quadrante.items():                  # loop chave: valor
        if valor:                                           # se True
            print(chave)


