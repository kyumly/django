from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.http import HttpResponseNotAllowed
from .models import Answer
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Question


from django.http import HttpResponse

# def detail(request, question_id):
#     print(question_id)
#     question = Question.objects.get(id=question_id)
#     context = {'question': question}
#     return render(request, 'pybo/question_detail.html', context)



# 구버전
# def answer_create(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     #answer_set 무엇인가
#     # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
#     answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
#     answer.save()
#     return redirect('pybo:detail', question_id = question.id)