salario = float(input())
faixa = {0.28: [4500.01, salario], 0.18: [3000.01, 4500.00], 0.08: [2000.01, 3000.00]}

c = 0
for i, k in faixa.items():
    if salario >= k[0] and salario <= k[1]:
        a = salario - (k[0] - 0.01)
        salario = abs(a - salario)
        b = a * i
        c = c + b
if salario < 2000.00:
    print(f"Isento")
else:
    print(f"R$ {c:.2f}")
