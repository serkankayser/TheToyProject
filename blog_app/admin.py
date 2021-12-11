from django.contrib import admin
from .models import Article, Writer


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "written_by", "edited_by", "created_at")


class WriterAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(Article, ArticleAdmin)
admin.site.register(Writer, WriterAdmin)
