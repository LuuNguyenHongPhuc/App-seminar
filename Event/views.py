from datetime import datetime
from django.shortcuts import render
from django.views import View

from Event.forms import EventCreatorForm, Images
from Event.models import BoxImage, EventModel
from EventTicket.util import getContextUser
from util.models import QrCheckEvent



class EventCreatorView(View):
    def get(self,request,*args, **kwargs):
        form =EventCreatorForm()
        form_images=Images()
        return  render(template_name="eventcreator.html",request=request,context={'form':form,"form_images":form_images})
    def post(self,request):
        form =EventCreatorForm(request.POST,request.FILES)
        form_images =Images(request.POST,request.FILES)
        
        if form.is_valid() and form_images.is_valid():
            user =getContextUser(request=request)
            print("lay duoc form")
            
            event = form.save(commit=False) 
            event.author =user.email
            event.save()  

            
           
            images = request.FILES.getlist("images")
            for image in images:
                new_image =BoxImage.objects.create(id_event=event.id,img=image)
            return  render(template_name="eventcreator.html",request=request,context={"form":form,"form_images":form_images})
        else:
            print(form.errors)
class EventInfo(View):
    def get(self,request,id):
        context ={}
        event =EventModel.objects.filter(id=id).first()
        event_id =event.id
        boxs_images =BoxImage.objects.filter(id_event=event_id).all()
        context["event"]=event
        context["boxs_images"]=boxs_images
        return render(template_name="eventInfo.html",request=request,context=context)
    # dang ky event
    def post(self,request,id):
        
        event =EventModel.objects.filter(id=id).first()
        event_id =event.id
        user =getContextUser(request=request)
        user_id =user.id
        sign_event =QrCheckEvent.objects.add(user_id=user_id,event_id=event_id)
        print("trạng thái đăng ký sự kiện có tên là"+event.title)
        print(sign_event)
        
        boxs_images =BoxImage.objects.filter(id_event=event_id).all()
        context ={
                "event":event,
                "email":          user.email ,
                "time":datetime.now() ,
                "qr_code":sign_event
        }
        return render(template_name="ticket.html",request=request,context=context)
         


class EventFix(View):
    def get(self,request,id):
        event =EventModel.objects.filter(id=id).first()
        form =EventCreatorForm(instance=event)
        event_id =event.id
        
        context ={
            "form":form
        }
        
        return render(template_name="eventfix.html",request=request,context=context)
    def post(self,request,id):
        event =EventModel.objects.filter(id=id).first()
        form = EventCreatorForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            context ={
            
            "form":form
        }
        
        return render(template_name="eventfix.html",request=request,context=context)