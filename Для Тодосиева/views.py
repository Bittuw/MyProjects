from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from .models import Experiment, Question, User
from django.views.generic import View

from django.utils import timezone

# Create your views here.
def index(request):
    user_id = request.session.get("user")
    if user_id is None:
        user_id = User.objects.create().id
    request.session["user"] = user_id
    return render(request, "index.html")

def test(request):
    if request.session.get("user", 0) == 0:
        return HttpResponseRedirect("/polls/")

    if request.method == "POST":
        time = request.POST.get('time')
        request.session["time"] = time
    else:
        button_exit = False
        user__id = User.objects.get(id=request.session["user"])
        exp = Experiment.objects.filter(user_id=user__id)
        count = exp.count()
        if count >= 5:
            button_exit=True
        if count >=10:
            request.session['exit']=True
            return redirect('exit')
        question = Question.random_question(Question, exp)
        request.session["question"]=question.id_q
        request.session['time_start'] = (timezone.now() - timezone.datetime(1900, 1, 1, tzinfo=timezone.utc)).seconds
        return render(request, 'test.html', {'question': question, 'button_exit':button_exit, 'count':count+1})


    
def answer(request):
    if request.session.get("user", 0) == 0:
        return HttpResponseRedirect("/polls/")

    if request.session.get('exit', False) == True:
        return HttpResponseRedirect("/polls/exit/")

    if request.method == "POST":
        time_diff = request.session['time_start']
        ans_text = request.POST.get('answer')
        if (ans_text == ""):
            ans_text = "Null"
        ad_ans = request.POST.get('adeq')
        uid = request.session["user"]
        qid = request.session["question"]
        ans = Experiment.objects.create(
            user_id=User.objects.get(id=uid),
            question_id=Question.objects.get(id_q=qid),
            answer=ans_text,
            adequacy = ad_ans,
            time_start = time_diff
        )
        ans.save()
        return redirect('test')
    else:
        template = loader.get_template('answer.html')
        context = RequestContext(request)
        # (timezone.datetime(1900, 1, 1) - timezone.now()).seconds
        request.session['time_start'] = (timezone.now() - timezone.datetime(1900, 1, 1, tzinfo=timezone.utc)).seconds - request.session[
            'time_start']
        return render(request, 'answer.html')

def exit(request):
    if request.session.get("user", 0) == 0:
        return HttpResponseRedirect("/polls/")
    return render(request, 'exit.html')


# class Test(View):

#     def get(self, request):
#         user_id = request.session.get("user")
#         if user_id is None:
#             HttpResponseRedicert('polls/')

#         button_exit = False
#         user__id = User.objects.get(id=request.session["user"])
#         exp = Experiment.objects.filter(user_id=user__id)
#         count = exp.count()
#         if count >= 5:
#             button_exit=True
#         if count >=10:
#             request.session['exit']=True
#             return redirect('exit')
#         question = Question.random_question(Question, exp)
#         request.session["question"]=question.id_q
#         request.session['time_start'] = (timezone.now() - timezone.datetime(1900, 1, 1, tzinfo=timezone.utc)).seconds
#         return render(request, 'polls/test.html', {'question': question, 'button_exit':button_exit, 'count':count+1})


#     def post(self, request):
#         pass