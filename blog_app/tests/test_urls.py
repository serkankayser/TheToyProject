from django.test import TestCase
from django.urls import reverse, resolve
from blog_app.views import dashboard, article_detail


class TestUrls(TestCase):

    def test_list_url_is_resolved(self):
        dashboard_url = reverse('dashboard')
        self.assertEqual(resolve(dashboard_url).func, dashboard)

    def test_article_url_is_resolved(self):
        article_url = reverse('article_detail', args=[1])
        self.assertEqual(resolve(article_url).func, article_detail)
