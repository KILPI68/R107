def velo_location():
    t_valide = False
    while not t_valide:
        try:
            d = int(input("Donnez l'heure de début de la location: "))
            f = int(input("Donnez l'heure de fin de la location: "))

            if not (0 <= d <= 24 and 0 <= f <= 24):
                print("Les heures doivent être comprises entre 0 et 24")
                continue

            if d == f:
                print("Attention! l'heure de fin est identique à l'heure de début.")
                continue

            if d > f:
                print("Attention! le début de la location est après la fin")
                continue

            t_valide = True
        except ValueError:
            pass

    h1 = 0
    h2 = 0

    for h in range(d, f):
        if (0 <= h < 7) or (17 <= h < 24):
            h1 += 1
        else:
            h2 += 1

    print("\nVous avez loué votre vélo pendant:")

    if h2 > 0:
        print(f"{h2} heures au tarif horaire de 2.0 euros")

    if h1 > 0:
        print(f"{h1} heures au tarif horaire de 1.0 euro")

    total = h1 * 1.0 + h2 * 2.0
    print(f"Le montant total à payer est de {total:.1f} euros.")


velo_location()