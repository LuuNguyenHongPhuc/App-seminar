from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import AnonymousUser
from Event.models import BoxImage, Categories, EventModel
from EventTicket.util import getContextUser


class UserHome(View):

    def get(self,request, page):
        events = EventModel.objects.get_recent_events_limited(limit=10)
        event =events[page]
        boxs_images =[]
        boxs_images =BoxImage.objects.filter(id_event=event.id).all()
        
        user =getContextUser(request=request)
        if isinstance(user,AnonymousUser):
            user =None
        print(user)
        context ={
            "user":user,
            "event":event,
            "boxs_images":boxs_images
            
        }
        return render(template_name="userhome.html",request=request,context=context)
    
class ListEvent(View):
    def get(self,request,*args,**kwargs):
        user =getContextUser(request=request)
        email_admin =user.email
        print(email_admin)
        return render(template_name="allevent.html",request=request,context={})
    
class AdminPanel(View):
    def get(self,request,):
        user =getContextUser(request=request)
        type_selected = request.GET.get("event_category")  # Lấy giá trị từ URL
        print(type_selected)  # Debug để kiểm tra

        events = EventModel.objects.filter(type__iexact=str(type_selected))

        

        for event in events:
            print(event.title)
        if user.is_superuser:
            return render(template_name= "admin/adminPanel.html",request=request,context={"events":events})
        return render(template_name= "error_template/403.html",request=request,context={})
        