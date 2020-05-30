from django.urls import path

from . import views

app_name = 'main_app'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('loadArticles/', views.loadArticles, name = 'loadArticles'),
    path('category/', views.category, name = 'category')
]