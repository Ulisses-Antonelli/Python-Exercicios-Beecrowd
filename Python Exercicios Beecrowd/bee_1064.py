a = 0
contador = []
for i in range(0, 6):
    num = float(input())
    if num > 0.0:
        contador.append(num)
for j in contador:
    a = j + a
media = a / len(contador)

print(f"{len(contador)} valores positivos\n"
      f"{media:.1f}")
