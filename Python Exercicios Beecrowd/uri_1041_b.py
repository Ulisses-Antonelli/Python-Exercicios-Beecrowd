x, y = map(float, input().split())
condicionais = {"Q1": "x > 0 and y > 0",
                "Q2": "x < 0 and y > 0",
                "Q3": "x < 0 and y < 0",
                "Q4": "x > 0 and y < 0",
                "Origem": "x == y == 0",
                "Eixo Y": "x == 0 and y != 0",
                "Eixo X": "y == 0 and x != 0"}
for i, k in condicionais.items():
    if eval(k):
        print(i)
