from django.conf.urls import url
from . import views


#matches an empty string (http://127.0.0.1:8000) is not considered a string
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]