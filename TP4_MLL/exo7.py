binome = ('login1', 'login2')
print(f"L'étudiant {binome[0]} est en binome avec l'étudiant {binome[1]}")

print("Que constatez-vous ? Les tuplets ne sont pas modifiables (mutables).")

print("Que constatez-vous ? On ne peut pas supprimer un élément d'un tuplet avec del().")

trinome_login = 'login3'
trinome = binome + (trinome_login,)
print(trinome)
print("Que pouvez-vous en conclure sur les tuplet ?")
print("Les tuplets sont immuables (non modifiables après leur création). Ils sont utilisés pour stocker des données qui ne doivent pas changer.")