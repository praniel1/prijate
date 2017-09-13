from . import views
from django.conf.urls import url
app_name = 'dash'
urlpatterns = [
    url(r'^(?P<user>\w+)$', views.index, name='index')
]