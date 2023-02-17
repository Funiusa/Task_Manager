from django.views.generic import ListView, CreateView, DetailView
from .models import Quiz, UserQuiz, Question, UserAnswer
from django.urls import reverse_lazy


class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz/quiz_list.html'


class QuizCreateView(CreateView):
    model = Quiz
    fields = ['title', 'description']
    template_name = 'quiz/quiz_form.html'
    success_url = reverse_lazy('quiz_list')


class QuizResultView(DetailView):
    model = Quiz
    template_name = 'quiz/quiz_results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_quiz = UserQuiz.objects.get(user=self.request.user, quiz=self.object)
        context['user_quiz'] = user_quiz
        context['user_answers'] = UserAnswer.objects.filter(user_quiz=user_quiz)
        return context
