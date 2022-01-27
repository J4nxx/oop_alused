from praks2.sodur import Sodur
from random import randint

armee1 = []
armee1_id = []
armee2 = []
armee2_id= []
for i in range(1, 21):
    armee_valik = randint(1,2)
    if armee_valik == 1:
        armee1.append(Sodur(armee_valik))
    else:
        armee2.append(Sodur(armee_valik))
for sodur in armee1:
    armee1_id.append(sodur.id)
for sodur in armee2:
    armee2_id.append(sodur.id)
print("Esimeses armees on sodurid id'ga: " + ', '.join(map(armee1_id)))
print("Teises armees on sodurid id'ga: " + ', '.join(map(armee2_id)))