
cobaias = [input().split() for i in range(1, int(input()) + 1)]

C = [int(j) for j, k in cobaias if k == "C" or k == "c"]
R = [int(j) for j, k in cobaias if k == "R" or k == "r"]
S = [int(j) for j, k in cobaias if k == "S" or k == "s"]

print(f"Total: {sum(C + R + S)} cobaias")
print(f"Total de coelhos: {sum(C)}")
print(f"Total de ratos: {sum(R)}")
print(f"Total de sapos: {sum(S)}")
print(f"Percentual de coelhos: {(100 * sum(C)) / sum(C + R + S):.2f} %")
print(f"Percentual de ratos: {(100 * sum(R)) / sum(C + R + S):.2f} %")
print(f"Percentual de sapos: {(100 * sum(S)) / sum(C + R + S):.2f} %")

# i if i > lista_aleatoria[0] else lista_aleatoria.remove(i) for i in lista_aleatoria