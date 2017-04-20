from django.db import models

class Counsel01(models.Model):
    writer = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    fp = models.CharField(max_length=15)
    content = models.TextField()
    photo = models.FileField(null=True, blank=True, upload_to='%y/%m/%d')
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hits = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title

class Counsel02(models.Model):
    writer = models.CharField(max_length=15)
    birth = models.CharField(max_length=20)
    tel = models.IntegerField()
    email = models.CharField(max_length=40)
    address = models.CharField(max_length=20)
    job = models.CharField(max_length=20)
    area = models.CharField(max_length=10, null=True)
    starttime = models.CharField(max_length=20, null=True)
    endtime = models.CharField(max_length=20, null=True)
    fp = models.CharField(max_length=15, null=True)
    content = models.CharField(max_length=50, null=True)
    agree = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
