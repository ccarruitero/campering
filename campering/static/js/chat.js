(function(){
    var box     = PUBNUB.$('box');
    var input   = PUBNUB.$('input');
    var channel = 'chat';

    // HANDLE TEXT MESSAGE
    function chat_receive(text) {
        box.innerHTML = (''+text).replace( /[<>]/g, '' ) +
            '<br>' + box.innerHTML;
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
