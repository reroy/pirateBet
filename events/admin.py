from django.contrib import admin

from .models import Koef, Match


class KoefMatch(admin.TabularInline):
    model = Koef
    extra = 3


class MatchesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Team 1', {'fields': ['first_team']}),
        ('Team 2', {'fields': ['second_team']}),
    ]

    list_display = ('match_vs', )
    inlines = [KoefMatch]




admin.site.register(Match, MatchesAdmin)
