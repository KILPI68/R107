tab = [5, 2, 4, 8, 1, 3]

print(tab)

n = len(tab)
for i in range(n):

    index_min = i
    for j in range(i + 1, n):
        if tab[j] < tab[index_min]:
            index_min = j

    if index_min != i:
        tab[i], tab[index_min] = tab[index_min], tab[i]

    print(tab)