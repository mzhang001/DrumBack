# from swampdragon.route_handler import ModelRouter
# from swampdragon import route_handler
# from threading import Thread
# import serial
#
# from tornado.ioloop import PeriodicCallback

from swampdragon.pubsub_providers.data_publisher import publish_data

import serial
import re

from tornado.ioloop import PeriodicCallback

pcb = None
ser = None

port = '/dev/cu.usbmodem1411'
serialArduino = serial.Serial(port, 9600)

upCount = 0
downCount = 0
leftCount = 0
rightCount = 0


def broadcast_sys_info():
    global upCount, downCount, leftCount, rightCount
    global pcb, ser
    if pcb is None:
        pcb = PeriodicCallback(broadcast_sys_info, 100)
        pcb.start()

    valueRead = serialArduino.readline()
    choiceSearch = re.search('UP|DOWN|LEFT|RIGHT', str(valueRead))
    try:
        left_sent = 0
        right_sent = 0
        up_sent = 0
        down_sent = 0
        choice = choiceSearch.group(0)
        print(choice)
        if choice == "UP":
            up_sent += 1
            upCount += 1
        elif choice == "DOWN":
            down_sent += 1
            downCount += 1
        elif choice == "LEFT":
            left_sent += 1
            leftCount += 1
        elif choice == "RIGHT":
            right_sent += 1
            rightCount += 1
        publish_data('sysinfo', {
            'left_t': left_sent,
            'right_t': right_sent,
            'top': up_sent,
            'down': down_sent
        })
    except AttributeError:
        pass
