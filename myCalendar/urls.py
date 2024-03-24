from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='sidebar-calendar'),
    
    path('update-calendar/<int:year>/<int:month>/', views.update_calendar, name='update-calendar'),
]
