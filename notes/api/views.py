from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from notes.api.serializers import NoteSerializer
from notes.models import Note


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)
