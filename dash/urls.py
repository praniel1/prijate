from . import views
from django.conf.urls import url
app_name = 'dash'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user_profile$', views.user_profile, name='user_profile'),
    url(r'^pic$', views.upload_pic, name='pic'),
    url(r'^logout_user$', views.logout_user, name='logout_user')
]