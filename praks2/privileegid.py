class Privileegid():
    def __init__(self):
        self.privileegid = ["Lubatud lisada kasutajaid, ", "Lubatud eemaldada kasutajaid, ", "Lubatud blokeerida kasutajaid"]

    def naita_privileegid(self):
        for privileeg in self.privileegid:
            print('- ' + privileeg)

