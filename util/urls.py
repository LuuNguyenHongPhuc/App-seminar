from django.urls import path
from util import views



urlpatterns = [
     
    path("check-in/",view=views.Checkin.as_view(),name="check-in")

]
