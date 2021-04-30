from django.contrib import admin
from myapp.models import Ngoform, Validedform, AfterPayment,Contact
# Register your models here.
admin.site.register(Ngoform)
admin.site.register(Validedform)
admin.site.register(AfterPayment)
admin.site.register(Contact)