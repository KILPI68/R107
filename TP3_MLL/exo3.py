from random import randint

x=randint(0,100)
n=0
c=0



while n != x :
    n = int(input("Entrez votre hypothèse : "))
    c = c+1
    if n == x :
        print("Bravo vous avez trouvé !")
        print(f"Nombre d'essais : {c}")
    elif n > x :
        print("Le chiffre est plus petit")
    elif n < x :
        print("Le chiffre est plus grand")





