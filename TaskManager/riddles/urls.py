from django.urls import path
from . import views

# app_name = 'riddles'

urlpatterns = [
    path('', views.riddles_index, name='riddles_index'),
    path('detail/', views.detail, name="detail"),
    path('answer/', views.answer, name="answer"),
]
