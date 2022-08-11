from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'author', 'startDate', 'endDate')


admin.site.register(Book, BookAdmin)
