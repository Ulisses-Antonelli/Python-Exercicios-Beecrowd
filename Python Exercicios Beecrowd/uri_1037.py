# TESTE
#for item in range(101):
#    dados = item

dados = float(input())
intervalo = [0, 25, 50, 75, 100]
#            0   1   2   3   4

if dados >= 0 and dados <= 100:
    for y in intervalo:
        if dados <= y:
            a = intervalo.index(y)
            b = a - 1
            break

    if dados <= 25:
        print(f'Intervalo [0,25]')
    elif dados > 25 and dados <= 100:
        print(f'Intervalo ({intervalo[b]},{intervalo[a]}]')
else:
    print('Fora de intervalo')














