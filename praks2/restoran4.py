from praks2.restoran3 import Restoraan
restoraan1 = Restoraan("Olafi Resto", "Su ema spagette")
restoraan1.kirjelda_restoraan()
restoraan1.ava_restoraan()
print(restoraan1.teenindatud_kylastajad)
restoraan1.maara_teenindatud_kylalised(5)
print(restoraan1.teenindatud_kylastajad)
restoraan1.suurenda_teenindatud_kylalised(15)
print(restoraan1.teenindatud_kylastajad)