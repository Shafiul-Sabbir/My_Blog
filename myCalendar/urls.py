from django.urls import path
from . import views

urlpatterns = [
    # path('home/<int:year>/<int:month>/', views.home, name='calendar-home'),
    path('home/', views.home, name='calendar-home'),
    path('update-calendar/<int:year>/<int:month>/', views.update_calendar, name='update-calendar'),
]
