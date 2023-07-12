a = str(input())
b = str(input())
c = str(input())

lista = {"aguia": ["vertebrado", "ave", "carnivoro"],
         "pomba": ["vertebrado", "ave", "onivoro"],
         "homem": ["vertebrado", "mamifero", "onivoro"],
         "vaca": ["vertebrado", "mamifero", "herbivoro"],
         "pulga": ["invertebrado", "inseto", "hematofago"],
         "lagarta": ["invertebrado", "inseto", "herbivoro"],
         "sanguessuga": ["invertebrado", "anelideo", "hematofago"],
         "minhoca": ["invertebrado", "anelideo", "onivoro"]}

for k, i in lista.items():
    if i[0] == a and i[1] == b and i[2] == c:
        print(k)
