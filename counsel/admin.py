from django.contrib import admin
from .models import Counsel01, Counsel02

class Counsel01Admin(admin.ModelAdmin):
    list_display = ('id', 'writer', 'title', 'fp', 'content', 'photo')

class Counsel02Admin(admin.ModelAdmin):
    list_display = ('id', 'writer', 'birth', 'tel', 'email', 'address', 'job', 'area', 'starttime', 'endtime', 'fp', 'content', 'agree')

admin.site.register(Counsel01, Counsel01Admin)
admin.site.register(Counsel02, Counsel02Admin)
