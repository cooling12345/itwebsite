from django.urls import path
from . import views
app_name = 'website'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('board/', views.board, name='board'),
    path('swipe/', views.swipe, name='swipe'),
    path('music/', views.music, name='music'),
]