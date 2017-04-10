from django.contrib import admin
from .models import Customer01, Customer02, Customer03

class Customer01Admin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'content')

class Customer02Admin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'content')

class Customer03Admin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'content', 'start_date', 'end_date')

admin.site.register(Customer01, Customer01Admin)
admin.site.register(Customer02, Customer02Admin)
admin.site.register(Customer03, Customer03Admin)