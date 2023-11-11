from django.shortcuts import render
from django.views import View
from test_app.forms import QuestionForm
from test_app.models import Questions


# class HomePageView(View):
#     def get(self, request):
#         form = QuestionForm()
#         test_questions = Questions.objects.all()
#
#         context = {
#             "form": form,
#             "test_questions": test_questions,
#         }
#         return render(request, 'home.html', context)

class HomePageView(View):
    def get(self, request):
        questions = Questions.objects.all()
        context = {
            'test_questions': questions
        }
        return render(request, 'home.html', context)


    def post(self, request):
        questions = Questions.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans == request.POST.get(q.question):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score/(total*10) *100

        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        print(correct)
        return render(request,'result.html',context)

