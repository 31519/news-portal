from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('local_news/', views.local_news, name='local_news'),
    path('post_detail/<slug:category_slug>/<slug:post_slug>/', views.post_detail, name='post_detail'),

]
