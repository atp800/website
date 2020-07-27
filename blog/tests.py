from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from blog.views import post_list
from blog.views import post_detail
from blog.views import post_edit
from blog.views import post_new


class PostListTest(TestCase):

    def test_root_url_resolves_to_post_list_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, post_list) 

    def test_post_list_returns_correct_html(self):
        request = HttpRequest()  
        response = post_list(request)  
        html = response.content.decode('utf8')  
        #self.assertTrue(html.startswith('<html>'))  
        self.assertIn('<title>2nd Year Blog</title>', html)  
        self.assertTrue(html.endswith('</html>')) 



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