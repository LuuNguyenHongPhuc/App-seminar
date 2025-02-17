from django import forms
from Event.models import BoxImage, EventModel

class EventCreatorForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = [
           "title", "describe", "type", "start_time", "end_time", "thumb",
 "map_ifram", "address", "facebook_link",
    "instagram_link", "phone",
    "describe_one",
    "describe_two",
    "video"
   
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "title-label", "placeholder": "Nhập tiêu đề sự kiện"}),
            "describe": forms.Textarea(attrs={"class": "describe-label", "placeholder": "Mô tả sự kiện"}),
            "type": forms.Select(attrs={"class": "type-label"}), 
            # "start_time": forms.SelectDateWidget(attrs={"class": "date-input"}),
            # "end_time": forms.SelectDateWidget(attrs={"class": "date-input"}),
            "thumb": forms.ClearableFileInput(attrs={"class": "thumb-label",}),
           
            "map_ifram": forms.TextInput(attrs={"class": "map-label", "placeholder": "Nhúng bản đồ Google Maps"}),
           
            "address": forms.TextInput(attrs={"class": "address-label", "placeholder": "Nhập địa chỉ cụ thể"}),
            "facebook_link": forms.URLInput(attrs={"class": "facebook-label", "placeholder": "Nhập link Facebook"}),
            "instagram_link": forms.URLInput(attrs={"class": "instagram-label", "placeholder": "Nhập link Instagram"}),
            "phone": forms.TextInput(attrs={"class": "phone-label", "placeholder": "Nhập số điện thoại liên hệ"}),
             
        }
        labels ={
            "thumb":"lưu ý ảnh thumb phải là ảnh có chất lượng full hd"
        }





class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True
##
class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result
##
class Images(forms.ModelForm):
    images = MultipleFileField(label='chọn tối thiếu 10 ảnh', required=False,widget=MultipleFileInput(attrs={'multiple': 'multiple'}))
    class Meta:
        model = BoxImage
        fields = []
    
