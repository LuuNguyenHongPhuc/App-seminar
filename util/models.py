import base64
from io import BytesIO
from django.db import models



import uuid
import qrcode



class UserAction(models.Model):
    id =models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)
    user_id =models.CharField(default="",max_length=266)
    title =models.CharField(max_length=256,null=True)
    describe =models.CharField(max_length=256,null=True)
    time =models.DateTimeField(null=True)


class QrCheckObject(models.Manager):
    def add(self, user_id, event_id):
        if not self.filter(user_id=user_id, event_id=event_id).exists():
            qr = self.create(event_id=event_id, user_id=user_id)
            qr_code =createQrcode(user_id=user_id,event_id=event_id)
            qr.qr_img =qr_code
            qr.save()
            return  qr_code
        return None

    def checkQr(self, user_id, event_id):
        qr = self.filter(user_id=user_id, event_id=event_id)
        if qr.exists():
            self.da_tham_gia =True
            self.save()
            return True
        return False

class QrCheckEvent(models.Model):
    id =models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)
    event_id =models.UUIDField(default="")
    user_id =models.UUIDField(default="")
    qr_img =models.ImageField(upload_to="qr-code",null=True)
    da_tham_gia =models.BooleanField(default=False)
    objects =QrCheckObject()
    


def createQrcode(user_id, event_id):
    
    qr_data = f"user_id:{user_id}, event_id:{event_id},mess:ve tham gia su kien "


    qr = qrcode.QRCode(
        version=1,  
        error_correction=qrcode.constants.ERROR_CORRECT_L, 
        box_size=10,  
        border=4  
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    
    qr_image = qr.make_image(fill="black", back_color="white")


    buffer = BytesIO()
    qr_image.save(buffer, format="PNG")
    qr_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return qr_base64 