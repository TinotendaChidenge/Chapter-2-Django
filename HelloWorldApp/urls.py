from django.urls import path
from .views import hello_wprld

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
