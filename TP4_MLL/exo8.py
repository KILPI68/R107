# 5. Création et affichage du dictionnaire pour l'étudiant 1
etudiant1 = {}
etudiant1['firstname'] = 'titi'
etudiant1['name'] = 'toto'
etudiant1['promo'] = 2022
etudiant1['group'] = 202

print(f"votre nom est '{etudiant1['name']}', prénom est '{etudiant1['firstname']}', vous faites")
print(f"partie de la promo '{etudiant1['promo']}' et votre groupe est '{etudiant1['group']}'")

# 6. Affichage avec keys(), values() et items()
print("Les clés du dictionnaire sont :")
for cle in etudiant1.keys():
    print(f"-{cle}")

print("Les valeurs du dictionnaire sont :")
for valeur in etudiant1.values():
    print(f"-{valeur}")

print("Les tuplets du dictionnaire sont :")
for couple in etudiant1.items():
    print(f"-{couple}")

# 7. Ajout du dictionnaire pour l'étudiant 2
etudiant2 = {}
etudiant2['firstname'] = 'tutu'
etudiant2['name'] = 'tata'
etudiant2['promo'] = 2022
etudiant2['group'] = 102

# 8. Création du dictionnaire "binome_dict"
binome_dict = {}
binome_dict[123] = etudiant1
binome_dict[456] = etudiant2

# 9. Affichage des membres du binôme
print("Les étudiants formants le binôme sont :")

for id_poste, etudiant in binome_dict.items():
    nom = etudiant['name']
    prenom = etudiant['firstname']
    groupe = etudiant['group']
    print(f"-{id_poste} L'étudiant {nom} {prenom} du groupe {groupe}")