from django.urls import path
from . import views
from .views import (
    AnouncementListView,
    AnouncementDetailView,
    AnouncementCreateView,
    AnouncementUpdateView,
    UserAnouncementListView,
    AnouncementDeleteView
)

urlpatterns = [
    path('latest-posts/', views.latest_posts, name='sidebar_latest_posts'),
    
    path('anouncements/', views.anouncements, name='sidebar_anouncements'),
    
    path('weather/', views.weather, name='sidebar-weather'),
    
    path('', AnouncementListView.as_view(), name='sidebar_anouncement_list'),
    
    path('user/<str:username>', UserAnouncementListView.as_view(), name='user-anouncements'),
    
    path('anouncement/new/', AnouncementCreateView.as_view(), name='anouncement-create'),
    
    path('anouncement/<int:pk>/', AnouncementDetailView.as_view(), name='anouncement-detail'),
    
    path('anouncement/<int:pk>/update/', AnouncementUpdateView.as_view(), name='anouncement-update'),
    
    path('anouncement/<int:pk>/delete/', AnouncementDeleteView.as_view(), name='anouncement-delete'),
]
