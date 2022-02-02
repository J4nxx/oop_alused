from praks2.adminstraator import Admin

admin1 = Admin("Olaf olev", "Alakivi")
admin1.set_andmed(16, "olaf-olev.alakivi@voco.ee")
admin1.kirjelda_kasutaja()
admin1.privileegid = "Lubatud lisada kasutajaid, blokeerida kasutajaid, eemaldada kasutajaid"
admin1.naita_privileegid()
