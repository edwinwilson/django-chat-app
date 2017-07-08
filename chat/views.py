from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder

from .models import ChatRoom, Message, User


# Create your views here.
class ListChatroomsView(generic.ListView):
    template_name = 'chat/chatrooms.html'
    context_object_name = 'latest_chatrooms'

    def get_queryset(self):
        return ChatRoom.objects.order_by('-date_created')[:10]

def create_chatroom(request):
    return HttpResponse("View for creating a chat room.")

def index_view(request):
    return render(request, 'chat/index.html')

def create_user(request):
    user = User(name=request.POST['user_name'], date_created=timezone.now(), password='')
    user.save()
    request.session['user_name'] = user.name
    return HttpResponseRedirect(reverse('chat:list_chatrooms'))


class DetailsView(generic.DetailView):
    model = User
    template_name = 'chat/user.html'


def display_chatroom(request, chatroom_id):
    chatroom = get_object_or_404(ChatRoom, pk=chatroom_id)
    message_set = Message.objects.filter(chatroom=chatroom_id).order_by('date_sent')
    return render(request, 'chat/chatroom.html', {'chatroom': chatroom, 'messages': message_set})


def update_messages(request):
    if request.method == 'GET':
        if request.is_ajax():
            chatroom_id = request.GET['chat']
            message_set = Message.objects.filter(chatroom=chatroom_id).order_by('date_sent')
            message_list = []
            for row in message_set:
                message_list.append({'date_sent': row.date_sent, 'content': row.content, 'sender_name': row.sender.name})
            mimetype = 'application/json'
            data = json.dumps(message_list, cls=DjangoJSONEncoder)
            return HttpResponse(data, mimetype)


def send_message(request, chatroom_id):
    chatroom_id = request.POST['chat']
    chatroom = get_object_or_404(ChatRoom, pk=chatroom_id)
    new_message = Message(chatroom=chatroom,
                          sender=User.objects.get(name=request.session['user_name']),
                          content=request.POST['content'],
                          date_sent=timezone.now(),
                          encrypted=False)
    new_message.save()
    return HttpResponseRedirect(reverse('chat:display_chatroom', args=(chatroom.id,)))
