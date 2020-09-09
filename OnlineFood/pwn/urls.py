
from django.urls import path

from pwn import views

urlpatterns = [

    path('',views.showIndex,name='pwn_main'),
    path('pwn_login_check/',views.pwn_login_check,name='pwn_login_check'),
    path('welcome/',views.welcome,name='welcome'),
    path('state/',views.openState,name='state'),
    path('city/',views.openCity,name='city'),
    path('cuisine/',views.openCusine,name='cuisine'),
    path('vendor/',views.openVendor,name='vendor'),
    path('resports/',views.openReporsts,name='reports'),
    path('logout/',views.pwn_login_check,name='logout'),

    path('saveState/',views.saveState,name="saveState"),
    path('updateState/',views.updateState,name="updateState"),
    path('deleteState/',views.deleteState,name="deleteState"),

    path('saveCity/',views.saveCity,name="saveCity"),
    path('updateCity/',views.updateCity,name="updateCity"),
    path('deleteCity/',views.deleteCity,name="deleteCity"),

    path('saveCuisine/', views.saveCuisine, name="saveCuisine"),
    path('updateCuisine/', views.updateCuisine, name="updateCuisine"),
    path('deleteCuisine/', views.deleteCuisine, name="deleteCuisine"),

]
