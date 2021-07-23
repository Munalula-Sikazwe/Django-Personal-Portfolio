from django.urls import path
from .views import MainView
app_name = 'portfolio'
urlpatterns = [
    path('',MainView.as_view(),name='home')
]