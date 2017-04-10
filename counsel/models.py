from django.db import models

class Counsel01(models.Model):
    writer = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    fp = models.CharField(max_length=15)
    content = models.TextField()
    photo = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hits = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title