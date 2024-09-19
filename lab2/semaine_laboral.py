#Ce programme identifie le jour de la semaine selon un nombre
jours_semaine = "Dimanche","Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi"

semaine_laboral = "Lundi","Mardi","Mercredi","Jeudi","Vendredi"

jour = int(input("Entrer un nombre: "))

print("Jour de la semaine",jours_semaine[jour])

if jour >= 5:
    print("Jour ouvrable de la semaine:",semaine_laboral [0])
else:
    print("Jour ouvrable de la semaine:",semaine_laboral [jour])
