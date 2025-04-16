from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.db.models import Sum, Max
from .utils import minimax

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

class AllView(generic.ListView):
    model = Question
    template_name = 'polls/all.html'

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def frequency(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = question.get_choices()

    return render(request, 'polls/frequency.html',{
        'question': question,
        'choices': choices,
    })
def statistics(request):
    total_sondages = Question.objects.count()
    total_choix = Choice.objects.count()
    total_votes = Choice.objects.aggregate(Sum('votes'))['votes__sum'] or 0
    moyenne_votes = total_votes / total_sondages if total_sondages > 0 else 0

    # Annoter chaque question avec le total de votes
    questions_avec_votes = Question.objects.annotate(total_votes=Sum('choice__votes'))

    question_populaire = questions_avec_votes.order_by('-total_votes').first()
    question_moins_populaire = questions_avec_votes.order_by('total_votes').first()

    derniere_question = Question.objects.latest('pub_date')

    # Calcul du total de votes pour ces questions
    total_votes_populaire = question_populaire.total_votes if question_populaire else 0
    total_votes_moins_populaire = question_moins_populaire.total_votes if question_moins_populaire else 0

    return render(request, 'polls/statistics.html', {
        'total_sondages': total_sondages,
        'total_choix': total_choix,
        'total_votes': total_votes,
        'moyenne_votes': moyenne_votes,
        'question_populaire': question_populaire,
        'total_votes_populaire': total_votes_populaire,
        'question_moins_populaire': question_moins_populaire,
        'total_votes_moins_populaire': total_votes_moins_populaire,
        'derniere_question': derniere_question,
    })

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))