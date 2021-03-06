"""toy_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from blog_app import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('article/<int:article_id>', views.article_detail, name='article_detail'),
    path('article-create', views.article_create, name='article-create'),
    path('article-approval', views.article_approval, name='article-approval'),
    path('articles-edited', views.article_edited, name='/articles-edited'),
    url(r'^feedback/$', views.FeedbackView.as_view(), name="feedback"),
    path('admin/', admin.site.urls),
]
