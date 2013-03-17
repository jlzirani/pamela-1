from django.db import models

class Mac(models.Model):
    mac = models.CharField(max_length=17)
    ip = models.CharField(max_length=17)
    last_seen = models.DateTimeField(auto_now=True)
    owner = models.CharField(max_length=50)
    machine = models.CharField(max_length=15)
