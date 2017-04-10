from django.contrib import admin
from .models import Contacts, Contacts02, Contacts03, Contacts04, Contacts05

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'content')

class Contacts02Admin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'content')

class Contacts03Admin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'content')

class Contacts04Admin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'content')

class Contacts05Admin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'content')

admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Contacts02, Contacts02Admin)
admin.site.register(Contacts03, Contacts03Admin)
admin.site.register(Contacts04, Contacts04Admin)
admin.site.register(Contacts05, Contacts05Admin)
