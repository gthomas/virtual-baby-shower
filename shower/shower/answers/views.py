from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET
from django.http import HttpResponseForbidden, HttpResponseNotAllowed, JsonResponse, HttpResponseRedirect


# Create your views here.

def guests_only(function):
    def wraps(request, *args, **kwargs):
        if request.user.is_logged_in:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("nope")

@require_GET
@guests_only
def questions(request):
    if request.method == 'GET':
        data = []
        for question in Question.objects.all():
            data.append(Question.to_dict())
        return JsonResponse(data=data)
    elif request.method == 'POST':
        return HttpResponseNotAllowed()

@require_GET
@guests_only
def question_detail(request, question_id):
    pass

@require_http_methods(["GET", "POST"])
@guests_only
def answers(request, question_id):
    if request.method == 'GET':
        data = []
        for answer in Answer.objects.filter(question__pk=question_id):
            data.append(Answer.to_dict())
        return JsonResponse(data=data)
    elif request.method == 'POST':
        return HttpResponseRedirect('question-list')

@require_http_methods(["GET", "POST"])
@guests_only
def my_answer(request, question_id):
    if request.method == 'GET':
        data = []
        for answer in Answer.objects.filter(question__pk=question_id):
            data.append(Answer.to_dict())
        return JsonResponse(data=data)
    elif request.method == 'POST':
        return HttpResponseRedirect()

def donation(request):
    pass

def donate(request):
    pass

def thanks(request):
    pass

def index(request):
    pass
