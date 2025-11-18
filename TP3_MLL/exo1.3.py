valeurs = []
while len(valeurs) < 10:
    v = float(input("Entrez une valeur entre 0 et 20 : "))
    if 0 <= v <= 20:
        valeurs.append(v)

inf_15 = sum(1 for v in valeurs if v < 15)
sup_ou_egal_15 = sum(1 for v in valeurs if v >= 15)
sup_ou_egal_10 = sum(1 for v in valeurs if v >= 10)

print("Valeurs < 15 :", inf_15)
print("Valeurs ≥ 15 :", sup_ou_egal_15)
print("Valeurs ≥ 10 :", sup_ou_egal_10)

