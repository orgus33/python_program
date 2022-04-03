def addition(liste1, liste2):
    liste = []
    for i in range(0, len(liste1)):
        liste.append((liste1[i] + liste2[i]) % 100)
    return liste


def est_plus_petit(liste_min, liste_max):
    for i in range(len(liste_max)):
        if liste_min[i] > liste_max[i]:
            return False
    return True


def chaine_vers_liste(chaine):
    liste = []
    for character in chaine:
        liste.append(ord(character) % 100)

    if len(liste) % 6 != 0:
        while len(liste) % 6 != 0:
            liste.insert(0, 0)

    return liste


def un_tour(bloc):

    # Etape 1 :
    for i in range(0, len(bloc)-1, 2):
        bloc[i+1] = bloc[i] + bloc[i+1]

    # Etape 2 :
    n = 7
    for i in range(0, len(bloc)-1, 2):
        bloc[i] = (bloc[i] * n) + 1
        n += 4
        bloc[i+1] = (bloc[i+1] * n) + 1
        n += 2

    # Etape 3 :
    n = bloc[-1]
    del bloc[-1]
    bloc.insert(0, n)

    # Etape 4 :
    for i in range(len(bloc)):
        bloc[i] %= 100

    return bloc


def dix_tours(bloc):
    for i in range(0, 10):

        # Etape 1 :
        for i in range(0, len(bloc)-1, 2):
            bloc[i+1] = bloc[i] + bloc[i+1]

        # Etape 2 :
        n = 7
        for i in range(0, len(bloc)-1, 2):
            bloc[i] = (bloc[i] * n) + 1
            n += 4
            bloc[i+1] = (bloc[i+1] * n) + 1
            n += 2

        # Etape 3 :
        n = bloc[-1]
        del bloc[-1]
        bloc.insert(0, n)

        # Etape 4 :
        for i in range(len(bloc)):
            bloc[i] = bloc[i] % 100

    return bloc


def hachage(liste):
    while len(liste) > 6:
        b1 = liste[0:6]
        b2 = liste[6:12]

        b1 = dix_tours(b1)

        b1 = addition(b1, b2)

        liste[0:12] = b1

    liste = dix_tours(liste)

    return liste


def verification_preuve_de_travail(liste, preuve):
    return est_plus_petit(hachage(liste + preuve), [0, 0, 5])


def preuve_de_travail(liste):
    preuve = [97, 49, 93, 87, 89, 47]
    i = len(liste)-1
    while verification_preuve_de_travail(liste, preuve) != True:
        if liste[i] < 99:
            liste[i] += 1
        elif liste[i] == 99:
            i -= 1
            preuve[i] += 1
        if i < 0:
            return None
    return preuve


def ajout_transaction(transaction):

    global Livre
    Livre += [transaction]
    return Livre


Livre = [[0, 0, 0, 0, 0, 0]]


print(ajout_transaction("Camille +100"))


def minage():
    last_trans = Livre[len(Livre)-1]
    liste_trans = chaine_vers_liste(last_trans)
    prec_preuve = Livre[len(Livre)-2]
    liste = [prec_preuve + liste_trans]
    print(liste)
    preuve_liste = preuve_de_travail(liste)
    Livre.insert(preuve_liste)


print(minage())
