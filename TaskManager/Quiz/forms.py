from django import forms
from .models import Question, Answer, UserAnswer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

    answers = forms.CharField(widget=forms.Textarea)

    def save(self, quiz, commit=True):
        question = super().save(commit=False)
        question.quiz = quiz
        question.save()

        answers = self.cleaned_data.get('answers')
        answers_list = answers.split('\n')

        for answer in answers_list:
            answer_text, is_correct = answer.split(':')
            Answer.objects.create(
                question=question,
                text=answer_text.strip(),
                is_correct=(is_correct.strip().lower() == 'true')
            )

        return question


class TakeQuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.question = kwargs.pop('question')
        super().__init__(*args, **kwargs)
        self.fields['answer'] = forms.ModelChoiceField(
            queryset=self.question.answer_set.all(),
            widget=forms.RadioSelect,
            empty_label=None
        )

    def check_answer(self):
        answer = self.cleaned_data.get('answer')
        is_correct = answer.is_correct
        user_answer = UserAnswer(
            user_quiz=self.question.quiz.userquiz_set.get(user=self.request.user),
            answer=answer,
            is_correct=is_correct
        )
        user_answer.save()
        return is_correct
