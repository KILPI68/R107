X = int(input("Entrez la valeur X : "))
somme = 0
N = 0
while somme < X:
    somme += N
    N += 1

if somme == X:
    print("Le nombre N recherché est :", N - 1)
else:
    print("Aucun N ne donne une somme exacte de", X)

