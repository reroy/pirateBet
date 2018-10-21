from django.contrib import admin

from .models import Bet, Match


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


admin.site.register(Match, MatchesAdmin)
