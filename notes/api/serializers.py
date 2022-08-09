from notes.models import Note
from rest_framework import serializers


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['pk', 'note_type', 'created_at',
                  'updated_at', 'title', 'body']
