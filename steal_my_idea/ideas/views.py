from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django import template

from ideas.models import Idea, Page

class HomeView(generic.ListView):
    """Home page, including 4 most recent ideas"""
    
    template_name = 'ideas/home.html'
    context_object_name = 'latest_idea_list'
    
    def get_queryset(self):
        """Get most recent three ideas."""
        return Idea.objects.order_by('-date_published')[:4]

class IndexView(generic.ListView):
    """List view of 30 most recent ideas"""
    
    template_name = 'ideas/index.html'
    context_object_name = 'latest_idea_list'
    
    def get_queryset(self):
        return Idea.objects.order_by('-date_published')[:30]

class SingleView(generic.DetailView):
    """Renders single ideas to the screen"""
    
    model = Idea
    template_name = 'ideas/single.html'
    
class PageView(generic.DetailView):
    """Renders single pages like About, Contact etc"""
    
    model = Page
    template_name = 'ideas/page.html'

class ResultsView(generic.DetailView):
    """Currently not in use"""
    
    model = Idea
    template_name = 'ideas/results.html'
    
class ProfileView(generic.DetailView):
    """Renders profile pages. Lots of work to be done on these."""
    
    model = User
    template_name = 'ideas/profile.html'

def profile(request, user_id):
    """Currently not in use"""
    
    return HttpResponse('ideas:profile', user_id)

def upvote(request, idea_id):
    """Adds +1 to upvote count. Currently restricted to logged users."""
    
    i = get_object_or_404(Idea, pk=idea_id)
    i.votes += 1
    i.save()
    return HttpResponseRedirect(reverse('ideas:single', args=(i.id,)))

def adduser(request):
    """Custom create user account form"""
    
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            new_user.is_staff = True
            
            try:
                group = Group.objects.get(name='Members')
            except Group.DoesNotExist:
                pass
            else:
                new_user.groups.add(group)
            
            new_user.save()
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            
            # login and redirect to admin interface
            if user is not None:
                if user.is_active:
                    login(request, user)
                else:
                    # Return to form, @TODO add a 'disabled account' error message
                    form = UserForm()
                    return render(request, 'ideas/adduser.html', {'form': form}) 
            else:
                # Return to form, @TODO add an 'invalid login' error message.
                form = UserForm()
                return render(request, 'ideas/adduser.html', {'form': form}) 
            
            return HttpResponseRedirect(reverse('admin:index'))
    else:
        form = UserForm() 

    return render(request, 'ideas/adduser.html', {'form': form}) 

def googleverify(request):
    """Keep Google developer tools happy."""
    
    return render(request, 'ideas/google48059d14ad7e617c.html')

    