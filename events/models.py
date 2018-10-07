from django.db import models
from teams.models import Club


class Match(models.Model):

    def allTeams():
        all_star = ()
        for x, y in enumerate(Club.objects.all()):
            all_star += ((str(x), y.team_name),)
        return all_star

    first_team = models.CharField(max_length=1, choices=allTeams())
    second_team = models.CharField(max_length=1, choices=allTeams())

    def __str__(self):
        return '{} vs {}'.format(self.get_first_team_display(), self.get_second_team_display())

    def match_vs(self):
        anounce_match = Match.objects.filter(id=self.id)
        if anounce_match:
            return '{} vs {}'.format(self.get_first_team_display(), self.get_second_team_display())
        return None

    match_vs.short_description = 'All matches'


class Koef(models.Model):
    bet_options = (
        ('1', 'first'),
        ('X', 'draw'),
        ('2', 'second')
    )
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    factor = models.FloatField(default=1, blank=False)
    bets = models.IntegerField(default=0)
    bet_place = models.CharField(max_length=1, choices=bet_options)



