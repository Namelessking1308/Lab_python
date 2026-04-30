# Author : Grégory Cuyle

import random

# Create rooms name and description
def createRooms() : 
    global rooms 
    
    rooms = [
        {"name": "Salle du Temps", "desc": "Cette salle est reliée à une autre dimension où le temps s'écoule différemment. Une minute en dehors de cette salle équivaut à 6 heures dedans, et un jour à une année. Cette salle est utilisée par les combatants pour augmenter leurs potentiels", "exit" : "nord"},
        {"name": "Salle de l'Esprit", "desc": "Ici, les grands esprits se rencontrent pour une bataille mentale", "exit" : "sud"},
        {"name": "Salle de la Force", "desc": "Ici la gravité est 10x supérieure à la normale. Cette salle est utilisée pour augmenter leur force", "exit" : "est"},
        {"name": "Salle de l'Âme", "desc": "Si votre âme est pure, vous survivrez à cette salle. Sinon, malédiction à vous.", "exit" : "ouest"}
    ]

# Change current room
def moveRoom(currentRoom, direction) :

    if(direction == rooms[currentRoom]["exit"]) :
        print(f"Vous vous dirigez dans la direction {direction}. Vous voyez la sortie et sortez de la salle.")

        newRoom = random.randint(0, 3)
        while( newRoom == currentRoom):
            newRoom = random.randint(0, 3)
    else :
        print("Vous ne voyez pas la sortie ...")
    

# Display room details
def displayRoom(number) : 
    #Welcome
    print(f"Bienvenue dans la salle numéro {number+1} !\n")
    #Name
    for i in range (len(rooms[number]["name"])) :
        print("=",end="")
    print("\n"+rooms[number]["name"])
    for i in range (len(rooms[number]["name"])) :
        print("=",end="")
    #Desc
    print("\n\nDescription : "+rooms[number]["desc"])