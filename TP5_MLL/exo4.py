somme_depart=int(input("Entrez votre salaire :"))

reste = somme_depart

nb_100 = reste // 100
reste = reste % 100

nb_50 = reste // 50
reste = reste % 50

nb_10 = reste // 10
reste = reste % 10

nb_2 = reste // 2
reste = reste % 2

nb_1 = reste // 2
reste = reste % 2

print(f"{somme_depart} euros, c’est donc {nb_100} billets de 100, {nb_50} de 50, {nb_10} de 10, {nb_2} pièces de 2 et {nb_1} pièce 1.")