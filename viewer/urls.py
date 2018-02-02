from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^display/$', views.display, name='display'),
    url(r'^mol_view/$', views.mol_view, name='mol_view'),
    url(r'^img_from_pk/$', views.img_from_pk, name='img_from_pk'),
    url(r'^prot_from_pk/(?P<pk>[0-9]+)/$', views.prot_from_pk, name='prot_from_pk'),
    url(r'^mol_from_pk/(?P<pk>[0-9]+)/', views.mol_from_pk, name='mol_from_pk'),
    url(r'^post_view/$', views.post_view, name='post_view'),
    url(r'^get_view/$', views.get_view, name='get_view'),
]