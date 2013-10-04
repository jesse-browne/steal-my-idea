from django.http import HttpResponse

from ideas.models import Idea

def index(request):
    latest_ideas = Idea.objects.order_by('-date_published')[:3]
    output = ', '.join([i.title for i in latest_ideas])
    return HttpResponse(output)

def home(request):
    return HttpResponse('Home of Ideas to Steal!')

def single(request, idea_id):
    return HttpResponse('Single Idea to Steal!')

def upvote(request, idea_id):
    return HttpResponse('Single Idea Successfully Up Voted!')