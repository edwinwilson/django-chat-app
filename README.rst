

=====
CHAT
=====

Chat is a simple Django app to chat.

Quick start
-----------

1. Add "chat" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'chat',
    ]

2. Include the chat URLconf in your project urls.py like this::

    url(r'^chat/', include('chat.urls')),

3. Run `python manage.py migrate` to create the chat models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a chat (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/chat/ to participate in the chat.
