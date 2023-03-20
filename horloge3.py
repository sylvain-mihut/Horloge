import time

# Définition de la fonction pour afficher l'heure actuelle
def afficher_heure(heure):
    print(f"Heure actuelle: {heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d}", end="\r")

# Définition de la fonction pour régler l'heure
def regler_heure():
    heures = int(input("Entrez l'heure (0-23) : "))
    minutes = int(input("Entrez les minutes (0-59) : "))
    secondes = int(input("Entrez les secondes (0-59) : "))
    heure = (heures, minutes, secondes)
    afficher_heure(heure)
    return heure

# Définition de la fonction pour régler l'heure de l'alarme
def regler_alarme():
    heures = int(input("Entrez l'heure de l'alarme (0-23) : "))
    minutes = int(input("Entrez les minutes de l'alarme (0-59) : "))
    secondes = int(input("Entrez les secondes de l'alarme (0-59) : "))
    heure = (heures, minutes, secondes)
    print(f"Alarme réglée pour {heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d}")
    return heure

# Régler l'heure et l'alarme au début du programme
heure_actuelle = regler_heure()
alarme = regler_alarme()

# Boucle principale du programme
while True:
    afficher_heure(heure_actuelle)  # Affichage de l'heure actuelle
    if heure_actuelle == alarme:  # Si l'heure actuelle correspond à l'heure de l'alarme
        print("L'heure de l'alarme est atteinte !")

    time.sleep(1)  # Pause de 1 seconde
    heure_actuelle = (heure_actuelle[0], heure_actuelle[1], heure_actuelle[2] + 1)  # On ajoute 1 seconde à l'heure actuelle
    if heure_actuelle[2] == 60:  # Si on a dépassé 59 secondes
        heure_actuelle = (heure_actuelle[0], heure_actuelle[1] + 1, 0)  # On ajoute 1 minute et on remet les secondes à zéro
    if heure_actuelle[1] == 60:  # Si on a dépassé 59 minutes
        heure_actuelle = (heure_actuelle[0] + 1, 0, 0)  # On ajoute 1 heure et on remet les minutes et les secondes à zéro
    if heure_actuelle[0] == 24:  # Si on a dépassé 23 heures
        heure_actuelle = (0, 0, 0)  # On remet l'heure à zéro
