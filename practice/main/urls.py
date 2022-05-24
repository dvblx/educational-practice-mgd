from django.urls import path, include
from . import views
from .views import RegisterUser, LoginUser, logout_user, create_event1, userprofile, usercards

urlpatterns = [
    path('home', views.index, name='home'),
    path('events', views.events, name='events'),
    path('people', views.people, name='people'),
    path('create_event', create_event1.as_view(), name='create_event'),
    path('register', RegisterUser.as_view(), name='register'),
    path('enter', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('event_info/<int:event_id>/', views.event_info, name='event_info'),
    path('success', views.success, name='success'),
    path('success2', views.success2, name='success2'),
    path('userprofile', userprofile.as_view(), name='userprofile'),
    path('moderpage', views.moderpage, name='moderpage'),
]
