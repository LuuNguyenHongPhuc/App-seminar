
from django.urls import path

from Event import views

urlpatterns =[
    path("create/",views.EventCreatorView.as_view(),name="create"),
    path("<str:id>",views.EventInfo.as_view(),name="event"),
   
]