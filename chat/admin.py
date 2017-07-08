from django.contrib import admin

from .models import ChatRoom
from .models import User
from .models import Membership
from .models import Message

admin.site.register(ChatRoom)
admin.site.register(User)
admin.site.register(Membership)
admin.site.register(Message)
