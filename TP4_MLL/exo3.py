nMax = 4
v1 = []
v2 = []
produit_scalaire = 0

while True:
    n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))
    if 1 <= n <= nMax:
        break
    else:
        print(f"La taille doit ê4tre comprise entre 1 et {nMax}.")

print("Saisie du premier vecteur :")
for i in range(n):
    v = int(input(f"v1[{i}] = "))
    v1.append(v)

print("Saisie du second vecteur :")
for i in range(n):
    v = int(input(f"v2[{i}] = "))
    v2.append(v)

for i in range(n):
    produit_scalaire += v1[i] * v2[i]

print(f"Le produit scalaire de v1 par v2 vaut {produit_scalaire:.1f}")