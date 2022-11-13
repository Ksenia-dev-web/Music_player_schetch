from django.urls import path
from . import views

app_name = 'play'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.MusicFileView.as_view(), name='music_file'),
    path('<int:id>/likes/', views.likes, name='likes'),
    # path('music_file/likes/', views.likes, name='likes'),
]