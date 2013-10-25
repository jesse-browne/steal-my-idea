from django.db import models
from django.contrib.auth.models import User

class Idea(models.Model):
    """The framework of an idea!"""
    
    HELP = 'Help! Work with me to make this idea a reality'
    EXECUTION = 'Someone, anyone to make take this idea and make it a reality'
    AUTHOR_WANTS_OPTIONS = (
        (HELP,      'help! Work with me to make this idea a reality, email me to get started.'),
        (EXECUTION, 'someone, anyone to take this idea and make it a reality.'),           
    )
    
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, related_name="author", editable=False)
    date_published = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    author_wants = models.CharField('I want', max_length=100, choices=AUTHOR_WANTS_OPTIONS, default=EXECUTION)
    votes = models.IntegerField(default=0, editable=False)
    
    def __unicode__(self):
        return self.title

class Page(models.Model):
    """For single pages like About, Contact etc"""
    
    heading = models.CharField(max_length=200)
    date_published = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    
    def __unicode__(self):
        return self.heading