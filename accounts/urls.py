from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.signup_form, name='signup'),
    url(r'^login/$', views.login_form, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
]
