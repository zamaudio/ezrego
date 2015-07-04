from django.contrib import admin

from .models import Vehicle
from .models import Person
from .models import VehicleTransfer

admin.site.register(Vehicle)
admin.site.register(Person)
admin.site.register(VehicleTransfer)
