from django.urls import path

from . import views

# home view
urlpatterns = [
    path('index/', views.index, name = 'pst_index'),
]