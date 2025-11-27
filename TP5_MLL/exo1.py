nom1=input("Entrez le premier nom:")
prenom1=input("Entrez le premier prénom:")
nom2=input("Entrez le deuxième nom:")
prenom2=input("Entrez le deuxième prénom:")



if nom1 < nom2 :
    print(f"{str.capitalize(prenom1)} {str.upper(nom1)}")
    print(f"{str.capitalize(prenom2)} {str.upper(nom2)}")
else :
    print(f"{str.capitalize(prenom2)} {str.upper(nom2)}")
    print(f"{str.capitalize(prenom1)} {str.upper(nom1)}")
