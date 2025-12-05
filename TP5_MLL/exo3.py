entree = input("Entrez un mot ou une phrase :")
entlow=str.lower(entree)
sortie = "".join(c for c in entlow if c.isalpha())
testpal = sortie[::-1]

if testpal == sortie:
    print(f"{entree} est un palindrome !")
else:
    print(f"{entree} n'est pas un palindrome !")




