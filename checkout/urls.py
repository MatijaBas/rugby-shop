from django.conf.urls import url
from .views import checkout, order_detail

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^order/(?P<order_id>[0-9]+)/$', order_detail, name='order_detail'),
]
