from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.views import View
from app.util import get_current_user
from django.shortcuts import render, redirect
from .froms import RegisterForm, LoginForm  # Import form
from django.contrib.auth import login,logout
@login_required
def home(request):
    if request.user.is_authenticated:

        return render(request, 'home.html', {'message': ""})
    return redirect('/login')
def dangky(request,):
    if request.method == 'POST':
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
           
            password = form.cleaned_data.get("password1")
            password = make_password(password)

            
            user = form.save(commit=False)
            user.password = password  
            user.save() 
            
            avatar =form.cleaned_data.get('avatar')
            if avatar:
                print("đã lấy được avatar từ phía form")
                user.avatar= avatar
                user.save()
                print("lưu thành công avatar vào db")
         
            login(request, user)

            messages.success(request, 'Registration successful!')
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, "user/register.html", {'form': form})
def dangnhap(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print("lay form thanh cong")
            user = form.authenticate_user() 
            login(request, user)  #
            messages.success( "Đăng nhập thành công!")
            print("dang nhap thanh cong")
            return redirect('/')  
        else:
            messages.error(request, "Thông tin đăng nhập không hợp lệ.")
    else:
        form = LoginForm()

    return render(request, 'user/login.html', {'form': form})

def logout_view(request):
    logout(request)  
    messages.success(request, "Đăng xuất thành côn")
    return redirect('login') 


class UserInfo(View):
    template_link ='user/Userinfo.html'
    def get(self, request):
        
        now_user =get_current_user(request=request)
        context ={
            'user':now_user
        }
        if now_user is not None:

            context ={
            
            'user':now_user

            }
        return render(request, self.template_link,context=context)
    def post(self,request):
        now_user =get_current_user(request=request)
        