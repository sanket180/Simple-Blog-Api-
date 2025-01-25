from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

class BlogTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username="testuser", password="12345")
        cls.post = Post.objects.create(author=cls.user,title="Test Post", content="This is a test post.")

    def test_post_model(self):
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.content, "This is a test post.")
        self.assertEqual(str(self.post), "Test Post")