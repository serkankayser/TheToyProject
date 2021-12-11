from django.test import TestCase
from blog_app.forms import ArticleCreateForm, ArticleEditForm


class TestForms(TestCase):
    def test_article_create_form_valid(self):
        form = ArticleCreateForm(data={
            'title': "Testing title",
            'content': "Testing content"
        })
        self.assertTrue(form.is_valid())

    def test_article_create_form_invalid(self):
        form = ArticleCreateForm(data={
            'title': "Testing title",
            'content':
            """Lorem Ipsum is simply dummy text of the printing
            and typesetting industry. Lorem Ipsum has been the industry's
            standard dummy text ever since the 1500s, when an unknown printer
            took galley of type and scrambled it to make a type specimen book.
            It has survived not only five centuries"""
        })
        self.assertFalse(form.is_valid())

    def test_article_edit_form_invalid(self):
        form = ArticleEditForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
