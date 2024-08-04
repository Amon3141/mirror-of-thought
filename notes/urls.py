from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
  path('', views.main, name='hello'),
  path('<int:n>/', views.sub, name='sub'),
]