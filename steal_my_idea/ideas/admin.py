from django.contrib import admin
from ideas.models import Idea

class IdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published')
    list_filter = ['date_published']
    search_fields = ['title']
    date_hierarchy = 'date_published'

admin.site.register(Idea, IdeaAdmin)
