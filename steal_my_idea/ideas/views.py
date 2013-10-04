from django.http import HttpResponse
from django.shortcuts import render

from ideas.models import Idea

def index(request):
    latest_idea_list = Idea.objects.order_by('-date_published')[:3]
    context = {'latest_idea_list': latest_idea_list}
    return render(request, 'ideas/index.html', context)

def home(request):
    return HttpResponse('Home of Ideas to Steal!')

def single(request, idea_id):
    return HttpResponse('Single Idea to Steal!')

def upvote(request, idea_id):
    return HttpResponse('Single Idea Successfully Up Voted!')