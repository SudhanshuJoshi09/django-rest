from django.urls import path 
from rest_framework.urlpatterns import format_suffix_patterns
from article import views


urlpatterns = [
    path('article/', views.article_list),
    path('article/<int:primary_key>/', views.article_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)