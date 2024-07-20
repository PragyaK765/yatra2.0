from django.contrib import admin
from  .models import Destination,Detailed_desc,pessanger_detail,Cards,NetBanking,Transactions
# Register your models here.

admin.site.register(Destination)
admin.site.register(Detailed_desc)
admin.site.register(pessanger_detail)
admin.site.register(Cards)
admin.site.register(NetBanking)
admin.site.register(Transactions)



