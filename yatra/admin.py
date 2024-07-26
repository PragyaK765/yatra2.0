from django.contrib import admin
from  .models import Destination,Detailed_desc, pessanger_detail, Khalti_details, Transactions
# Register your models here.

admin.site.register(Destination)
admin.site.register(Detailed_desc)
admin.site.register(pessanger_detail)
admin.site.register(Khalti_details)
admin.site.register(Transactions)

