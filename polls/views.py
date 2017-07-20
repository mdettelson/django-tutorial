# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#  from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.db.models import F
from polls.models import Question, Choice


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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html',
                      {'question': question,
                       'error_message': "You didn't select a choice",
                       })
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing with
        # POST data.  This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
