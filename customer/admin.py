from django.contrib import admin
from .models import Customer01, Customer02, Customer03, Customer04

class Customer01Admin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'content')

class Customer02Admin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'content')

class Customer03Admin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'content', 'start_date', 'end_date')

class Customer04Admin(admin.ModelAdmin):
    list_display = ('id', 'writer', 'title', 'content', 'password', 'user', 'answer')

admin.site.register(Customer01, Customer01Admin)
admin.site.register(Customer02, Customer02Admin)
admin.site.register(Customer03, Customer03Admin)
admin.site.register(Customer04, Customer04Admin)
