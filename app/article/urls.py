from django.urls import path 
from article import views


urlpatterns = [
    path('article/', views.article_list),
    path('article/<int:primary_key>/', views.article_detail),
]