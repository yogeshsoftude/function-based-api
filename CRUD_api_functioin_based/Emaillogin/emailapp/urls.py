from django.contrib import admin
from django.urls import path
from emailapp.views import Registration,user_login,get_data,Update_data,Update_data_patch,Delete_data,activate,logout_user,Reset_pass,forget_pass


urlpatterns = [
    
    path('registration/',Registration),
    path('login/',user_login),
    path('get_data/<int:uid>/',get_data),
    path('get_data/',get_data),
    path("Update_data/<int:uid>/",Update_data),
    path("Update_data/",Update_data),
    # path("Update_data_patch/<int:uid>/",Update_data_patch),
    path("Update_data_patch/",Update_data_patch),
    # path('Delete_data/<uid>/',Delete_data),
    path('Delete_data/',Delete_data),
    path('activate/<token>/', activate),
    path("logout_user/",logout_user),
    path("reset_password/",Reset_pass),
    path("forget_password/",forget_pass),
     
]
    
