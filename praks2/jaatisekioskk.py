from praks2.jaatisekiosk import JaatiseKiosk
kiosk = JaatiseKiosk("Janre kiosk", "Jaatist")
kiosk.jaatise_valik = "Vaniljejaatis, " + "Šokolaadijaatis, " + "Sidrunijaatis"
kiosk.kirjelda_restoraan()
kiosk.naita_jaatise_valik()