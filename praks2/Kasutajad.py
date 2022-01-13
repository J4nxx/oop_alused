class Kasutajad():
    eesnimi = ""
    perenimi = ""
    email = ""
    vanus = 0

    def kirjelda_kasutaja(self):
        print("Kasutaja eesnimi on {0}, perenimi on {1}, email on {2}, vanus on {3}".format(self.eesnimi, self.perenimi, self.email, self.vanus))

    def tervita_kasutaja(self):
        print("Tervitan kasutajat {0}".format(self.eesnimi))