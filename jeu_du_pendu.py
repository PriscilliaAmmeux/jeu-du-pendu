mot = "python"

print("Bienvenue dans le jeu du Pendu ! Vous avez 7 tentatives pour deviner un mot secret. Ce mot comporte 5 lettres. Bonne chance !")
proposition = ""
tentatives = 1
while tentatives <= 7:
    proposition = input("Tentative numéro "+str(tentatives)+" : ")
    if proposition == mot:
        print("Bien joué ! Vous avez gagné !")
        break
    else:
        print("Raté !")
    tentatives = tentatives + 1
print("Fin de la partie")