# from swampdragon.route_handler import ModelRouter
# from swampdragon import route_handler
# from threading import Thread
# import serial
#
# from tornado.ioloop import PeriodicCallback
from swampdragon.pubsub_providers.data_publisher import publish_data

import serial
import subprocess
import re

from tornado.ioloop import PeriodicCallback

pcb = None
ser = None

port = '/dev/cu.usbmodem1411'
serialArduino = serial.Serial(port, 9600)
likeCount = 0
unlikeCount = 0


def play(audio_file_path):
    subprocess.call(["ffplay", "-nodisp", "-autoexit", audio_file_path])


def broadcast_sys_info():
    global likeCount, unlikeCount
    # while True:
    #     valueRead = serialArduino.readline()
    #     choiceSearch = re.search('LIKE|UNLIKE', str(valueRead))
    #     try:
    #         choice = choiceSearch.group(0)
    #         if choice == "LIKE":
    #             likeCount += 1
    #             print(choice)
    #             print(likeCount)
    #             # play('like.wav')
    #             publish_data('sysinfo', {
    #                 'cpu': likeCount,
    #                 'kb_received': unlikeCount,
    #                 'kb_sent': unlikeCount,
    #             })
    #         elif choice == "UNLIKE":
    #             unlikeCount += 1
    #             print(choice)
    #             print(unlikeCount)
    #             # play('unlink.wav')
    #             publish_data('sysinfo', {
    #                 'cpu': likeCount,
    #                 'kb_received': unlikeCount,
    #                 'kb_sent': unlikeCount
    #             })
    #     except AttributeError:
    #         pass

    global pcb, ser
    if pcb is None:
        pcb = PeriodicCallback(broadcast_sys_info, 30)
        pcb.start()
    valueRead = serialArduino.readline()
    choiceSearch = re.search('LIKE|UNLIKE', str(valueRead))
    try:
        choice = choiceSearch.group(0)
        if choice == "LIKE":
            likeCount += 1
            print(choice)
            print(likeCount)
            # play('like.wav')
            publish_data('sysinfo', {
                'like': likeCount,
                'dislike': unlikeCount
            })
        elif choice == "UNLIKE":
            unlikeCount += 1
            print(choice)
            print(unlikeCount)
            # play('unlink.wav')
            publish_data('sysinfo', {
                'like': likeCount,
                'dislike': unlikeCount
            })
    except AttributeError:
        pass