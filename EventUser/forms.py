from django import forms

from EventUser.models import  CustomUser


class RegisterForm(forms.ModelForm):
    class Meta:
        model =CustomUser
        fields =["email","password"]
        widgets ={
            "email" :forms.TextInput(attrs={"class":"email_label"}),
            "password": forms.PasswordInput(attrs={"class": "password_label"})
        }



class LoginForm(forms.Form):
    email = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username'
        }),
        label="Username"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        }),
        label="Password"
    )


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        exclude = ["password", "user_permissions", "groups","last_login"]
         ## them tat ca cac truong trong form ngoai tru các truong nay