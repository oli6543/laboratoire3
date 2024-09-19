#Première partie du laboratoire

import random

ranges = (-30,-10,10,30)


for i in range(10):
    led = random.randint(-100, 100)

    if led >= -100 and led <= -30:
        print("couleur" , i + 1 ,  "Bleu")
    elif led >= -29 and led <= -10:
        print("couleur" , i + 1 ,  "Vert")
    elif led >= -9 and led <= 10:
        print("couleur" , i + 1 ,  "Jaune")
    elif led >= 11 and led <= 30:
        print("couleur" , i + 1 ,  "Orange")
    else:
        print("couleur" , i + 1 ,  "Rouge")
