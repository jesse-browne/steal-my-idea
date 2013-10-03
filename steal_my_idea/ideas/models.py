from django.db import models

# Define models.

class Idea(models.Model):
    HELP = 'HE'
    EXECUTION = 'EX'
    MONEY = 'MO'
    AUTHOR_WANTS_OPTIONS = (
        (HELP, 'Help! Work with me to make this idea a reality'),
        (EXECUTION, 'Someone, anyone to make take this idea and make it a reality'),
        (MONEY, 'Money to take this idea and turn it into a reality'),            
    )
    
    title = models.CharField(max_length=200)
    date_published = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    author_wants = models.CharField(max_length=2, choices=AUTHOR_WANTS_OPTIONS, default=EXECUTION)
    
class UpVotes(models.Model):
    idea = models.ForeignKey(Idea)
    votes = models.IntegerField(default=0)

