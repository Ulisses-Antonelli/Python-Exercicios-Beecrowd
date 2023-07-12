X = input().split()

[A, B, C] = map(float, X)

objetos = ['TRIANGULO', 'CIRCULO', 'TRAPEZIO', 'QUADRADO', 'RETANGULO']
calculo = [(A * C) / 2, 3.14159 * (C ** 2), ((A + B) * C / 2), B * B, A * B]

for ID in range(5):
    print(f'{objetos[ID]}: {calculo[ID]:.3f}')






