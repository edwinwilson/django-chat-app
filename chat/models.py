from django.db import models
from django.utils import timezone
import  datetime

class User(models.Model):
    name = models.CharField(max_length=20)
    date_created = models.DateTimeField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ChatRoom(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    users = models.ManyToManyField(User, through="Membership", related_name="users")
    date_created = models.DateTimeField()
    encryption = models.BooleanField(default=False)
    persistence = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_room = models.ForeignKey(ChatRoom)
    date_joined = models.DateTimeField()

    def __str__(self):
        return self.user.name + " member of " + self.chat_room.name + " since " + str(self.date_joined)


class Message(models.Model):
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    recipient = models.ManyToManyField(User, verbose_name="list of recipients", related_name="recipient", blank=True)
    date_sent = models.DateTimeField()
    content = models.CharField(max_length=2000)
    encrypted = models.BooleanField(default=False)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_sent <= now
