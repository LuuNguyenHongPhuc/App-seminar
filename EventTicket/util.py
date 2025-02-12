from datetime import datetime
from django.contrib.auth.decorators import login_required

from util.models import UserAction

def getContextUser(request):
    user =request.user
    if user:
        
        return user
    
    return None




def create_new_action(user_id,title,describe):
    action = UserAction(
            user_id=user_id,
            title=title,
            describe=describe,
            time=datetime.now())
    action.save()