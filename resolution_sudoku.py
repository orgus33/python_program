L = [[0, 9, 0, 2, 0, 0, 6, 0, 5],
     [3, 2, 0, 0, 0, 7, 0, 0, 0],
     [0, 7, 0, 9, 0, 5, 0, 0, 8],
     [0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 7, 0, 0, 0, 0, 9, 4],
     [6, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 8, 0, 0, 0, 0, 0, 7],
     [0, 3, 0, 4, 9, 1, 5, 0, 0],
     [0, 0, 0, 0, 0, 3, 0, 0, 0]]


def chiffres_ligne(L, i):
    chiffres = []
    for chiffre in L[i]:
        if chiffre != 0:
            chiffres.append(chiffre)
    return chiffres

# print(chiffres_ligne(L, 0))


def chiffres_colonne(L, j):
    chiffres = []
    for index in range(len(L)):
        if L[index][j] != 0:
            chiffres.append(L[index][j])
    return chiffres

# print(chiffres_colonne(L, 0))


def chiffres_bloc(L, i, j):
    chiffres = []
    for index in range(0, 6):
        print(index)

print(chiffres_bloc(L, 4, 7))
