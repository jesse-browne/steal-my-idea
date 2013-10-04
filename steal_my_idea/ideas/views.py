from django.http import HttpResponse
from django.template import RequestContext, loader

from ideas.models import Idea

def index(request):
    latest_idea_list = Idea.objects.order_by('-date_published')[:3]
    template = loader.get_template('ideas/index.html')
    context = RequestContext(request, {
        'latest_idea_list': latest_idea_list,
    })
    return HttpResponse(template.render(context))

def home(request):
    return HttpResponse('Home of Ideas to Steal!')

def single(request, idea_id):
    return HttpResponse('Single Idea to Steal!')

def upvote(request, idea_id):
    return HttpResponse('Single Idea Successfully Up Voted!')