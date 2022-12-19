from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.http import HttpResponseNotAllowed
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


from django.http import HttpResponse


def index(request):
    page = request.GET.get('page', '1')
    #question_list =  Question.objects.all().order_by('-create_date')
    question_list =  Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)    #페이지당 10개 씩 보여주기
    page_obj = paginator.get_page(page)
    print(page_obj)
    context = {'question_list': page_obj}
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

# 구버전
# def answer_create(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     #answer_set 무엇인가
#     # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
#     answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
#     answer.save()
#     return redirect('pybo:detail', question_id = question.id)

@login_required(login_url='common:login')
def question_create(request):
    if request.method == "POST":
        print(request.POST)
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect("pybo:index")
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

