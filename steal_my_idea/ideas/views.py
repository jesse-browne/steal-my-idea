from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404

from ideas.models import Idea

def index(request):
    latest_idea_list = Idea.objects.order_by('-date_published')[:3]
    context = {'latest_idea_list': latest_idea_list}
    return render(request, 'ideas/index.html', context)

def home(request):
    return HttpResponse('Home of Ideas to Steal!')

def single(request, idea_id):
    idea = get_object_or_404(Idea, pk=idea_id)
    return render(request, 'ideas/single.html', {'idea': idea})

def upvote(request, idea_id):
    i = get_object_or_404(Idea, pk=idea_id)
    i.votes += 1
    i.save()
    return HttpResponseRedirect(reverse('ideas:results', args=(i.id,)))

def results(request, idea_id):
    idea = get_object_or_404(Idea, pk=idea_id)
    return render(request, 'ideas/results.html', {'idea': idea})