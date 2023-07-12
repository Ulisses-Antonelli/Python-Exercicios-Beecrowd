contador_1 = []
contador_2 = []
for i in range(0, 5):
    num = int(input())
    contador_1.append(num)
for j in contador_1:
    if j % 2 == 0:
        contador_2.append(j)
print(f"{len(contador_2)} valores pares")


