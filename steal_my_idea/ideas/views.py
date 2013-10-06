from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic

from ideas.models import Idea

class IndexView(generic.ListView):
    template_name = 'ideas/index.html'
    context_object_name = 'latest_idea_list'
    
    def get_queryset(self):
        """Get most recent three ideas."""
        return Idea.objects.order_by('-date_published')[:3]

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
