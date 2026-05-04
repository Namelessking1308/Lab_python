# Hauteur : Amon(Deawoz)
def afficherInventaire(inventaire):
    print(inventaire)


def Ramasser(inventaire):

    Choix = input("Appuyer sur 'F' pour ramasser\n").lower()

    if Choix == 'f':

        for i ,element in enumerate(inventaire):

            if element == 0:

                inventaire[i] = "objet"
                break
         
        else: 
            print("plus de place")


def devinette (rep):
     sec = 0
     while sec != 1:
        rep = input("Comment le deuxieme fils de Razor Back s'appelle apres avoir atteint le niveau max sur strangar").lower

        if rep == "la mer noir":
          print("DING DING DINNNG, bonne reponse!!!")
          sec += 1

        else:
           print("Mauvaise reponse... tu cherches trop loin")
          





