from django.conf.urls import url
from . import views

app_name = 'chat'
urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'create_chatroom/$', views.create_chatroom, name='create_chatroom'),
    url(r'create_user/$', views.create_user, name='create_user'),
    url(r'update_messages/$', views.update_messages, name='update_messages'),
    url(r'list_chatrooms/$', views.ListChatroomsView.as_view(), name='list_chatrooms'),
    url(r'user/(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='display_user'),
    url(r'chatroom/(?P<chatroom_id>[0-9]+)/$', views.display_chatroom, name='display_chatroom'),
    url(r'(?P<chatroom_id>[0-9]+)/send_message/$', views.send_message, name='send_message'),
]
