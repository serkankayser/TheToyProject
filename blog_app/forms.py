from django import forms
from .models import Article
from blog_app.tasks import send_feedback_email_task


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


class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={'rows': 5}))
    honeypot = forms.CharField(widget=forms.HiddenInput(), required=False)

    def send_email(self):
        # try to trick spammers by checking whether the honeypot field is
        # filled in; not super complicated/effective but it works
        if self.cleaned_data['honeypot']:
            return False
        send_feedback_email_task.delay(
            self.cleaned_data['email'], self.cleaned_data['message'])
