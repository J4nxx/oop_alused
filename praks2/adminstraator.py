from praks2.kasutajad import Kasutajad
from praks2.privileegid import Privileegid
class Admin(Kasutajad):

    privileegid = Privileegid()


admin = Admin('admin', 'istraator')
admin.privileegid.naita_privileegid()


