from django.contrib import admin
from django.contrib.auth.models import User

from ideas.models import Idea, Page

class IdeaAdmin(admin.ModelAdmin):
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

class PageAdmin(admin.ModelAdmin):
    list_display = ('heading', 'date_published')
    list_filter = ['date_published']
    search_fields = ['heading']
    date_hierarchy = 'date_published'    

admin.site.register(Idea, IdeaAdmin)
admin.site.register(Page, PageAdmin)
