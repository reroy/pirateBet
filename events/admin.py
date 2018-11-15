from django.contrib import admin

from .models import Bet, Match, UserBank, UserBet


def disable_match(ModelAdmin, request, queryset):
    queryset.update(is_active=False)


def enable_match(ModelAdmin, request, queryset):
    queryset.update(is_active=True)


disable_match.short_description = "Disable selected matchs"
enable_match.short_description = "Enable selected matchs"


class BetMatch(admin.TabularInline):
    model = Bet
    extra = 3


class MatchesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Team 1', {'fields': ['first_team']}),
        ('Team 2', {'fields': ['second_team']}),
        ('Status', {'fields': ['is_active']}),
    ]
    actions = [enable_match,disable_match]
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
