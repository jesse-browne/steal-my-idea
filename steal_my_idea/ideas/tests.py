"""
Unit Tests for Steal My Idea. 
These will pass when you run "manage.py test".
"""

from django.test import TestCase
from django.core.urlresolvers import reverse

from ideas.models import Idea

def create_idea(title, description):
    """Create idea with place holder title and description"""
    return Idea.objects.create(title=title, description=description)

def create_page(heading, text):
    """Create a page with heading and text"""
    return Page.objects.create(heading=heading, text=text)

class IdeaViewTests(TestCase):
    def test_index_view_with_no_ideas(self):
        """If no ideas show error message"""
        response = self.client.get(reverse('ideas:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no ideas to steal right now :(')
        self.assertQuerysetEqual(response.context['latest_idea_list'], [])

#    def test_index_view_with_one_idea(self):        
#        create_idea(title='Some idea', description='Lorem ipsum')
#        response = self.client.get(reverse('ideas:index'))
#        self.assertQuerysetEqual(
#            response.context['latest_idea_list'], 
#            ['<Idea: Some idea>']
#        )
        
#    def test_index_view_with_two_ideas(self):        
#        create_idea(title='Some idea', description='Lorem ipsum')
#        create_idea(title='Another idea', description='Lorem')
#        response = self.client.get(reverse('ideas:index'))
#        self.assertQuerysetEqual(
#            response.context['latest_idea_list'], 
#            ['<Idea: Another idea>', '<Idea: Some idea>']
#        )