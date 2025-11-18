BASE = 1
fromage = 200.0
eau = 0.5
ail = 0.5
pain = 100

nbConvives=int(input("Entrez le nombre de personne(s) conviées à la fondue :"))

nvfro = fromage * nbConvives
nveau = eau * nbConvives
nvail = ail * nbConvives
nvpai = pain * nbConvives

print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut :\n-{nvfro} gr de fromage\n-{nveau} dl d'eau\n-{nvail} gousses d'ail\n-{nvpai} gr de pain")


