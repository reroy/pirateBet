from django.contrib import admin

from .models import Bet, Match, UserBank, UserBet


class BetMatch(admin.TabularInline):
    model = Bet
    extra = 3


class MatchesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Team 1', {'fields': ['first_team']}),
        ('Team 2', {'fields': ['second_team']}),
    ]

    list_display = ('match_title', )
    inlines = [BetMatch]


class UserBets(admin.TabularInline):
    model = UserBet
    extra = 3


class MatchesBets(admin.ModelAdmin):
    list_display = ('user', 'user_amount', )
    inlines = [UserBets]


admin.site.register(Match, MatchesAdmin)
admin.site.register(UserBank, MatchesBets)
