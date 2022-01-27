class Inimene():
    jk = 0
    def __int__(self):
        self.id = self.jk + 1
        Inimene.jk = self.jk + 1
    def info(self):
        print("id = {0}".format(self.id))