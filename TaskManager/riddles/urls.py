from django.urls import path
from . import views

app_name = 'riddles'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name="detail"),
    path('answer/', views.answer, name="answer"),
]
