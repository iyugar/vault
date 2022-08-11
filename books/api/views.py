from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from books.api.serializers import BookSerializer
from books.models import Book


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
