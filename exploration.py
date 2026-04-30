# Author : Grégory Cuyle

import random

# Create rooms name and description
def createRooms() : 
    global rooms 
    
    rooms = [
        {"name": "Salle du Temps", "desc": "Cette salle est reliée à une autre dimension où le temps s'écoule différemment. Une minute en dehors de cette salle équivaut à 6 heures dedans, et un jour à une année. Cette salle est utilisée par les combatants pour augmenter leurs potentiels", "exit" : "nord"},
        {"name": "Salle de l'Esprit", "desc": "super salle", "exit" : "sud"},
        {"name": "Salle de la Force", "desc": "super salle", "exit" : "est"},
        {"name": "Salle de l'Âme", "desc": "super salle", "exit" : "ouest"}
    ]


def move(currentRoom) :
    print()

def displayRoom(number) : 
    print(f"Bienvenue dans la salle numéro {number+1}")
    for i in range (rooms[number]["name"].len()) :
        print("=")
    print(rooms[number]["name"])
    for i in range (rooms[number]["name"].len()) :
        print("=")