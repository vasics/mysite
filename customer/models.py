from django.db import models
from django.contrib.auth.models import User

class Customer01(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hits = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title

class Customer02(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hits = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title

class Customer03(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    content = models.TextField()
    start_date = models.IntegerField()
    end_date = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hits = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title

class Customer04(models.Model):
    writer = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    content = models.CharField(max_length=1000)
    user = models.ForeignKey(User, null=True)
    answer = models.CharField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hits = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title
