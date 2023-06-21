from django.urls import path
from . import views
app_name = 'Productapp'
urlpatterns = [
    path('search', views.search, name='search'),
    ]