from django.test import TestCase
import datetime
from django.utils import timezone

# Create your tests here.

from .models import Message, ChatRoom, User


class MessageModelTests(TestCase):

    def test_was_published_recently_with_future_message(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        user = User(name='user',
                    date_created=timezone.now(),
                    password='')
        chatroom = ChatRoom(name='chatroom',
                            owner=user,
                            date_created=timezone.now(),
                            )
        future_question = Message(chatroom=chatroom, sender=user,
                                  content='content',
                                  date_sent=time,
                                  encrypted=False)
        self.assertIs(future_question.was_published_recently(), False)
