from notes.models import Note, BookNote
from rest_framework import serializers


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['pk', 'note_type', 'created_at',
                  'updated_at', 'title', 'body']


class BookNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNote
        fields = ['pk', 'note_type', 'created_at',
                  'updated_at', 'title', 'body', 'book']
