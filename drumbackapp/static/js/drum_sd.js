/**
 * Created by mengzhang on 1/31/16.
 */


left = 0;
right = 0;
up = 0;
down = 0;

left_audio = $("#left_voice")[0];
right_audio = $("#right_voice")[0];
up_audio = $("#up_voice")[0];
down_audio = $("#down_voice")[0];


swampdragon.onChannelMessage(function (channels, message) {
    left = message.data.left_t;
    right = message.data.right_t;
    up = message.data.up;
    down = message.data.down;
    left_audio.load();
    right_audio.load();
    down_audio.load();
    up_audio.load();
    if (left) {
        left_audio.play();
    }
    if (right) {
        right_audio.play();
    }
    if (up) {
        up_audio.play();
    }
    if (down) {
        down_audio.play();
    }
});

swampdragon.ready(function() {
    swampdragon.subscribe('sys','sysinfo', null);
});