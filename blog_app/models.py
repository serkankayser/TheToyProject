from django.db import models
from django.contrib.auth.models import User


class Writer(models.Model):
    is_editor = models.BooleanField(default=False)
    name = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Article(models.Model):
    status_choices = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    )
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    status = models.CharField(
        max_length=20,
        choices=status_choices, default='Pending'
    )
    written_by = models.ForeignKey(
        Writer,
        related_name='article_written_by',
        on_delete=models.CASCADE
    )
    edited_by = models.ForeignKey(
        Writer,
        related_name='article_edited_by',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField()

    def __str__(self):
        return f"{self.title} {self.status} {self.written_by} {self.edited_by} {self.created_at}"
