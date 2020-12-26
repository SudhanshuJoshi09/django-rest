from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from article.models import Tags, Article
from article.serializers import TagSerializer, ArticleSerializer


@csrf_exempt
def article_list(request):
    """List all the articles, or create a new article"""
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            return JsonResponse(serializer.data, status=201)
        return Jsonresponse(serializer.errors, status=400)


@csrf_exempt
def article_detail(request, primary_key):
    """Retrieve, update or delete a article"""
    try:
        article = Article.objects.get(primary_key)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArticleSerializer()