from django.db import models
from django.utils import timezone

class Query(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    class Meta: 
        ordering = ('-created_at',)
    def __str__(self):
        return self.title

class Result(models.Model):
    results = models.BigIntegerField()
    searched_at = models.DateTimeField(default=timezone.now)
    search_time = models.BigIntegerField()
    query = models.ForeignKey(Query, on_delete=models.CASCADE, related_name='id_query')

    class Meta: 
        ordering = ('-searched_at',)

    