"""Moodul sisaldab Andmed, Opetaja ja Opilane klasse"""
from random import randint
class Andmed:
    """Andmed klass, teeb listi kuhu lisab kõik teemad."""
    def __init__(self, *info):
        self.info = list(info)
    def __getitem__(self, i ):
        """"""
        return self.info[i]

class Opetaja:
    """Opetaja klass lisab opilastele teemasi listist."""
    def opetab(self, info, *opilane):
        """Opetab meetod kutsub esile opilane opib meetodi iga opilase objektiga, kes seda teemat opib."""
        for i in opilane:
            i.opib(info)
class Opilane:
    """Opilane klass lisab või eemaldab teemasi opilaste teadmistes."""
    def __init__(self):
        self.teadmised = []
    def opib(self, info):
        """Lisab opilane teadmised listi teemad."""
        self.teadmised.append(info)
    def ise_opib(self, info):
        """Ise_opib meetod lisab teema ilma opetaja klassi kasutamatta."""
        self.teadmised.append(info)
    def unustamine(self):
        """Unusutamine meetob juhuslikult eemaldab ühe teema opilaste teadmistest."""
        voimalus = randint(1,10)
        if voimalus <=5:
            self.teadmised.pop(randint(0,len(self.teadmised)-1))
        else:
            pass