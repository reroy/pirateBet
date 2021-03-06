from django.db import models
from teams.models import Club
from django.contrib.auth.models import User
from decimal import Decimal
from django.db.models.signals import post_save
from django.dispatch import receiver


class Match(models.Model):
    first_team = models.CharField(max_length=255)
    second_team = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta.get_field('first_team').choices = Club.get_all_teams()
        self._meta.get_field('second_team').choices = Club.get_all_teams()

    def __str__(self):
        return '{} vs {}'.format(self.first_team, self.second_team)

    @property
    def match_title(self):
        return '{} vs {}'.format(self.first_team, self.second_team)

    @property
    def first_team_logo(self):
        for x in Club.objects.all():
            if self.first_team == x.team_name:
                return x.team_logo.url

    @property
    def second_team_logo(self):
        for x in Club.objects.all():
            if self.second_team == x.team_name:
                return x.team_logo.url

    @property
    def first_team_index(self):
        for x in Club.objects.all():
            if self.first_team == x.team_name:
                return int(x.id)

    @property
    def second_team_index(self):
        for x in Club.objects.all():
            if self.second_team == x.team_name:
                return int(x.id)

    match_title.fget.short_description = 'All matches'


class Bet(models.Model):
    BET_OPTIONS = (
        ('1', 'first'),
        ('X', 'draw'),
        ('2', 'second')
    )
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    factor = models.FloatField(default=1, blank=False)
    winning_bet = models.BooleanField(default=False)
    bets = models.IntegerField(default=0)
    bet_type = models.CharField(max_length=1, choices=BET_OPTIONS)
    money_bet = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))
    bet_users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return '{}, Bet type: {}, Bet factor: {}, Bets count: {}'.format(
            self.match,
            self.bet_type,
            self.factor,
            self.bet_type,
        )


class UserBank(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_amount = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))
    total_input = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return str(self.user) + '\'s bank account '


class UserBet(models.Model):
    BET_OPTIONS = (
        ('1', 'first'),
        ('X', 'draw'),
        ('2', 'second')
    )
    BET_STATUS = (
        ('1', 'win'),
        ('X', 'pending'),
        ('0', 'lost')
    )
    user = models.ForeignKey(UserBank, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    bet_type = models.CharField(max_length=1, choices=BET_OPTIONS)
    money_bet = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))
    factor = models.FloatField(default=1, blank=False)
    bet_id = models.IntegerField(default=0, blank=False)
    bet_status = models.CharField(max_length=1, default='X', choices=BET_STATUS)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserBank.objects.create(user=instance)
    instance.userbank.save()
