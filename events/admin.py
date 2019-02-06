from django.contrib import admin
import random
from .models import Bet, Match, UserBank, UserBet
from django.contrib.auth.models import User
from decimal import Decimal


def disable_match(ModelAdmin, request, queryset):

    global userBet
    booty = 0
    users = User.objects.all()
    admin_user = User.objects.get(username='admin')
    for match in queryset:

        a = ['1', '2', 'X']
        b = random.choice(a)

        for bet in match.bet_set.all():
            if bet.bet_type == b:
                print(b)
                bet.winning_bet = True
                bet.save()

    queryset.update(is_active=False)

    if request.method == 'POST':
        for match in queryset:
            if not match.is_active:
                for bet in match.bet_set.all():

                    if not bet.winning_bet:
                        for user in users:
                            for userBet in user.userbank.userbet_set.all():
                                if userBet.bet_id == bet.id and userBet.bet_status == 'X':
                                    userBet.bet_status = '0'
                                    userBet.save()
                        booty += bet.money_bet
                        print(booty)

                    elif bet.winning_bet:
                        for user in users:
                            if user.username != 'admin':
                                for userBet in user.userbank.userbet_set.all():
                                    if userBet.bet_id == bet.id and userBet.bet_status == 'X':
                                        userBet.bet_status = '1'
                                        userBet.save()
                                        user.userbank.user_amount += userBet.money_bet*Decimal(bet.factor)
                                        user.save()
                                        print('user win: ' + str(userBet.money_bet*Decimal(bet.factor)))
                        print('bet id: ' + str(bet.id))
                        print(str(userBet.money_bet * Decimal(bet.factor)))
        admin_user.userbank.user_amount += Decimal(booty)
        admin_user.save()


disable_match.short_description = "End selected matches"


def enable_match(ModelAdmin, request, queryset):
    for match in queryset:
        for bet in match.bet_set.all():
            if bet.winning_bet:
                bet.winning_bet = False
                bet.save()
    queryset.update(is_active=True)


enable_match.short_description = "Enable selected matches"


def deactivate_match(ModelAdmin, request, queryset):
    queryset.update(is_active=False)
    users = User.objects.all()

    if request.method == 'POST':
        for match in queryset:
            for bet in match.bet_set.all():
                for user in users:
                    for userBets in user.userbank.userbet_set.all():
                        if userBets.bet_id == bet.id:
                            user.userbank.user_amount += userBets.money_bet
                            user.save()
                            bet.money_bet -= userBets.money_bet
                            bet.save()
                            userBets.delete()


deactivate_match.short_description = "Deactivate selected matches"


def activate_match(ModelAdmin, request, queryset):
    queryset.update(is_active=True)

    if request.method == 'POST':
        for match in queryset:
            for bet in match.bet_set.all():
                bet.winning_bet = False
                bet.bets = 0
                bet.money_bet = 0
                bet.save()


activate_match.short_description = "Activate selected matches"


class BetMatch(admin.TabularInline):
    model = Bet
    extra = 3


class MatchesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Team 1', {'fields': ['first_team']}),
        ('Team 2', {'fields': ['second_team']}),
        ('Status', {'fields': ['is_active']}),
    ]
    actions = [enable_match, disable_match, activate_match, deactivate_match]
    list_display = ('match_title', 'is_active', )
    inlines = [BetMatch]


class UserBets(admin.TabularInline):
    model = UserBet
    extra = 3


class MatchesBets(admin.ModelAdmin):
    list_display = ('user', 'user_amount', )
    inlines = [UserBets]


admin.site.register(Match, MatchesAdmin)
admin.site.register(UserBank, MatchesBets)
