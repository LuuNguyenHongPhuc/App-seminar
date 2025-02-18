from django.core.files.base import ContentFile
import base64
from io import BytesIO
import uuid
import qrcode
from django.db import models

class UserAction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    user_id = models.CharField(default="", max_length=266)
    title = models.CharField(max_length=256, null=True)
    describe = models.CharField(max_length=256, null=True)
    time = models.DateTimeField(null=True)

class QrCheckObject(models.Manager):
    def add(self, user_id, event_id,email):
        if not self.filter(user_id=user_id, event_id=event_id).exists():
            qr = self.create(event_id=event_id, user_id=user_id)
            # createQrcode trả về tuple (filename, ContentFile)
            filename, qr_file = createQrcode(user_id=user_id, event_id=event_id)
            # Lưu ảnh QR vào trường ImageField
            qr.email =email
            qr.qr_img.save(filename, qr_file, save=False)
            qr.save()
            return qr
        return None

    def checkQr(self, user_id, event_id):
        qr = self.filter(user_id=user_id, event_id=event_id)
        if qr.exists():
            qr_instance = qr.first()
            qr_instance.da_tham_gia = True
            qr_instance.save()
            return True
        return False

class QrCheckEvent(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    email =models.CharField(default="",null=True,max_length=266)
    event_id = models.UUIDField(default="")
    user_id = models.UUIDField(default="")
    qr_img = models.ImageField(upload_to="qr-codes/", null=True)  # Trường ImageField để lưu ảnh
    da_tham_gia = models.BooleanField(default=False)
    objects = QrCheckObject()

def createQrcode(user_id, event_id):
    # Tạo dữ liệu QR
    qr_data = f"user_id:{user_id}, event_id:{event_id}, mess: ve tham gia su kien "

    # Tạo mã QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    # Tạo hình ảnh mã QR
    qr_image = qr.make_image(fill="black", back_color="white")

    # Lưu mã QR dưới dạng ảnh vào bộ nhớ đệm
    buffer = BytesIO()
    qr_image.save(buffer, format="PNG")
    buffer.seek(0)  # Đảm bảo con trỏ bộ nhớ đệm ở đầu

    # Đặt tên tệp cho ảnh QR và trả về tuple (filename, ContentFile)
    filename = f"qr_{user_id}_{event_id}.png"
    return filename, ContentFile(buffer.read())
