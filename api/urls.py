from django.urls import include, path
from rest_framework.routers import DefaultRouter

from notes.api import views as noteViews

router = DefaultRouter()

router.register(r'notes', noteViews.NoteViewSet, basename='notes')

urlpatterns = [
    path('', include(router.urls)),
]
