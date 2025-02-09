from django.urls import path
from rest_framework.urls import urlpatterns
from django.contrib.auth.views import LogoutView
from EventUser import views

urlpatterns =[
    path('register/', views.RegisterView.as_view(), name="register"),
   path("fix/",views.UseerFix.as_view(),name="fix"),
    path('login/',views.LoginView.as_view(),name="login"),
    path("info/",views.UserView.as_view(),name="info"),
     path("logout/", LogoutView.as_view(), name="logout"),
]