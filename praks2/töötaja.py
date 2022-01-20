from praks2.töötajad import Inimene
töötaja1 = Inimene("Olaf-Olev", "Alakivi", 15)
töötaja2 = Inimene("Ax-Sylvester", "Hommuk", 12)
töötaja3 = Inimene("Viktor", "Lumiste", 10)
töötaja1.tutvustus()
töötaja2.tutvustus()
töötaja3.tutvustus()

if töötaja1.kutsekvalifikatsioon > töötaja2.kutsekvalifikatsioon:
    if töötaja2.kutsekvalifikatsioon > töötaja3.kutsekvalifikatsioon:
        print("Olete vallandatud " + töötaja3.eesnimi + "!" )
        del(töötaja3)
    else:
        del(töötaja2)

elif töötaja1.kutsekvalifikatsioon < töötaja2:
    print("Olete vallandatud " + töötaja1.eesnimi + "!")
    del(töötaja1)


input()