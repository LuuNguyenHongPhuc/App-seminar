from django.shortcuts import redirect
from django.urls import path

from EventPortal import views

urlpatterns =[
 path('home/', lambda request: redirect('/home/0/')),  
    path('home/<int:page>/', views.UserHome.as_view(), name='home'),
    path("list/",views.ListEvent.as_view(),name="list-event"),
    path("adminpanel/",view=views.AdminPanel.as_view(),name="adminpanel"),
    path("my-ticket/",view=views.MyTicket.as_view(),name="my-ticket"),
    path("joins/<str:id>",view=views.JoinerEvent.as_view(),name="joins"),
    path("about/",view=views.AboutView.as_view(),name="about")
]