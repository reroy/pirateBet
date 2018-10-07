from django.db import models

from django.utils.html import format_html


class Club(models.Model):
    team_name = models.CharField(max_length=20)
    team_logo = models.ImageField(upload_to='teams/logos/', blank=False)

    def __str__(self):
        return self.team_name

    def image_tag(self):
        return format_html('<img src="%s" width="100" height="100" />' % self.team_logo.url)

    image_tag.short_description = 'Logo'

#   @classmethod
#   def get_all_teams(cls):
#       return list(cls.objects.values_list('id', 'team_name'))
