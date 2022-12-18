from django.shortcuts import render
from .models import Question
# Create your views here.

from django.http import HttpResponse


def index(request):
    #question_list =  Question.objects.all().order_by('-create_date')
    question_list =  Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    print(question_list)
    #return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")
    return render(request, 'pybo/question_list.html', context)


# def detail(request, question_id):
#     print(question_id)
#     question = Question.objects.get(id=question_id)
#     context = {'question': question}
#     return render(request, 'pybo/question_detail.html', context)
from django.shortcuts import render, get_object_or_404
from .models import Question

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)