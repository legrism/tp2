
import random

boucle = True
while boucle:
    borne_minimale = int(input('choisissez un nombre minimal'))
    borne_maximale = int(input('choisissez un nombre maximal.'))
    chiffre = random.randint(borne_minimale, borne_maximale)

    boucle_deviner = True
    compteur_essai = 0
    while boucle_deviner:

        nombre = int(input('essayer de deviner  un chiffre aleatoire entre votre nombre minimal et maximal.'))
        if nombre < chiffre:
            print('Votre chiffre est trop bas, essayez plus haut.')
        elif nombre > chiffre:
            print('Le chiffre que vous avez deviné est trop haut.')
        else:
            print('Vous avez trouvé le bon chiffre, felicitation.')
            print("vous avez réussis en " + str(compteur_essai) + " essais" )
            boucle_deviner= False

        compteur_essai += 1

    rejouer = input("Tu as gagné veux-tu rejouer (oui/non)?")

    if rejouer == 'non':
        boucle= False



