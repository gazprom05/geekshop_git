
from django.urls import re_path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    re_path(r'^$', adminapp.main, name='main'),
    re_path(r'^user/create/$', adminapp.user_create, name='user_create'),
    re_path(r'^user/update/(?P<pk>\d+)/$', adminapp.user_update, name='user_update'),
    # re_path(r'^user/delete/(?P<pk>\d+)/$', adminapp.user_delete, name='user_delete'),

    # re_path(r'^add/(?P<pk>\d+)/$', adminapp.add, name='add'),
    # re_path(r'^remove/(?P<pk>\d+)/$', adminapp.remove, name='remove'),
    # re_path(r'^edit/(?P<pk>\d+)/(?P<value>\d+)/$', adminapp.edit),

]