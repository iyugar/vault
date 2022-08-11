from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from notes.api.serializers import NoteSerializer, BookNoteSerializer
from notes.models import Note, BookNote


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookNoteViewSet(viewsets.ModelViewSet):
    serializer_class = BookNoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BookNote.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
