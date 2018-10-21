from django.db import models
from teams.models import Club


class Match(models.Model):
    first_team = models.CharField(max_length=255)
    second_team = models.CharField(max_length=255)

#   def allTeams():
#       all_star = ()
#       for x, y in enumerate(Club.objects.all()):
#           all_star += ((str(x), y.team_name),)
#       return all_star

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta.get_field('first_team').choices = Club.get_all_teams()
        self._meta.get_field('second_team').choices = Club.get_all_teams()

    def __str__(self):
        return '{} vs {}'.format(self.first_team, self.second_team)

    @property
    def match_title(self):
        return '{} vs {}'.format(self.first_team, self.second_team)

#    def match_vs(self):
#        anounce_match = Match.objects.filter(id=self.id)
#        if anounce_match:
#            return '{} vs {}'.format(self.get_first_team_display(), self.get_second_team_display())
#        return None

    match_title.fget.short_description = 'All matches'


class Bet(models.Model):
    BET_OPTIONS = (
        ('1', 'first'),
        ('X', 'draw'),
        ('2', 'second')
    )
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    factor = models.FloatField(default=1, blank=False)
    bets = models.IntegerField(default=0)
    bet_type = models.CharField(max_length=1, choices=BET_OPTIONS)
    is_betted = models.BooleanField(default=False)
    money_bet = models.IntegerField(default=0)

    def __str__(self):
        return '{}, Bet type: {}, Bet factor: {}, Bets count: {}'.format(
            self.match,
            self.bet_type,
            self.factor,
            self.bet_type,
        )
