date_str = input("Entrez une date au format jjmmaaaa : ")

if len(date_str) != 8 or not date_str.isdigit():
    print("La date est incorrecte : Le format doit être jjmmaaaa.")
else:
    jour = int(date_str[0:2])
    mois = int(date_str[2:4])
    annee = int(date_str[4:8])

    date_valide = False

    if annee >= 1:

        est_bissextile = (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

        if 1 <= mois <= 12:

            if mois in [1, 3, 5, 7, 8, 10, 12]:
                jours_max = 31
            elif mois in [4, 6, 9, 11]:
                jours_max = 30
            elif mois == 2:
                jours_max = 29 if est_bissextile else 28

            if 1 <= jour <= jours_max:
                date_valide = True

    if date_valide:
        print("La date est valide.")
    else:
        print("La date est incorrecte.")