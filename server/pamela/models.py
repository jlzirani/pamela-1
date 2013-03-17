from django.db import models
from django import forms

class Mac(models.Model):
    mac = models.CharField(max_length=17)
    ip = models.CharField(max_length=17)
    last_seen = models.DateTimeField(auto_now=True)
    owner = models.CharField(max_length=50)
    machine = models.CharField(max_length=15)

    def __repr__(self):
        return '<{} {} {} {}>'.format(self.mac,self.ip,self.owner,self.machine)

class MacForm(forms.Form):
    owner = forms.CharField(max_length=50,required=False)
    machine = forms.CharField(max_length=10,required=False)