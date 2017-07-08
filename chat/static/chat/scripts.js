function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

var csrftoken = getCookie('csrftoken');

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

window.onload = function() {
    var d = $('#inner_messages');
    d.scrollTop(d.prop("scrollHeight"));
    updateMessages();
}

function postMessage(){
    var content = document.getElementById('send_message').value;
    var chatroom_id = document.getElementById('chatroom_id').value;
    var send_url = "/chat/" + chatroom_id + "/send_message/";
    var csrftoken = getCookie('csrftoken');
    $.ajax(
    {
        url: send_url,
        type: "POST",
        data: { 'chat': chatroom_id, 'content': content },
        success: updateMessages(),
        complete: function(){
            document.getElementById('send_message').value = "";
        }
    }
    );
}

function updateMessages() {
    var csrftoken = getCookie('csrftoken');
    var chatroom_id = document.getElementById('chatroom_id').value;

    $.ajax(
    {
        url: "/chat/update_messages/",
        headers: {
            'X-CSRFToken': csrftoken,
        },
        type: "GET",
        data: { 'chat': chatroom_id },
        success: function(data){
                var msgsString = '';
                $.each(data, function(key, value) {
                        var d = new Date(value['date_sent']);
                        msgsString += d.toDateString() + " " + d.toLocaleTimeString();
                        msgsString += '-';
                        msgsString += value['sender_name'];
                        msgsString += ' : ';
                        msgsString += value['content'];
                        msgsString += '<br>'
                    });
                $('#inner_messages').html(msgsString);
                var d = $('#inner_messages');
                d.scrollTop(d.prop("scrollHeight"));
            },
        complete: function() {
                setTimeout(updateMessages, 1500);
            }
    }
    );
}

function sendMessageAndUpdate(){
    var xHttp = new XMLHttpRequest();
}
