# exo5.py

jour = int(input("Entrez le jour : "))
heure = int(input("Entrez l'heure : "))
minute = int(input("Entrez les minutes  : "))

duree = (jour - 1) * 24 * 60 + heure * 60 + minute

print(f"Depuis le début du mois, il s'est écoulé {duree} minutes.")
