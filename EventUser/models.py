import uuid


from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email không hợp lệ")
        email = self.normalize_email(email)
        user = self.model( email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        user = self.create( email, password, **extra_fields)
        user.save()  
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True,primary_key=True)
    full_name =models.CharField(max_length=266,null=True,blank=True)
    user_id = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth =models.DateField(blank=True,null=True)
    phone_number =models.CharField(max_length=10,null=True,blank=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    address = models.CharField(max_length=255, null=True, blank=True)
    avt = models.ImageField(upload_to="image/avatar",blank=True,null=True)
    date_join = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.email
