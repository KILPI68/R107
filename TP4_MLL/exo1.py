x=float(input("Entrez votre chiffre:"))
n = 0
list=[]


for i in range(10) :
    print(f"{x} * {n+1} = {round(x * n+1,2)}")
    n=n+1