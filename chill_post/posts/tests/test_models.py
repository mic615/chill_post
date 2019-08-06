# tests/test_models.py
from django.test import TestCase

from ..models import Post
from django.contrib.auth.models import User


class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test', email='test@gmail.com', password='top_secret')
    def test_str(self):
        """Test for string representation."""

        post = Post.objects.create(text='hi',user=self.user)
        self.assertEqual(str(post), post.text)
