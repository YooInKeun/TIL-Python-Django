from django.db import models
from django.utils import timezone

class Record(models.Model):

    text = models.TextField()
    word_all_count = models.CharField(max_length=100, default = 'None')
    word_count = models.CharField(max_length=200, default = 'None')
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self):

        return self.text