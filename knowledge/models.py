from django.db import models
from django.contrib.auth.models import User

class Contacts(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hits = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title

class Contacts02(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hits = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title

class Contacts03(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hits = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title

class Contacts04(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hits = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title

class Contacts05(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hits = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title

class Contacts06q(models.Model):
    writer = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hits = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title
