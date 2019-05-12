from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
import events

urlpatterns = [
    url(r'^events/', include(('events.urls', 'events'), namespace='events')),
    url(r'^teams/', include(('teams.urls', 'teams'), namespace='teams')),
    url(r'^home/$', events.views.home, name='home'),
    url(r'^cash/$', events.views.credit_card, name='cash'),
    url(r'^admin/', admin.site.urls),

    url(r'^signup/$', events.views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView, name='login'),
    url(r'^logout/$', auth_views.LogoutView, {'next_page': 'home'}, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
