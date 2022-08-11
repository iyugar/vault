from django.db import models
from django.conf import settings

class Book(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='books')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    startDate = models.DateField()
    endDate = models.DateField()

    def __str__(self):
        return self.title
    
