from django.urls import path
from . import views

app_name="landing"

urlpatterns = [
    path('', views.coming_soon, name='coming_soon'),
    path("subscribe/", views.subscribe, name="subscribe"),
]