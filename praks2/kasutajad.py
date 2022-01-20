class Kasutajad():
    def __init__(self, eesnimi, perenimi):
        self.eesnimi = eesnimi
        self.perenimi = perenimi

    def maara_kasutajanimi(self, kasutajanimi):
        self.kasutajanimi = kasutajanimi

    def maara_parool(self, parool):
        self.parool = parool

    def maara_vanus(self, vanus):
        self.vanus = vanus

    def maara_gmail(self, gmail):
        self.gmail = gmail
    def kirjelda_kasutaja(self):
        print("Kasutaja eesnimi on {0}, perenimi on {1}, parool on {2}, vanus on {3}, gmail on {4}".format(self.eesnimi, self.perenimi, self.parool, self.vanus, self.gmail))

    def tervita_kasutaja(self):
        print("Tervitan kasutajat {0}".format(self.eesnimi))