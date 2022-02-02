from praks2.kasutajad import Kasutajad
class Admin(Kasutajad):
    privileegid = []

    def naita_privileegid(self):
        print(self.privileegid)