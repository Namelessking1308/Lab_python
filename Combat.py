import random

def combattre(joueur, ennemi):
    while joueur > 0 and ennemi > 0:
        prepa = input('Souhaitez vous ATTAQUER (1) ou FUIR (2) ?')
        
        if prepa == '1':
            degat = random.randint(20, 30)
            ennemi -= degat
            print('Vous avez infligé -{degat} !')

            if ennemi <= 0:
                print(f'Bien joué, vous l''avez tué !')
                return True

        elif prepa == '2':
            print('Vous avez pris la fuite...')
            return False
          
        degat = random.randint(20, 30)
        joueur -= degat
        print('Vous avez subi -{degat}')



    if joueur <= 0:
        print('Vous êtes mort...')
        return False



