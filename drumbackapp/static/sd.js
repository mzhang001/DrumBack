/**
 * Created by mengzhang on 1/31/16.
 */


swampdragon.onChannelMessage(function (channels, message) {
    like_elem.innerText = message.data.like;
    dislike_elem.innerText = message.data.dislike;
    like_click = message.data.like;
    unlike_click = message.data.dislike;
});

swampdragon.ready(function() {
    swampdragon.subscribe('sys','sysinfo', null);
});