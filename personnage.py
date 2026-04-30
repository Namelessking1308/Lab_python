# Fonctionnalités à répartir (une par personne) :
# 1. Module Personnage & Stats (branche feature/personnage)
# o Création du joueur (nom, points de vie, inventaire sous forme de liste ou
# dictionnaire)
# o Fonction afficher_stats()

# Auteur Ibrahim

class personnage():
    def __init__(self):
        self.nom = ""
        self.pv = 100
        self.inventaire = []
    
    def stat(self):
        self.nom = input("Entrer un nom: ")

    def afficher_stat(self):
        print(f"Votre Nom: {self.nom}\nPV: {self.pv}\n")
    
p1 = personnage()
p1.stat()
p1.afficher_stat()