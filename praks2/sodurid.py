from praks2.sodur import Sodur
from random import randint

sodur1 = Sodur()
sodur2 = Sodur()

while(sodur1.tervis > 0 and sodur2.tervis > 0):
    kes_loob = randint(1, 2)
    if(kes_loob == 1):
        print("Esimene lööb teist")
        sodur2.tervis -= 20
    if(kes_loob == 2):
        print("Teine lööb esimest")
        sodur1.tervis -= 20

if(sodur1.tervis != 0):
    print("Esimene võitis!")
    print("Teine kaotas!")
else:
    print("Teine võitis!")
    print("Esimene kaotas")
