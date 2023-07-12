x, y = map(float, input().split())

if x > 0 and y > 0:
    A = "Q1"
elif x < 0 and y > 0:
    A = "Q2"
elif x > 0 and y < 0:
    A = "Q4"
elif x < 0 and y < 0:
    A = "Q3"
elif x == y == 0:
    A = "Origem"
elif x == 0 and y != 0:
    A = "Eixo Y"
elif y == 0 and x != 0:
    A = "Eixo X"

print(f'{A}')
