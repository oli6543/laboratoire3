import random

ranges = (-30,-10,10,30)
listeBleu = {}
listeVert = {}
listeJaune = {}
listeOrange = {}
listeRouge = {}


for i in range(100):
    led = random.randint(-100, 100)

    if led >= -100 and led <= -30:
        if led in listeBleu:
            listeBleu[led] += 1
        else:
            listeBleu[led] = 1 
    elif led > -30 and led <= -10:
        if led in listeVert:
            listeVert[led] += 1
        else:
            listeVert[led] = 1 
    elif led > -10 and led <= 10:
        if led in listeJaune:
            listeJaune[led] += 1
        else:
            listeJaune[led] = 1 
    elif led > 10 and led <= 30:
        if led in listeOrange:
            listeOrange[led] += 1
        else:
            listeOrange[led] = 1 
    else:
        if led in listeRouge:
            listeRouge[led] += 1
        else:
            listeRouge[led] = 1

print("liste bleu:" , listeBleu)
print("liste Vert:" , listeVert)
print("liste Jaune:" , listeJaune)
print("liste Orange:" , listeOrange)
print("liste Rouge:" , listeRouge)