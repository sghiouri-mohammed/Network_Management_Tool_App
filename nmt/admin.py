from django.contrib import admin

from .models import Account, Floor, ConferenceCenterBuildings, CampusBuildings, NetworkCenter, DataCenterBuildings


# Register your models here.
admin.site.register(Account)
admin.site.register(Floor)
admin.site.register(ConferenceCenterBuildings)
admin.site.register(CampusBuildings)
admin.site.register(NetworkCenter)
admin.site.register(DataCenterBuildings)
