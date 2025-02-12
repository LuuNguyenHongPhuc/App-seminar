from django.contrib import messages
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import View
from datetime import datetime
from EventTicket.util import getContextUser,create_new_action
from EventUser.forms import RegisterForm, LoginForm, UserInfoForm
from EventUser.models import CustomUser

from django.contrib.auth import authenticate,login,logout

from util.models import UserAction

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, "register.html", {"form": form})

    def post(self, request, *args, **kwargs):
        storage = messages.get_messages(request)
        storage.used = True
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

        
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, "Email đã tồn tại. Vui lòng dùng email khác.")
                return render(request, "register.html", {"form": form})

            new_user = CustomUser.objects.create(email=email, password=password, **kwargs)

           

            if new_user:
                messages.success(request, "Tạo tài khoản thành côn")
                return redirect("login")

        messages.error(request, "Có lỗi xảy ra. Vui lòng kiểm tra lại thông tin.")
        return render(request, "register.html", {"form": form})
        


class AdminRegister(View):
    def get(self,request,*args,**kwargs):
        form =RegisterForm()
        return  render(template_name="Admin-register.html",request=request)

class LoginView(View):
    def get(self, request):
        storage = messages.get_messages(request)
        storage.used = True
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        storage = messages.get_messages(request)
        storage.used = True
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
         
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Đăng nhập thành công!")
                # return redirect("home")  
                return redirect(reverse("home", args=[0])) 

            else:
                messages.error(request, "Email hoặc mật khẩu không chính xác.")

      
        return render(request, "login.html", {"form": form})
class UserView(View):
    def create_content(self,user,*args, **kwargs):
        formatted_date = user.date_join.strftime("%d-%m-%Y vào lúc %H:%M:%S")
        recent_active =UserAction.objects.filter(user_id=user.id).all()
        return {
            "full_name":user.full_name,
            "email":user.email,
            "avt":user.avt,
            "birth":user.date_of_birth,
            "phone":user.phone_number,
            "locate":user.address,
            "is_admin":user.is_superuser,
            "cccd":user.user_id,
            "created":formatted_date,
            "last_login":user.last_login,
            "recent_active":recent_active
            
        }
    def get(self,request):
        user =getContextUser(request=request)
        
        return render(template_name="userinfo.html",request=request,context=self.create_content(user=user))


class UseerFix(View):
    def get(self, request):
        
        user = getContextUser(request=request)
        form = UserInfoForm(instance=user)
        return render(request, "user-fix.html", {"form": form, "user": user})

    def post(self, request):
        
        user = getContextUser(request=request)
        print(user.email)
        form = UserInfoForm(request.POST, request.FILES, instance=user)  
        if form.is_valid():
            form.save()
            create_new_action(user_id=user.id,title="Thay đổi Thông tin người dùng",describe="Người dùng thay đổi thông tin người dùng",)
            
            ## save hành động của người dùng vào db
            return redirect("info")  
        return render(request, "user-fix.html", {"form": form, "user": user})

class Logout(View):
    def post(self,request):
        logout(request=request)
        return redirect("login")
        

