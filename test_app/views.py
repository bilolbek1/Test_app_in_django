from django.db.models import Q
from django.shortcuts import render
from django.views import View
from test_app.forms import QuestionForm
from test_app.models import Questions, Test


class HomePageView(View):
    def get(self, request):
        tests = Test.objects.all()
        search = request.GET.get('q', '')
        if search:
            tests = tests.filter(
                Q(name__contains=search)
            )
        print(search)

        context = {
            'tests': tests,
            'search': search
        }
        return render(request, 'home.html', context)

class TestDetailView(View):
    def get(self, request, id):
        test = Test.objects.get(id=id)
        questions = test.questions_set.order_by('-id')

        context = {
            "questions": questions,
            "test": test
        }
        return render(request, 'test_detail.html', context)

    def post(self, request, id):
        test = Test.objects.get(id=id)
        questions = test.questions_set.all()
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
        percent = int(percent)

        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        print(correct)
        return render(request, 'result.html', context)







#
# class TestDetailView(View):
#     def get(self, request, id):
#         questions = Questions.objects.all()
#         test = Test.objects.get(id=id)
#         question1 = test.questions_set.all()
#         context = {
#             'test_questions': questions
#         }
#         return render(request, 'home.html', context)
#
#
#     def post(self, request):
#         questions = Questions.objects.all()
#         score = 0
#         wrong = 0
#         correct = 0
#         total = 0
#         for q in questions:
#             total += 1
#             print(request.POST.get(q.question))
#             print(q.ans)
#             print()
#             if q.ans == request.POST.get(q.question):
#                 score += 10
#                 correct += 1
#             else:
#                 wrong += 1
#         percent = score/(total*10) *100
#         percent = int(percent)
#
#         context = {
#             'score':score,
#             'time': request.POST.get('timer'),
#             'correct':correct,
#             'wrong':wrong,
#             'percent':percent,
#             'total':total
#         }
#         print(correct)
#         return render(request,'result.html',context)

