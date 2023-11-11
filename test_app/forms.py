from django.forms import ModelForm

from test_app.models import Questions


class QuestionForm(ModelForm):
    class Meta:
        model = Questions
        fields = "__all__"

