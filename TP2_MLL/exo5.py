nbent=int(input(f"Entrez un nombre entier : "))

if nbent > 0 :
    if nbent %2 == 0 :
        print("Le nombre est positif et pair")
    else :
        print("Le nombre est positif et impair")
elif nbent < 0 :
    if nbent % 2 == 0:
        print("Le nombre est négatif et pair")
    else:
        print("Le nombre est négatif et impair")
elif nbent == 0 :
    print("Le nombre est zéro et il est pair")