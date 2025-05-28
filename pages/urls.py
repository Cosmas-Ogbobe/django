# pages/urls.py
from django.urls import path
from .views import HomePageView

urlpatterns = [
path('', HomePageView.as_view(), name='home'),
path('about/', HomePageView.as_view(template_name='about.html'), name='about'),
]