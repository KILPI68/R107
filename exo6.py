# exo6.py

minutes = int(input("entrez le nombre de minutes voulues:"))

jour = minutes // (24 * 60)
reste = minutes % (24 * 60)
heure = reste // 60
minute = reste % 60

print(f"Date : {jour + 1}, {heure} h {minute} min")
