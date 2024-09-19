#Partie 2 du laboratoire avec les LED
import random

ranges = (-30,-10,10,30)
listeBleu = []
listeVert = []
listeJaune = []
listeOrange = []
listeRouge = []


for i in range(100):
    led = random.randint(-100, 100)

    if led >= -100 and led <= -30:
        listeBleu.append(led) 
    elif led > -30 and led <= -10:
        listeVert.append(led)
    elif led > -10 and led <= 10:
        listeJaune.append(led)
    elif led > 10 and led <= 30:
        listeOrange.append(led)
    else:
        listeRouge.append(led)

print("liste bleu:" , listeBleu)
print("liste Vert:" , listeVert)
print("liste Jaune:" , listeJaune)
print("liste Orange:" , listeOrange)
print("liste Rouge:" , listeRouge)
