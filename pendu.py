#########################
####### fonctions #######
#########################
def ligne_bas():
    print('*' * 18)
    to_return = ''
    return to_return


def ligne_haut():
    print(' '*5, '*' * 13)
    to_return = ''
    return to_return


def diago_1():
    esp = 1
    for j in range(1, 3):
        print(' '*5, '*', ' ' * esp, '*')
        esp -= 1
    to_return = ''
    return to_return


def ligne_2():
    esp = 1
    esp_plus = 2
    for j in range(1, 3):
        print(' '*5, '*', ' ' * esp, '*', ' '*esp_plus, '*')
        esp -= 1
        esp_plus += 1
    to_return = ''
    return to_return


def ligne_horizon(rest):
    to_draw = 0 + rest
    for i in range(to_draw, 19):
        print(' '*5, '*')
    to_return = ''
    return to_return


def tete():
    print(' '*5, '*', ' '*5, '*'*3)
    print(' '*5, '*', ' '*3, '', '*', ' ',  '*')
    print(' '*5, '*', ' '*3, '', '*', ' ', '*')
    print(' '*5, '*', ' '*5, '*'*3)
    to_return = ''
    return to_return


def body():
    for i in range(8, 13):
        print(' '*5, '*', ' '*5, '', '*')
    to_return = ''
    return to_return


def body_arm_1():
    esp = 0
    esp_debut = 2
    print(' '*5, '*', ' '*5, '', '*')
    for i in range(9, 12):
        print(' '*5, '*', ' '*esp_debut, '', '*', ' '*esp, '*')
        esp += 1
        esp_debut -= 1
    print(' '*5, '*', ' '*5, '', '*')
    to_return = ''
    return to_return


def body_arm_2():
    esp = 0
    esp_debut = 2
    print(' '*5, '*', ' '*5, '', '*')
    for i in range(9, 12):
        print(' '*5, '*', ' '*esp_debut, '', '*', ' '*esp, '*', ' '*esp, '*')
        esp += 1
        esp_debut -= 1
    print(' '*5, '*', ' '*5, '', '*')
    to_return = ''
    return to_return


def body_leg_1():
    for i in range(14, 18):
        print(' '*5, '*', ' '*3, '', '*')
    to_return = ''
    return to_return


def body_leg_2():
    for i in range(14, 18):
        print(' '*5, '*', ' '*4, '', '*',  '*')
    to_return = ''
    return to_return


def draw_pendu(number_try):
    rest = 0
    if number_try == 1:
        for i in range(0, 19):
            print()
        print(ligne_bas())

    elif number_try == 2:
        print(ligne_horizon(rest), ligne_bas())

    elif number_try == 3:
        print(ligne_haut(), ligne_horizon(rest), ligne_bas())

    elif number_try == 4:
        rest = 2
        print(ligne_haut(), diago_1(), ligne_horizon(rest), ligne_bas())

    elif number_try == 5:
        rest = 4
        print(ligne_haut(), ligne_2(), ligne_horizon(rest), ligne_bas())

    elif number_try == 6:
        rest = 7
        print(ligne_haut(), ligne_2(), tete(),
              ligne_horizon(rest), ligne_bas())

    elif number_try == 7:
        rest = 13
        print(ligne_haut(), ligne_2(), tete(), body(),
              ligne_horizon(rest), ligne_bas(), '')

    elif number_try == 8:
        rest = 13
        print(ligne_haut(), ligne_2(), tete(), body_arm_1(),
              ligne_horizon(rest), ligne_bas(), '')

    elif number_try == 9:
        rest = 13
        print(ligne_haut(), ligne_2(), tete(), body_arm_2(),
              ligne_horizon(rest), ligne_bas(), '')

    elif number_try == 10:
        rest = 18
        print(ligne_haut(), ligne_2(), tete(), body_arm_2(),
              body_leg_1(), ligne_horizon(rest), ligne_bas(), '')

    elif number_try == 11:
        rest = 18
        print(ligne_haut(), ligne_2(), tete(), body_arm_2(),
              body_leg_2(), ligne_horizon(rest), ligne_bas(), '')
    to_return = ''
    return to_return

#########################
#### algo principal #####
#########################


replay = 'oui'
print('Hey! C\'est le jeu du pendu. Trouve un ami pour jouer avec toi ou mange un curly.')
print('')
while replay == 'oui':
    joueur_1 = input(
        'Joueur 1 entre ton nom, c\'est toi qui va choisir le mot. ')
    joueur_2 = input(
        'Joueur 2 entre ton nom, c\'est toi qui devra trouver le mot de le mot. ')
    print(joueur_1, 'entre un mot et', joueur_2, 'ferme les yeux')
    word = input('')
    print('Maintenant,', joueur_1, 'entre un signe pour cacher ton mot')
    signe = input('')
    for line in range(0, 50):
        print((signe+' ') * 10)
    print('')
    size_word = len(word)
    number_try = 10
    good_chaine = []
    word_find = False
    for index in range(0, size_word):
        good_chaine.append(word[index])
    result = []
    letter_used = []
    for index in range(0, size_word):
        result.append('_ ')
    print(result)
    print('Il y a', size_word, 'lettres à trouver')
    while number_try != 11 and word_find == False:
        have_result = True
        is_letter = False
        print('Tu as encore', number_try, 'essais')
        letter = input('Entrez une lettre: ')
        letter_used.append(letter)
        print('')
        for l in range(0, size_word):
            if letter == word[l]:
                print('Bravo tu as trouvé une lettre')
                result[l] = letter
                print(result)
                is_letter = True
            else:
                have_result = False
        if have_result == False and is_letter == False:
            print('Cette lettre n\'est pas dans mon mot')
            number_try -= 1
            print(draw_pendu(number_try))
            print(result)
        print('Tu as utilisé toutes ces lettres:', letter_used)

        if good_chaine == result:
            word_find = True
            print('BRAVO,', joueur_2, '! Tu as trouvé le mot de', joueur_1)
    if number_try == 0:
        print('Oh non', joueur_2, 'tu n\'as pas réussi à trouver le mot de', joueur_1)
        print('Le mot était', word)
    print('')
    print('Voulez vous rejouer?')
    replay = input('')
if replay == 'non':
    print('Merci d\'avoir jouer à mon jeu, au revoir')
