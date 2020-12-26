from article.models import Article
from article.models import Tags
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id', 'tag_name', 'tag_description']


class ArticleSerializer(serializers.Serializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'description']
    