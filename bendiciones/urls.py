from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('bendita-salud/', views.ejercicios, name='ejercicios'),
     path('bendita-salud/ejercicios', views.ejercicios, name='ejercicios'),
      path('bendita-salud/nutricion', views.nutricion, name='nutricion'),
    path('bendita-academia/', views.card2, name='card2'),
    path('bendito-espíritu/', views.card3, name='card3'),
    path('inteligencia-artificial/', views.card4, name='card4'),
]