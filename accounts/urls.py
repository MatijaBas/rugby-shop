from django.conf.urls import url, include
from accounts import urls_reset
from .views import index, register, profile, logout, login,  return_policy, delivery, terms_conditions, subscribe_mail

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
    url(r"return-policy/", return_policy, name="return-policy"),
    url(r"delivery/", delivery, name="delivery"),
    url(r"terms-conditions/", terms_conditions, name="terms-conditions"),
    url(r"(?P<mail>\w+)/subscribe", subscribe_mail, name="subscribe_mail"),
]
