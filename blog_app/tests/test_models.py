from django.test import TestCase
from blog_app.models import Article, Writer, User
from datetime import datetime


class ArticleTest(TestCase):

    def create_article(self, title="Test title", content="Test content"):
        user = User.objects.create(username='serkan')
        writer = Writer.objects.create(name=user)
        return Article.objects.create(title=title, content=content, created_at=datetime.now(), written_by=writer)

    def test_create_article(self):
        w = self.create_article()
        self.assertTrue(isinstance(w, Article))
        self.assertEqual('Test title', w.title)
