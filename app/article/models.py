from django.db import models


class Tags(models.Model):
    tag_name = models.CharField(max_length=20)
    tag_description = models.CharField(max_length=100)
    # hit_count = models.IntegerField(blank=True, null=True)


class Article(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tags)

    class Meta:
        ordering = ['last_edited']