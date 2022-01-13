class Restoraan:
    restoraani_nimi = ''
    soogi_tyyp = ''

    def kirjelda_restoraan(self):
        kirj_tekst = self.restoraani_nimi, 'pakub', self.soogi_tyyp
        print(str(kirj_tekst))
    def ava_restoraan(self):
        print(self.restoraani_nimi, 'on avatud.')
