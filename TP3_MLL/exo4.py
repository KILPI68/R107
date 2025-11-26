import sys

def calculer_avec_for(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat

def calculer_avec_while(n):
    resultat = 1
    i = 1
    while i <= n:
        resultat *= i
        i += 1
    return resultat

n = int(input("Entrez un nombre entier positif (n) : "))

if n == 0:
    print(f"\nLe résultat final est : 0! = 1")
    sys.exit()

choix = input("Utiliser 'F' (for) ou 'W' (while) ? ").upper()

if choix == 'F':
    resultat_final = calculer_avec_for(n)

elif choix == 'W':
    resultat_final = calculer_avec_while(n)

else:
    print("F ou W")

print(f"\n Résultat final : {n}! = {resultat_final}")
