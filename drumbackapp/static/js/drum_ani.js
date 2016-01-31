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

max = 9;
middle_score = 5;
current_score = 5;
org_size = 150;
var middle_x = 200;


function drawHand(score) {
    var diff = score - middle_score;

    if (diff <= -4) diff = -4;
    else if (diff >= 4) diff = 4;
    var like_width = org_size * (1 + diff / max);
    var like_height = org_size * (1 + diff / max);
    var unlike_width = org_size * (1 - diff / max);
    var unlike_height = org_size * (1 - diff / max);
    $("#like").css("width", like_width).css("height", like_height);
    $("#unlike").css("width", unlike_width).css("height", unlike_height);

    //$('.pic').animate(
    //    {'margin-left': 1}, animationSpeed, function(){
    //        animationComplete = true;
    //    });
}

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
        current_score = current_score + 1;
        drawHand(current_score);
    }
    if (right) {
        right_audio.play();
        current_score = current_score - 1;
        drawHand(current_score);
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