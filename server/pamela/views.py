from pamela.models import Mac
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext, loader
from django.shortcuts import render
import json, datetime


def show_macs(request):
    macs = Mac.objects.all().filter(last_seen__gte=datetime.datetime.today()-datetime.timedelta(minutes=5))
    j = []
    for mac in macs:
        public = mac.mac
        if mac.owner:
            public = mac.owner
            if mac.machine:
                public += "({})".format(mac.name)
        j.append(public)
    return HttpResponse(json.dumps(j), content_type="application/json")

def update_macs(newmacs):
    for mac in newmacs:
        item, new= Mac.objects.get_or_create(mac=mac)
        if new: print('New mac detected')
        item.ip = newmacs[mac]
        item.save()