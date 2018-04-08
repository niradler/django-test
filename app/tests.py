from django.test import TestCase
import datetime
from .models import Post
# Create your tests here.

class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(author="Nir Adler", category="Action", post="Sample Post",pub_date=datetime.datetime.now())

    def test_create_post(self):
        """create new post test"""
        post = Post.objects.get(author="Nir Adler")

        self.assertEqual(post.author, 'Nir Adler')
        self.assertEqual(post.category, 'Action')

