from django.http import HttpResponse
from django.views import generic
from events.models import Match, Koef
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


def index(request):
    all_matches = Match.objects.all()
    context = {
        'all_matches': all_matches,
    }
    return render(request, 'events/index.html', context)



class DetailView(generic.DetailView):
    model = Match
    template_name = 'events/detail.html'


class ResultsView(generic.DetailView):
    model = Match
    template_name = 'events/results.html'


def bet(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    try:
        selected_choice = match.koef_set.get(pk=request.POST['koef'])
    except (KeyError, Koef.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'events/detail.html', {
            'match': match,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.bets += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('events:results', args=(match.id,)))
