from django.shortcuts import render_to_response
from django.template import  RequestContext
from sharing.models import Material, Category

def index(request):
    latest_materials = Material.objects.all()[:3]
    return render_to_response('index.html', {"latest_materials" : latest_materials}, context_instance=RequestContext(request))
