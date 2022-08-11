from django.contrib import admin
from .models import Note, BookNote


class NoteAdmin(admin.ModelAdmin):
    list_display = ('owner', 'note_type', 'created_at',
                    'updated_at', 'title', 'body')


class BookNoteAdmin(admin.ModelAdmin):
    list_display = ('owner', 'note_type', 'created_at',
                    'updated_at', 'title', 'body')


admin.site.register(Note, NoteAdmin)
admin.site.register(BookNote, BookNoteAdmin)
