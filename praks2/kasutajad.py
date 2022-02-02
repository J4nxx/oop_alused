class Kasutajad():
    def __init__(self, eesnimi, perenimi, sisse_katse = 0):
        self.eesnimi = eesnimi
        self.perenimi = perenimi
        self.sisselogkatse = sisse_katse

    def set_andmed(self, age, mail):
        self.mail = mail
        self.vanus = age

    def kirjelda_kasutaja(self):
        print("Kasutaja eesnimi on {0}, perenimi on {1},mail on {2}, vanus on {3}".format(self.eesnimi, self.perenimi, self.vanus, self.mail))

    def tervita_kasutaja(self):
        print("Tervitan kasutajat {0}".format(self.eesnimi))