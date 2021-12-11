from django.shortcuts import render
from .models import Article, User
from django.db.models import Q
from .forms import ArticleEditForm, ArticleCreateForm
from django.contrib import messages
from django.core.exceptions import PermissionDenied
import datetime
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def logged_user(request, format=None):
    content = {
        'user': str(request.user),
        'auth': str(request.auth),
    }
    return Response(content)


def dashboard(request):
    # GET LAST 30 DAYS
    last_30 = datetime.datetime.now() - datetime.timedelta(30)

    # GET ORM OBJECTS
    articles_gte = (Article.objects.filter(
        Q(created_at__gte=last_30)).order_by('written_by')
    )
    articles_all = Article.objects.all().order_by('written_by')

    # PUSH VALUES IN DICT
    context_all = {}
    context_gte = {}
    for x in articles_all:
        if str(x.written_by) in context_all:
            context_all[str(x.written_by)] += 1
        else:
            context_all[str(x.written_by)] = 1
    for x in articles_gte:
        if str(x.written_by) in context_gte:
            context_gte[str(x.written_by)] += 1
        else:
            context_gte[str(x.written_by)] = 1
    # ZIP THE DICT ITEMS
    zipped_dicts = zip(context_all.items(), context_gte.items())
    context = {
        'context_all': zipped_dicts
    }
    return render(request, 'index.html', context)


def article_create(request):
    if request.method == 'POST':
        form = ArticleCreateForm(request.POST)
        if form.is_valid():
            article = Article(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                written_by=request.user.writer,
                created_at=datetime.datetime.now(),
                status='pending'
            )
            article.save()
            messages.success(request, 'Article successfully created')
    if request.user.writer.is_editor:
        form = ArticleCreateForm()
        context = {
            "form": form
        }
        return render(request, 'article_create.html', context)
    raise PermissionDenied()


def article_detail(request, article_id):
    if request.user.writer.is_editor:
        if request.method == 'POST':
            form = ArticleEditForm(request.POST)
            if form.is_valid():
                article = Article.objects.get(id=article_id)
                article.title = form.cleaned_data['title']
                article.content = form.cleaned_data['content']
                article.status = form.cleaned_data['status']

                article.save(update_fields=['title', 'content', 'status'])
                messages.success(request, 'Form submission successful')

        form = ArticleEditForm()
        all_articles = (Article.objects.filter(
            id=article_id).
            values('title', 'content', 'status')
        )
        if all_articles:
            for article in all_articles:
                form.fields['title'].initial = article['title']
                form.fields['content'].initial = article['content']
                form.fields['status'].initial = article['status']
                context = {
                    "data": article,
                    "form": form
                }
            return render(request, 'article.html', context)
        return render(request, 'error.html')
    raise PermissionDenied()


def article_approval(request):
    if request.user.writer.is_editor:
        if request.method == 'POST':
            action = request.POST.get('status')
            id = request.POST.get('id')

            article = Article.objects.get(id=id)
            if action == 'Approve':
                article.status = 'approved'
            elif action == 'Reject':
                article.status = 'rejected'
            article.edited_by = request.user.writer
            article.save(update_fields=['status', 'edited_by'])
            messages.success(request, f'Status of {id}. article changed')
        context = {
            'data': []
        }
        all_articles = Article.objects.all().order_by('id').values()
        for article in all_articles:
            if article['status'] == 'pending':
                context['data'].append((
                    article['id'],
                    article['title'],
                    article['content'],
                    article['status'])
                )
        return render(request, 'article_approval.html', context)
    raise PermissionDenied()


def article_edited(request):
    if request.user.writer.is_editor:
        if request.method == 'POST':
            action = request.POST.get('status')
            id = request.POST.get('id')

            article = Article.objects.get(id=id)
            if action == 'Approve':
                article.status = 'approved'
            elif action == 'Reject':
                article.status = 'rejected'

            article.save(update_fields=['status'])
        context = {
            'data': []
        }
        all_users = [(user.id, user.username) for user in User.objects.all()]
        all_articles = Article.objects.all().order_by('id').values()
        for article in all_articles:
            if article['status'] != 'pending':
                for user in all_users:
                    if article['edited_by_id'] == user[0]:
                        article['edited_by_id'] = user[1]
                context['data'].append((
                    article['id'],
                    article['title'],
                    article['content'],
                    article['status'],
                    article['edited_by_id'])
                )

        return render(request, 'article_edited.html', context)
    raise PermissionDenied()
