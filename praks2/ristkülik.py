from random import randint
class Ristkülik():
    def __init__(self, laius, kõrgus, sümbol):
        self.laius = (laius)
        self.kõrgus = (kõrgus)
        self.sümbol = (sümbol)
    def __str__(self):
        ruut = []
        for i in range(self.kõrgus):
            ruut.append(self.sümbol * self.laius)
        ruut = '\n'. join(ruut)
        return ruut
    def __add__(self, other):
        laius = self.laius + other.laius
        kõrgus = self.kõrgus + self.kõrgus
        random = randint(1, 2)
        if random == 1:
            sümbol = self.sümbol
        else:
            sümbol = other.sümbol
        kujund = Ristkülik(laius, kõrgus, sümbol)
        return (kujund)
kujund1 = Ristkülik(10, 3, "*")
kujund2 = Ristkülik(8, 3, "z")
print(kujund1 + kujund2)