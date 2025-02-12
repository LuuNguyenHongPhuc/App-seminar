import datetime
import uuid

from django.db import models

from EventUser.models import CustomUser
class EventModelManager(models.Manager):
    def get_all_event(self):
        return self.all()
    def delete(self,id):
        event =self.filter(id=id)
        if event:
            event.delete()
            return True
        return False
    def incr_view(self,id):
        event =self.filter(id=id).first()
        if event:
            event.views +=1
            event.save()
    def add_user_join(self,event_id,user_id):
        user =CustomUser.objects.filter(id=user_id).first()
        event =self.filter(id=event_id).first()
        if user and event:
            event.join.add(user)
            event.save()
    def get_popular_event(self,limit):
        events= self.all().order_by('-views')[:limit]
        return events
    
    def get_recent_events_limited(self, limit):
        # Lọc các sự kiện theo thời gian tạo (create_at) và giới hạn theo số lượng
        events = self.all().order_by('-create_at')[:limit]
        return events
    
    


class Categories(models.Choices):
    MUSIC = "Music"
    SPORTS = "Sports"
    EDUCATION = "Education"
    TECHNOLOGY = "Technology"
    ART = "Art"
    THEATER = "Theater"
    FOOD = "Food"
    FITNESS = "Fitness"
    TRAVEL = "Travel"
    FASHION = "Fashion"
    BUSINESS = "Business"
    HEALTH = "Health"
    LITERATURE = "Literature"
    SCIENCE = "Science"
    HISTORY = "History"
    GAME ="Game"

class EventModel(models.Model):
    id =models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)
    title =models.CharField(max_length=100,default="")
    describe =models.TextField(default="")
    type =models.CharField(choices=Categories.choices,max_length=25)
    create_at =models.DateTimeField(auto_now_add=True)
    start_time =models.DateField()
    thumb =models.ImageField(upload_to="thumb/")
    end_time =models.DateField()
    map_ifram =models.CharField(max_length=266,null=True)
    video =models.FileField(upload_to="video/",null=True)
    author =models.CharField(max_length=266)
    price =models.IntegerField(default=0)
    locate =models.CharField(max_length=266)
    address =models.CharField(max_length=266)
    qr_code =models.ImageField(upload_to="qr-code/")
    facebook_link =models.CharField(max_length=266)
    instagram_link =models.CharField(max_length=266)
    phone =models.CharField(max_length=266)
    max_join =models.IntegerField(default=0)
    current_join =models.IntegerField(default=0)
    view =models.IntegerField(default=0)
    join =models.ManyToManyField(CustomUser,name="events")
    describe_one =models.TextField(null=True)
    describe_two =models.TextField(null=True)
    objects =EventModelManager()
    def is_active(self):
        today = datetime.now().date()
        return self.start_time< today < self.end_time

class BoxImage(models.Model):
    id =models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)
    id_event =models.UUIDField(null=True, blank=True)
    img =models.ImageField(upload_to="event/")
