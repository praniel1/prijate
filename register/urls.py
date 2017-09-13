from django.conf.urls import url
from . import views
app_name = 'register'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^index3', views.index3, name='index3'),
    url(r'^register',views.client_register, name='client_register'),
    #url(r'^login', views.client_login, name='client_login')
]