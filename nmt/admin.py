from django.contrib import admin

from .models import Account, NetworkCenter, Building, Floor, Local, Equipement, Commands




# Register your models here.
admin.site.register(Account)
admin.site.register(NetworkCenter)
admin.site.register(Building)
admin.site.register(Floor)
admin.site.register(Local)
admin.site.register(Equipement)
admin.site.register(Commands)

