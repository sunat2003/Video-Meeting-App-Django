from django.urls import path
from videoMeating_App import views

urlpatterns = [
    path('',views.home_view,name="home"),
    path('register/', views.register_view,name='register'),
    path('login/', views.login_view,name='login'),
    path('dashbord/',views.dashbord,name="dashbord"),
    path('videocall/',views.videoMeeting_view,name="videocall"),
    path('logout/',views.login_view,name="logout"),
    path('join/',views.join_room_view,name="join")
]