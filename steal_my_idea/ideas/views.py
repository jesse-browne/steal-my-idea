from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group

from ideas.models import Idea

class HomeView(generic.ListView):
    template_name = 'ideas/home.html'
    context_object_name = 'latest_idea_list'
    
    def get_queryset(self):
        """Get most recent three ideas."""
        return Idea.objects.order_by('-votes')[:4]

class IndexView(generic.ListView):
    template_name = 'ideas/index.html'
    context_object_name = 'latest_idea_list'
    
    def get_queryset(self):
        """Get most recent three ideas."""
        return Idea.objects.order_by('-votes')[:20]

class SingleView(generic.DetailView):
    model = Idea
    template_name = 'ideas/single.html'

class ResultsView(generic.DetailView):
    model = Idea
    template_name = 'ideas/results.html'

def upvote(request, idea_id):
    i = get_object_or_404(Idea, pk=idea_id)
    i.votes += 1
    i.save()
    return HttpResponseRedirect(reverse('ideas:results', args=(i.id,)))

def adduser(request):
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
            return HttpResponseRedirect(reverse('admin:index'))
    else:
        form = UserForm() 

    return render(request, 'ideas/adduser.html', {'form': form}) 