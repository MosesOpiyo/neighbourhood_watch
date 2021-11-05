from django.urls import path
from . import views

urlpatterns = [
    path('',views.register,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('home/',views.home,name='home'),
    path('new_hood/',views.new_hood,name='new_hood'),
    path('hood/<int:pk>',views.single_hood,name='hood'),
    path('new_business/',views.new_business,name='new_business'),
    path('event/',views.add_event,name='event')

    
]