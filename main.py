
import random

boucle = True
while boucle:
    chiffre = random.randint (1,10)


    boucle_deviner = True
    while boucle_deviner:
        nombre = int(input('essayer de deviner  un chiffre de 1 a 10.'))
        if nombre < chiffre:
            print('Votre chiffre est trop bas, essayez plus haut.')

        elif nombre > chiffre:
            print('Le chiffre que vous avez deviné est trop haut.')

        else:
            print('Vous avez trouvé le bon chiffre, felicitation.')
            boucle_deviner= False

    rejouer = input("Tu as gagné veux-tu rejouer (oui/non)?")

    if rejouer == 'non':
        boucle= False



