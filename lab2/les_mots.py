liste_mot = [""]
check = 0

while(True):
    mot = input("Entrer un mot:")

    if (liste_mot[0] == ""):
        print(mot,"n'est pas dans la liste")
        liste_mot.append(mot)
        liste_mot.pop(0) 
    else:
        if(mot == "Affiche"):
            for liste in liste_mot:
                print(liste)
        else:
            for liste in liste_mot:
                if (liste == mot):
                    print(mot,"est dans la liste")
                    check = 1
                    break
            if(check == 0):
                print(mot,"n'est pas dans la liste")
                liste_mot.append(mot)
            check = 0