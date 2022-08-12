from django.db import models
from django.conf import settings

from books.models import Book


class Note(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='notes')

    note_type = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=255, blank=True, null=True)

    body = models.TextField()


class BookNote(Note):
    book = models.ForeignKey(Book,
                             on_delete=models.CASCADE,
                             related_name='bookNotes')
    subtitle = models.CharField(max_length=255)
