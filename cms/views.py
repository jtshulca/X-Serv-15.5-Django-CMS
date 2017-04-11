from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from cms.models import Pages
# Create your views here.


def show(request):
    record = Pages.objects.all()
    respuesta = "Page Found: "
    for page in record:
        respuesta += "<li>/" + page.name + " --> " + page.page 
    return HttpResponse(respuesta)


def show_content(request, resource):
    try:
        record = Pages.objects.get(name=resource)
        return HttpResponse(record.page)
    except Pages.DoesNotExist:
        return HttpResponseNotFound('Page Not Found: /%s.' % resource)
