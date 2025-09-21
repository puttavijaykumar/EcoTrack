from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_image, name='upload_image'),
    path('results/', views.results, name='results'),
    path('dashboard/', views.dashboard, name='dashboard'),

]