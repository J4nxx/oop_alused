class Konto():
    def __init__(self, nimi , saldo):
        self.__nimi = nimi
        self.__saldo = saldo

    def deposiit(self, kogus):
        if kogus > 0:
            self.__saldo += kogus
    def ylekanne(self, kogus1):
        if kogus1 > 0:
            self.__saldo -= kogus1
        else:
            print("Summa peab olema positiivne!")
    def naita_saldo(self):
        return self.__saldo

    def naita_nimi(self):
        return self.__nimi