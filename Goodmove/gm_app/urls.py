from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('enter', views.enter),
    path('logout', views.logout),
    # path('choices', views.choices),
    path('search', views.search),
    path('details/<int:movie_id>', views.details)
    # path('details', views.movie_details)


]
