/**
 * Created by mengzhang on 1/30/16.
 */

var like_elem = document.getElementById("like_text");
var dislike_elem = document.getElementById("dislike_text");

like_click = 0;
unlike_click = 0;
max = 10;
min = -10;
org_size = 200;
org_padding = 800;

//$(document).ready(function () {
//    $("#like").click(function () {
//
//    });
//});
//
//$(document).ready(function () {
//    $("#unlike").click(function () {
//        unlike_click += 1;
//        var diff = like_click - unlike_click;
//        var like_width = org_size * (1 + diff / max);
//        var like_height = org_size * (1 + diff / max);
//        var unlike_width = org_size * (1 - diff / max);
//        var unlike_height = org_size * (1 - diff / max);
//        $("#like").css("width", like_width).css("height", like_height);
//        $("#unlike").css("width", unlike_width).css("height", unlike_height);
//    });
//});

function drawHand() {
    var diff = like_click - unlike_click;
    var like_width = org_size * (1 + diff / max);
    var like_height = org_size * (1 + diff / max);
    var unlike_width = org_size * (1 - diff / max);
    var unlike_height = org_size * (1 - diff / max);
    $("#like").css("width", like_width).css("height", like_height);
    $("#unlike").css("width", unlike_width).css("height", unlike_height);
}

swampdragon.onChannelMessage(function (channels, message) {
    like_elem.innerText = message.data.like;
    dislike_elem.innerText = message.data.dislike;
    like_click = message.data.like;
    unlike_click = message.data.dislike;
    drawHand();
});


swampdragon.ready(function() {
    swampdragon.subscribe('sys','sysinfo', null);
});