from django.conf.urls import url
from . import views
app_name = 'register'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^index2', views.index2, name='index2'),
    url(r'^index3', views.index3, name='index3'),
    url(r'^register',views.client_register, name='client_register'),
    url(r'^login', views.client_login, name = 'client_login'),
    url(r'^org_login', views.org_login, name='org_login'),
    url(r'^org_register', views.org_register, name='org_register')
]