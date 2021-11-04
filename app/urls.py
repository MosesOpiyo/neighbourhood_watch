from django.urls import path
from . import views

urlpatterns = [
    path('',views.register,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('home/',views.home,name='home'),
    path('neighbour_input/',views.Neigbourhood_input,name='neighbour_input'),
    path('location_input/',views.location_input,name='location')
]