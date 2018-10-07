from django.contrib import admin

from .models import Club


class TeamsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,   {'fields': ['team_name']}),
        ('Change image', {'fields': ['team_logo']}),
    ]
    list_display = ('team_name', 'team_logo', 'image_tag')
    readonly_fields = ['image_tag']


admin.site.register(Club, TeamsAdmin)
