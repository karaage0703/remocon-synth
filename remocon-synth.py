# -*- coding: utf-8 -*-
import sys
import serial
import time
import json
from ring import SequenceBuffer
import threading
from psonic import *
 
ser = serial.Serial("/dev/ttyACM0", 9600, timeout = 1)
cord = SequenceBuffer(5)

class SequenceThread(threading.Thread):
    "Sequence of music"
    def __init__(self, t):
        super(SequenceThread, self).__init__()
        self.t = t

    def run(self):
        while True:
            time.sleep(self.t)
            play(cord.get())


if __name__ == "__main__":
    cord = SequenceBuffer(5)

    sequence = SequenceThread(0.5)
    sequence.start()

    while True:
        try:
            ser.write(b"c\r\n")
            time.sleep(1)
            remocon_com = ser.readline()
            if b'Time Out' in remocon_com or b'Ready' in remocon_com:
                print("No Signal")
            else:
                print("Get Signal")
                print(remocon_com)

                ser.write(b"I,2\r\n")
                IR_str = ser.readline()

                if b'...' in IR_str:
                    print("error")
                else:
                    ir_numb = int(IR_str, 16)
                    print("ir_numb=" + str(ir_numb))
                    music_numb = ir_numb % 5
                    print("music_numb=" + str(music_numb))
                    if music_numb == 0:
                        cord.add(72)
                        # play(72)
                    if music_numb == 1:
                        cord.add(75)
                        # play(75)
                    if music_numb == 2:
                        cord.add(77)
                        # play(77)
                    if music_numb == 3:
                        cord.add(79)
                        # play(79)
                    if music_numb == 4:
                        cord.add(82)
                        # play(82)

        except KeyboardInterrupt:
            print('keyboard interrupt')
            ser.close()
            break
