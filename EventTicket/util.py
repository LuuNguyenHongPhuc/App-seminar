from datetime import datetime
from django.contrib.auth.decorators import login_required

from util.models import UserAction

def getContextUser(request):
    user =request.user
    if user:
        print("trang thai dang dang nhap")
        print("nguoi dung hien tai la"+user.email)
        return user
    print("chua co nguoi dung dang nhap ")
    return None




def create_new_action(user_id,title,describe):
    action = UserAction(
            user_id=user_id,
            title=title,
            describe=describe,
            time=datetime.now())
    action.save()