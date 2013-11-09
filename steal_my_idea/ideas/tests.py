"""
Unit Tests for Steal My Idea. 
These will pass when you run "manage.py test".
"""

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User

from ideas.models import Idea

def create_idea(title, description, author):
    """Create idea with place holder title and description"""
    return Idea.objects.create(title=title, description=description, author=author)

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

    def test_index_view_with_one_idea(self):
        new_user = User.objects.create_user('Timmy', 'timmy@jimmy.com', 'timmyspwd')
        create_idea(title='Some idea', description='Lorem ipsum', author=new_user)
        response = self.client.get(reverse('ideas:index'))
        self.assertQuerysetEqual(
            response.context['latest_idea_list'], 
            ['<Idea: Some idea>']
        )
        
    def test_index_view_with_two_ideas(self):      
        new_user = User.objects.create_user('Timmy', 'timmy@jimmy.com', 'timmyspwd')  
        create_idea(title='Some idea', description='Lorem ipsum', author=new_user)
        create_idea(title='Another idea', description='Lorem', author=new_user)
        response = self.client.get(reverse('ideas:index'))
        self.assertQuerysetEqual(
            response.context['latest_idea_list'], 
            ['<Idea: Another idea>', '<Idea: Some idea>']
        )