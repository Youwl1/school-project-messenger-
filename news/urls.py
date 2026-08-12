from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name = 'create'),
    path('<int:pk>/', views.NewsDetails.as_view(), name ='news_details'),
    path('<int:post_id>/update/', views.NewsUpdateDetails, name ='news_update'),
    path('<int:pk>/delete/', views.NewsDeleteDetails.as_view(), name='delete-article'),
]