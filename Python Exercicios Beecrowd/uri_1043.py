A, B, C = map(float, input().split())
if (A + B <= C) or (B + C <= A) or (C + A <= B):
    print(f'Area = {(((A + B) * C)/ 2):.1f}')
else:
    print(f'Perimetro = {A + B + C:.1f}')
