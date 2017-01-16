from django.shortcuts import render, get_object_or_404
from .models import Question, Choice

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from django.utils import timezone
# from django.template import loader if alternate method used

'''
def index(request):
    latestQuestionList = Question.objects.order_by('-pub_date')[:5]

    context = {
        'latestQuestionList': latestQuestionList,
    }

    ''''''
    alternate method
    template = loader.get_template('polls/index.html')

        return HttpResponse(template.render(context, request))
    ''''''
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    ''''''long method
      try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
    ''''''

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


    def results(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/results.html', {'question': question})



'''


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latestQuestionList'
    #  index template outputs no polls are available is no Question

    def get_queryset(self):
        #  returns that of time past only
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    # since the model is Question default variable in question

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):  # POST['choice'] raies key error
        # redisplay list
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "you didnot select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # prevent multiple voting by redirect
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
