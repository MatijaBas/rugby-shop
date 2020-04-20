from django.conf.urls import url
from .views import get_review, review_content, create_or_edit_review

urlpatterns = [
    url(r'^$', get_review, name='get_review'),
    url(r'^(?P<pk>\d+)/$', review_content, name='review_content'),
    url(r'^add/$', create_or_edit_review, name='add_review'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_review, name='edit_review'),
]
