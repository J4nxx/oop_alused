from praks2.restoran3 import Restoraan
class JaatiseKiosk(Restoraan):
    jaatise_valik = ""
    def naita_jaatise_valik(self):
        print(self.jaatise_valik)
