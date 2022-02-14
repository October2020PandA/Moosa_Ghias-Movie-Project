// function socket(){
//     var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
//     var room_socket = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/movieroom" + window.location.pathname);

// }
$(function() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var room_socket = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/movieroom" + window.location.pathname);
    console.log('run');
    room_socket.onmessage = function(message) {
        var data = JSON.parse(message.data);
        var chat = $("#chroomat")
        var ele = $('<tr></tr>')

        ele.append(
            $("<td></td>").text(data.timestamp)
        )
        ele.append(
            $("<td></td>").text(data.handle)
        )
        ele.append(
            $("<td></td>").text(data.message)
        )
        
        chat.append(ele)
    };

    // $("#roomform").on("submit", function(event) {
    //     var message = {
    //         handle: $('#handle').val(),
    //         message: $('#message').val(),
    //     }
    //     chatsock.send(JSON.stringify(message));
    //     $("#message").val('').focus();
    //     return false;
    // });
});