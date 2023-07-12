contador = []
for i in range(0, 5):
    num = int(input())
    contador.append(num)

par = list(filter(lambda x: x % 2 == 0, contador))
impar = list(filter(lambda x: x % 2 != 0, contador))
positivo = list(filter(lambda x: x > 0, contador))
negativo = list(filter(lambda x: x < 0, contador))

print(f"{par} valor(es) par(es)\n"
      f"{len(impar)} valor(es) impar(es)\n"
      f"{len(positivo)} valor(es) positivo(s)\n"
      f"{len(negativo)} valor(es) negativo(s)")

