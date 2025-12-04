notes = []
coefficients = []

for i in range(5):
    saisie = input(f"Note {i + 1} et Coef (Ex: 10.5 2) : ").split()

    note = float(saisie[0])
    coef = int(saisie[1])

    notes.append(note)
    coefficients.append(coef)

somme_produits = 0
somme_coefficients = 0

for note, coef in zip(notes, coefficients):
    somme_produits += note * coef
    somme_coefficients += coef

moyenne = somme_produits / somme_coefficients

admis_moyenne = moyenne > 10
admis_note_min = True

for note in notes:
    if note < 8:
        admis_note_min = False
        break

print(f"\nMoyenne : {moyenne:.2f}")

if admis_moyenne and admis_note_min:
    print("ADMIS")
else:
    print("NON ADMIS")