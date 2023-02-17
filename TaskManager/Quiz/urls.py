from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    QuizListView,
    QuizCreateView,
)

urlpatterns = [
    # Login and logout views
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

# urlpatterns = [
#     path('', QuizListView.as_view(), name='quiz_list'),
#     path('create/', QuizCreateView.as_view(), name='quiz_create'),
#     # path('<int:pk>/update/', QuizUpdateView.as_view(), name='quiz_update'),
#     # path('<int:pk>/', QuizDetailView.as_view(), name='quiz_detail'),
#     # path('<int:pk>/add_question/', QuestionCreateView.as_view(), name='question_create'),
#     # path('<int:pk>/take/', TakeQuizView.as_view(), name='take_quiz'),
#     # path('<int:pk>/results/', QuizResultView.as_view(), name='quiz_results'),
# ]
