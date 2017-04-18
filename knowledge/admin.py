from django.contrib import admin
from .models import Contacts, Contacts02, Contacts03, Contacts04, Contacts05, Contacts06q
from .models2 import Contacts06a

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

class Contacts06qAdmin(admin.ModelAdmin):
    list_display = ('id', 'writer', 'title', 'content')

class Contacts06aAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'reply')

admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Contacts02, Contacts02Admin)
admin.site.register(Contacts03, Contacts03Admin)
admin.site.register(Contacts04, Contacts04Admin)
admin.site.register(Contacts05, Contacts05Admin)
admin.site.register(Contacts06q, Contacts06qAdmin)
admin.site.register(Contacts06a, Contacts06aAdmin)
