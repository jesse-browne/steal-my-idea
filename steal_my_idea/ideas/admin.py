from django.contrib import admin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

from ideas.models import Idea, Page

class IdeaAdmin(admin.ModelAdmin):
    """
    Sets current authenticated user as idea author.
    Shows all ideas to admins and shows non-admins only their own ideas.
    Re-directs back to front end on successful idea creation if Save option selected.
    """
    
    list_display = ('title', 'date_published')
    list_filter = ['date_published']
    search_fields = ['title']
    date_hierarchy = 'date_published'
    
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
        
    def queryset(self, request):
        if request.user.is_superuser:
            return Idea.objects.all()
        return Idea.objects.filter(author=request.user)
    
    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect(reverse("ideas:index"))


class PageAdmin(admin.ModelAdmin):
    """Provides search, filter by date and lists pages in order of date published"""
    
    list_display = ('heading', 'date_published')
    list_filter = ['date_published']
    search_fields = ['heading']
    date_hierarchy = 'date_published'    

admin.site.register(Idea, IdeaAdmin)
admin.site.register(Page, PageAdmin)
