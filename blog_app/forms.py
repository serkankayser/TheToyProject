from django import forms
from .models import Article


class ArticleEditForm(forms.Form):
    class Meta:
        model = Article
        fields = ['title', 'content', 'status']
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={"rows": 1, "cols": 50})
    )
    content = forms.CharField(
        max_length=200,
        widget=forms.Textarea(attrs={"rows": 5, "cols": 50})
    )
    status = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly', })
    )


class ArticleCreateForm(forms.Form):
    class Meta:
        model = Article
        fields = ['title', 'content']
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={"rows": 1, "cols": 50})
    )
    content = forms.CharField(
        max_length=200,
        widget=forms.Textarea(attrs={"rows": 5, "cols": 50}))
