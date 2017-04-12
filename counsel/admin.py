from django.contrib import admin
from .models import Counsel01

class Counsel01Admin(admin.ModelAdmin):
    list_display = ('id', 'writer', 'title', 'fp', 'content', 'photo')

admin.site.register(Counsel01, Counsel01Admin)