from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sundmused', views.sundmused, name='sundmused'),
    path('<str:leht>', views.muud, name='muud')
]