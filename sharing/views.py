from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import  RequestContext
from django.contrib.auth.decorators import login_required
from taggit.models import Tag
from sharing.models import Material, Category
from sharing.forms import MaterialForm

def objects_list(request, model):
    objects = model.objects.all()
    object_name = objects.model._meta.verbose_name_plural.lower()
    template_name = 'sharing/%s_list.html' % object_name
    return render_to_response(template_name, {
        object_name : objects
    }, context_instance=RequestContext(request))  

  
def material(request, material):
    material = get_object_or_404(Material, slug=material)
    return render_to_response('sharing/materials_detail.html', {
        'material' : material
    })   


def category(request, category):
    category = get_object_or_404(Category, slug=category)
    materials = category.material_set.all()             
    return render_to_response('sharing/categories_detail.html', {
        'category' : category,
        'materials' : materials
    }) 

def tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug,)
    materials = Material.objects.filter(tags__name__in=[tag.name]).distinct()
    return render_to_response('sharing/tags_detail.html', {
        'tag' : tag,
        'materials' : materials
    })   

@login_required
def add_material(request):
    # Get the context from the request.
    context = RequestContext(request)
    # A HTTP POST?
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            obj = form.save(commit=False)
            obj.author = request.user
            form.save_m2m()
            obj.save()
            return redirect('/materials/')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = MaterialForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('sharing/add_material.html', {'form': form}, context)
    
#def edit_mate

def soon(request):
    return HttpResponse("Comming soon...")    