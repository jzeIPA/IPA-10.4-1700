from django.conf.urls import url
from django.conf.urls import include
from django.contrib.auth.views import login, logout, password_change_done
from django.core.urlresolvers import reverse
from benutzeraccounts import views

#alle URLs die aufrubar sind, werden hier aufgelistet. Die Views-Funktionen werden angesprochen

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'benutzeraccounts/login.html'}, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^profil/$', views.profile, name='profile'),
    url(r'^profil/bearbeiten/$', views.edit_profile, name='edit_profile'),
    url(r'^passwort_wechseln/$', views.change_password, name='change_password'),
    url(r'^passwort_wechseln/erledigt/$', password_change_done, {'template_name': 'benutzeraccounts/change_password_done.html'}, name='change_password_done'),
]
