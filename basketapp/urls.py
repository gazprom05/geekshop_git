from django.urls import re_path
import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    re_path(r'^$', basketapp.basket, name='view'),
    re_path(r'^add/(?P<pk>\d+)/$', basketapp.add, name='add'),
    re_path(r'^remove/(?P<pk>\d+)/$', basketapp.remove, name='remove'),
    re_path(r'^edit/(?P<pk>\d+)/(?P<value>\d+)/$', basketapp.edit),

]
