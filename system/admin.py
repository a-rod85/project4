from django.contrib import admin
from .models import Restaurant, Table, Seat, Reservation
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(Seat)
admin.site.register(Reservation)
