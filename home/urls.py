from django.urls import path
from home import views

urlpatterns = [
    path('', views.example_new, name='example_new'),
    path('example_old/', views.example_old, name='example_old'),
    path('example_broken/', views.example_broken, name='example_broken'),
    path('example_used/', views.example_used, name='example_used'),
]