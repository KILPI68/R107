nombre = float(input("Vous cherchez la table de multiplication de quel nombre ? "))
resultats = []

for i in range(10):
    resultat = nombre * i
    resultat_arrondi = round(resultat, 1)
    resultats.append(resultat_arrondi)

for i in range(10):
    print(f"{nombre:.1f}*{i}={resultats[i]:.1f}")