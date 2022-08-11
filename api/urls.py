from django.urls import include, path
from rest_framework.routers import DefaultRouter

from notes.api import views as noteViews
from books.api import views as bookViews

router = DefaultRouter()

router.register(r'notes', noteViews.NoteViewSet, basename='notes')
router.register(r'book_notes', noteViews.BookNoteViewSet, basename='bookNotes')
router.register(r'book', bookViews.BookViewSet, basename='books')

urlpatterns = [
    path('', include(router.urls)),
]
