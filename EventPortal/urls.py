from django.shortcuts import redirect
from django.urls import path

from EventPortal import views

urlpatterns =[
 path('home/', lambda request: redirect('/home/0/')),  
    path('home/<int:page>/', views.UserHome.as_view(), name='home'),
    path("list/",views.ListEvent.as_view(),name="list-event"),
    path("creator/",view=views.AdminPanel.as_view(),name="creator")
    
]