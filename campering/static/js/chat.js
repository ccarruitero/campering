(function(){
    var box     = PUBNUB.$('box');
    var input   = PUBNUB.$('input');
    var channel = 'chat';

    // HANDLE TEXT MESSAGE
    function chat_receive(text) {
      var boxMessage = document.createElement('div');
      var message = document.createElement('div');

      boxMessage.setAttribute('class', 'box-message');
      message.setAttribute('class', 'message');

      message.innerHTML = text;
      box.Message.appendChild(message);
      box.appendChild(boxMessage);
    }

    // OPEN SOCKET TO RECEIVE TEXT MESSAGE
    PUBNUB.subscribe({
        channel : channel,
        message : chat_receive
    });

    // SEND TEXT MESSAGE
    PUBNUB.bind( 'keyup', input, function(e) {
        (e.keyCode || e.charCode) === 13 && PUBNUB.publish({
            channel : channel,
            message : input.value,
            x       : (input.value='')
        });
    } );
})();
