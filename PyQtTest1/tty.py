#!/usr/bin/env python
# -*-coding:utf-8-*-

import serial
from time import sleep
import json
import threading

class CustomSerial(threading.Thread):
    '''自定义串口类'''
    def __init__(self, com, baud):
        threading.Thread.__init__(self)
        self.s = serial.Serial(com, baud)
        self.pointData = {}
        self.seriesData = {}
        self._hyPower = []
        self._liPower = []
        self._allPower = []
        self.x = []
        self._x = 0

    def run(self):
        while(True):
            try:
                self._x += 1
                j = json.loads(self.s.readline().decode('utf-8'))
                self.pointData = {"HyTemp":j["HyTemp"],
                                  "HyPress":j["HyPress"],
                                  "LiVolt":j["LiVolt"],
                                  "HyVolt":j["HyVolt"]}
                power = j["LiVolt"] * j["TotalCurrent"]
                hyPower = fakeData(j["HyVolt"])
                self._hyPower.append(hyPower)
                self._liPower.append(power - hyPower)
                self._allPower.append(power)
                self.seriesData = {"HyPower":self._hyPower,
                                   "LiPower":self._liPower,
                                   "AllPower":self._allPower,
                                   "x":list(range(self._x))}
            except:
                print("Serial Read ERROR!")
                pass


def fakeData(volt):
    if volt > 33.0:
        volt = 33.0
    elif volt < 19.0:
        volt = 19.0
    return 5.1 * ((volt - 33) ** 2)


if __name__ == "__main__":
    s = CustomSerial("COM4", 115200)
    s.start()
    while(True):
        print(s.seriesData)
        print(s.pointData)
        sleep(1)
