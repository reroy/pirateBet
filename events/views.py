from .models import Match, Bet, UserBank, UserBet, Club
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreditCardField, MatchBetForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from decimal import Decimal


def team_events(request, club_id):
    all_matches2 = set()
    team = list(Club.objects.filter(pk=club_id))[0]
    print(team)
    for match in Match.objects.filter(is_active=True):
        if match.first_team_index == int(club_id) or match.second_team_index == int(club_id):
            all_matches2.add(match.pk)

    all_matches3 = Match.objects.filter(pk__in=all_matches2)

    return render(request, 'events/team_events.html', {'all_matches3': all_matches3, 'team': team})


@login_required
def index(request):
    all_matches = Match.objects.all()
    return render(request, 'events/index.html', {'all_matches': all_matches})


@login_required
def detail(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    return render(request, 'events/detail.html', {'match': match})


@login_required
def results(request, match_id):
    match = get_object_or_404(Match, pk=match_id)

    return render(request, 'events/results.html', {'match': match})


@login_required
def bet(request, match_id):
    user = request.user
    match = get_object_or_404(Match, pk=match_id)

    try:
        bets_made = match.bet_set.get(pk=request.POST['typeBet'])
        if (user.userbank.user_amount - Decimal(request.POST['moneyBet'])) < 0:
            raise ValueError('insufficient funds')
    except (KeyError, Bet.DoesNotExist):
        return render(request, 'events/detail.html', {
            'match': match,
            'error_message': "You didn't select a choice.",
        })
    except ValueError:
        return render(request, 'events/detail.html', {
            'match': match,
            'error_message': "Not enough money.",
        })

    else:
        if request.method == 'POST':
            form = MatchBetForm(request.POST)
            if form.is_valid():
                bets_made.bets += 1
                bets_made.money_bet += form.cleaned_data['moneyBet']
                bets_made.save()

                user.userbank.user_amount -= form.cleaned_data['moneyBet']
                user.userbank.userbet_set.create(
                    money_bet=form.cleaned_data['moneyBet'],
                    bet_type=bets_made.bet_type,
                    match_id=match_id,
                    factor=bets_made.factor,
                    bet_id=bets_made.id
                )
                user.save()

                return HttpResponseRedirect(reverse('events:results', args=(match.id,)))


@login_required
def credit_card(request):
    user = request.user
    match = Match.objects.all()
    form = CreditCardField()
    if request.method == 'POST':
        form = CreditCardField(request.POST)
        if form.is_valid():
            user.userbank.user_amount += form.cleaned_data['amountDeposit']
            user.userbank.total_input += form.cleaned_data['amountDeposit']
            user.save()
            print(user.userbank.user_amount)
    return render(request, 'forms.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def home(request):
    return render(request, 'home.html')
