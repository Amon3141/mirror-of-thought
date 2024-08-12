from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
  path('', views.notes, name='notes'),
  path('get_response/', views.get_response, name='get_response'),
]