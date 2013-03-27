from django.http import HttpResponse
from django.template import Context, RequestContext
from django.conf.urls import  include, url
import json

services = {r'pamela/': r'pamela.urls',}


def getPatterns():
	return [url('^'+key, include(value)) for key, value in services.items()]

def getJson(request):
	return HttpResponse(json.dumps(services.keys()), content_type="application/json")


