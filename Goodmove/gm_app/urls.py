from django.urls import path
from . import views

urlpatterns = [
    path('$/', views.user, name='user'),
    path('$/', views.film, name='film'),
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('enter', views.enter),
    path('logout', views.logout),
    path('choices', views.choices),
    path('search', views.search),
    path('details/<int:movie_id>', views.details),
    path('add/<int:movie_id>', views.add),
    path('delete/<int:movie_id>', views.delete)


]

