from events.models import Match, Bet
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .form import CreditCardField


def index(request):
    all_matches = Match.objects.all()
    context = {
        'all_matches': all_matches,
    }
    return render(request, 'events/index.html', context)


def detail(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    return render(request, 'events/detail.html', {'match': match})


def results(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    return render(request, 'events/results.html', {'match': match})


def bet(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    try:
        bets_made = match.bet_set.get(pk=request.POST['bet'])

    except (KeyError, Bet.DoesNotExist):
        return render(request, 'events/detail.html', {
            'match': match,
            'error_message': "You didn't select a choice.",
        })
    else:
        bets_made.bets += 1
        bets_made.is_betted = True
        bets_made.money_bet = request.POST['money_spent']
        bets_made.save()

        return HttpResponseRedirect(reverse('events:results', args=(match.id,)))


def credit_card(request):
    form = CreditCardField()
    if request.method == 'POST':
        form = CreditCardField(request.POST)
        if form.is_valid():
            deposit = form.cleaned_data['amountDeposit']
            print(deposit)
    return render(request, 'form.html', {'form': form})


