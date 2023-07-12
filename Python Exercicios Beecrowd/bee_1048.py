
salario = float(input())
faixa_s = [0, 400, 400.01, 800, 800.01, 1200, 1200.01, 2000]
#          0    1------2     3------4      5------6       7
aumento = [1.15, 1.12, 1.10, 1.07, 1.04]
#          0    1      2     3      4
x, y, z = 0, 1, 0

nsalario = 0
ganhaAumento = False

while not ganhaAumento:

    if salario > 2000:
        nsalario = salario * aumento[4]
        break
    elif salario >= faixa_s[x] and salario <= faixa_s[y]:
        if z == x or z == x - 1 or z == x - 2 or z == x - 3:
            nsalario = salario * aumento[z]
            break
    else:
        x += 2
        y += 2
        z += 1

print(f"Novo salario: {nsalario:.2f}\n"
      f"Reajuste ganho: {nsalario - salario:.2f}\n"
      f"Em percentual: {4 if salario > 2000 else (aumento[z] - 1)*100:.0f} %")







