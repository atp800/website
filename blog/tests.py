from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from blog.views import post_list
from blog.views import post_detail
from blog.views import post_edit
from blog.views import post_new
from blog.views import cv_edit
from blog.views import cv_display


class PostListTest(TestCase):

    def test_root_url_resolves_to_post_list_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, post_list) 

    def test_post_list_returns_correct_html(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')  
        self.assertTrue(html.strip().startswith('<html>'))  
        self.assertIn('<title>2nd Year Blog</title>', html)  
        self.assertTrue(html.endswith('</html>'))
        self.assertTemplateUsed(response, 'blog/post_list.html')         



class PostDetailTest(TestCase):

    def test_root_url_resolves_to_post_detail_view(self):
        found = resolve('/post/14/')  
        self.assertEqual(found.func, post_detail)
        

class PostEditTest(TestCase):

    def test_root_url_resolves_to_post_edit_view(self):
        found = resolve('/post/14/edit/')  
        self.assertEqual(found.func, post_edit) 


class PostNewTest(TestCase):

    def test_root_url_resolves_to_post_new_view(self):
        found = resolve('/post/new/')  
        self.assertEqual(found.func, post_new)  


class CVDisplayTest(TestCase):

    def test_root_url_resolves_to_cv_display_view(self):
        found = resolve('/cv/')  
        self.assertEqual(found.func, cv_display)


class CVEditTest(TestCase):

    def test_root_url_resolves_to_cv_edit_view(self):
        found = resolve('/cv/edit/')  
        self.assertEqual(found.func, cv_edit)