from django.contrib import admin
from newbook.models import Hotel, Plan, Room, RoomStock

# Register your models here.

admin.site.register(Hotel)
admin.site.register(Plan)
admin.site.register(Room)
admin.site.register(RoomStock)