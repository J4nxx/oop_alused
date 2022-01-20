class Restoraan:
    teenindatud_kylastajad = 0
    def __init__(self,restoraani_nimi, soogi_tyyp):
        self.restoraani_nimi = restoraani_nimi
        self.soogi_tyyp = soogi_tyyp
    def kirjelda_restoraan(self):
        kirj_tekst = self.restoraani_nimi + ' pakub ' + self.soogi_tyyp
        print(kirj_tekst)

    def ava_restoraan(self):
        print(self.restoraani_nimi, 'on avatud.')
    def maara_teenindatud_kylalised(self, teenindatud_kylalised):
        self.teenindatud_kylastajad = teenindatud_kylalised
    def suurenda_teenindatud_kylalised(self, suurenda_teenindatud_kylalised):
        self.teenindatud_kylastajad += suurenda_teenindatud_kylalised
