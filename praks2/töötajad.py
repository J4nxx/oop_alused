class Inimene():
    def __init__(self, eesnimi, perenimi, kutsekvalifikatsioon = 1):
        self.eesnimi = eesnimi
        self.perenimi = perenimi
        self.kutsekvalifikatsioon = kutsekvalifikatsioon
    def __del__(self):
        print("Kõike head!")
    def tutvustus(self):
        print("Tere, olen {0},{1}".format(self.eesnimi, self.perenimi))
