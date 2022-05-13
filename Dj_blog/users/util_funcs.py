from .models import Profile
from Dj_blog.settings import BASE_DIR
from users.logger import log
import os

def isLocked(user):
    return user.profile.is_locked

def demote_user(user):
    user.is_staff = False
    user.save()

def lock_user(user):
    profile = Profile.objects.get(user=user)
    profile.is_locked = True
    profile.save()

def unlock_user(user):
    profile = Profile.objects.get(user=user)
    profile.is_locked = False
    profile.save()

    
def delete_profile_pic(profile_pic):
    try:
        pic_url = BASE_DIR+profile_pic.url
        if(pic_url.endswith("defaultImage.png")):
            pass
        else:
            os.remove(pic_url)
            log("profile pic has been deleted")
    except Exception as ex:
        log("no pic"+str(ex))
