from django.urls import resolve
from django.test import TestCase
from blog.views import post_list
from blog.views import post_detail

class PostListTest(TestCase):

    def test_root_url_resolves_to_post_list_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, post_list)  



class PostDetailTest(TestCase):

    def test_root_url_resolves_to_post_detail_view(self):
        found = resolve('/post/14/')  
        self.assertEqual(found.func, post_detail)  