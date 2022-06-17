from django.urls import path
from . import views


app_name = "core"


urlpatterns = [
    path('', views.viewer, name='viewer'),
    path('create', views.create, name='create')
]