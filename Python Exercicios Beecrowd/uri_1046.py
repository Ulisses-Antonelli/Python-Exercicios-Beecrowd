'''
h_inicial, h_final = map(int, input().split())

if h_inicial >= h_final:
    h_c = abs(h_inicial - 24) + h_final
else:
    h_c = abs(h_inicial - h_final)

print(f"O JOGO DUROU {h_c} HORA(S)")

'''

horas = list(range(0, 24))
x = 2
x = horas[x % len(horas)]
print(x)

