from django.shortcuts import render
from django.views import View

from Event.forms import EventCreatorForm, Images
from Event.models import BoxImage, EventModel
from EventTicket.util import getContextUser



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

class EventInfo(View):
    def get(self,request,id):
        context ={}
        event =EventModel.objects.filter(id=id).first()
        
        context["event"]=event
        return render(template_name="eventInfo.html",request=request,context=context)
         
        