from django.shortcuts import render, render_to_response, redirect
from django.template import  RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.messages import error
from users.models import User
from sharing.models import Material

# Create your views here.
def users_list(request):
    users = User.objects.all()
    return render_to_response('users/users_list.html', {
        'users' : users,
        
    }, context_instance= RequestContext(request))

def user_profile(request, username):
    user = User.objects.get(username=username)    
    return render_to_response('users/user_profile.html', {
        'user_' : user,
    }, context_instance= RequestContext(request))

def user_pubs(request, username):
    materials = Material.objects.filter(author__username=username)
    return render_to_response('users/user_posts.html', {
        'materials' : materials,
        'username' : username,
    }, context_instance= RequestContext(request))

def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
            else:
                error(request, 'Account is non-active or blocked!') 
        else:
            error(request, 'Invalid username or password!')   
    return HttpResponseRedirect('/materials/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/materials/')