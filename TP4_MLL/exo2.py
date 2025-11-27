nombreEtudiants = int(input("Donnez le nombre d'etudiants: "))
moyenne = 0.0;
notes = []
somme_notes = 0.0

for i in range(nombreEtudiants):
    while True:
        note = float(input(f"Note etudiant {i} : "))
        if 0.0 <= note <= 20.0:
            notes.append(note)
            somme_notes += note
            break
        else:
            print("La note doit être comprise entre 0 et 20, redonnez la :")

moyenne = somme_notes / nombreEtudiants

print(f"Moyenne de classe: {moyenne:.2f}")

print("Numéro de l'Etudiant | note | ecart a la moyenne")
for i in range(nombreEtudiants):
    ecart = notes[i] - moyenne
    print(f"{i} | {notes[i]:.1f} | {ecart:.2f}")