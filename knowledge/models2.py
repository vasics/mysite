from knowledge.models import Contacts06q
from django.db import models
from django.contrib.auth.models import User

class Contacts06a(models.Model):
    user = models.ForeignKey(User)
    contacts06q = models.ForeignKey(Contacts06q, null=True)
    reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)