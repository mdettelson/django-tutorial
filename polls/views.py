# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#  from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from polls.models import Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context_dict = {'latest_question_list': latest_question_list}
    # this and the above template line can be abbreviated to:
    # return render(request, 'polls/index.html', context_dict)
    # using django.shortcuts.render
    return HttpResponse(template.render(context_dict, request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # the following code should only run when
    # a question with the above id exists
    context_dict = {'question': question}
    return render(request, 'polls/detail.html', context_dict)


def results(request, question_id):
    return HttpResponse("You're looking at the results of question {}.".format(question_id))


def vote(request, question_id):
    return HttpResponse("You're voting on question {}.".format(question_id))
