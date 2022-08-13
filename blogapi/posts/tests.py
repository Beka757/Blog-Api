from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create(
            username='test_user1', password='test_user1'
        )
        test_user1.save()

        test_post = Post.objects.create(
            author=test_user1, title='post title', body='post body'
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'test_user1')
        self.assertEqual(title, 'post title')
        self.assertEqual(body, 'post body')
