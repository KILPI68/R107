L1 = [2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7]
element_plus_frequent = None
max_frequence = 0

for element_courant in L1:
    frequence = 0
    for element_a_comparer in L1:
        if element_courant == element_a_comparer:
            frequence += 1

    if frequence > max_frequence:
        max_frequence = frequence
        element_plus_frequent = element_courant

print("Le nombre le plus frequent dans la liste est le :")
print(f"{element_plus_frequent} ({max_frequence} x)")