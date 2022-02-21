from praks2.kool.oppimine import *
# Loome objekti "teemad" kasutades "Andmed" klassi.
teemad = Andmed("klass", "objekt", "pärilus", "polümorfism", "kapseldus")
# Loome objekti "anna" kasutades "Opetaja" klassi.
anna = Opetaja()
# Loome objekti "kadi" kasutades "Opilane" klassi.
kadi = Opilane()
# Loome objekti "mati" kasutades "Opilane" klassi.
mati = Opilane()
# Kutsume esile anna "opetab" meetodi.
anna.opetab(teemad[4], kadi, mati)
anna.opetab(teemad[2], kadi)
# Kutsume esile "mati" "ise_opib" meetodi.
mati.ise_opib(teemad[3])
# Prindime välja õpilaste teadmised
print("Mati oskab jargmisi teemasi: ", mati.teadmised)
print("Kadi oskab jargmisi teemasi: ", kadi.teadmised)
# Kutsume esile õpilaste "unustamine" meetodi.
mati.unustamine()
kadi.unustamine()
# Prindime uuesti välja õpilaste teadmised, juhul kui neil läks midagi meelest magamise ajal.
print("Matil ules argates meenus(id) ainult need teemad: ", mati.teadmised)
print("Kadil ules argates meenus(id) ainult need teemad: ", kadi.teadmised)