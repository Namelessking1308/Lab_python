import random

def combattre(joueur, ennemi):
    while joueur > 0 and ennemi > 0:
        joueur_commence = True
        degat = random.randint(20, 30)
        
        print()

        if ennemi == 0:
            print('Ennemi tué !')



