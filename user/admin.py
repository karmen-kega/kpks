from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Rapport, HistoriqueConnexion, Position, mission, message

# Register your models here.

admin.site.register(User)
admin.site.register(Rapport)
admin.site.register(HistoriqueConnexion)
admin.site.register(Position)
admin.site.register(mission)
admin.site.register(message)