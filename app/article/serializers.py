from article.models import Article
from article.models import Tags
from rest_framework import serializers


class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    tag_name = serializers.CharField(max_length=10)
    tag_description = serializers.CharField(max_length=100)

    def create(self, validated_data):
        """Create a new `tags` from the given validated_data"""
        return Tags.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update a given to the data provided"""
        instance.tag_name = validated_data.get('tag_name', instance.tag_name)
        instance.tag_description = validated_data.get('tag_description', instance.tag_description)
        instance.save()
        return instance


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=255)
    
    def create(self, validated_data):
        """Create a new `article` from the given validated_data"""
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update a article to the data provided"""
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance