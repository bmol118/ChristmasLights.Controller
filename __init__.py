import LightController
import Consts
import datetime
import sys
import time
from multiprocessing import Process
import os



def start():
    frame_count = int(sys.argv[1])
    use_time_control = bool(sys.argv[2])
    print(frame_count, type(frame_count))
    controller = LightController.Controller("../LightShowV2.bin", 10, 50, frame_count, False)
    controller.getFrames()
    print('Done Getting Frames')

    start_time = datetime.time(17,20)
    end_time = datetime.time(22,30)

    if use_time_control:
        print('Checking Time')
        while True:
            datetimenow = datetime.datetime.now()
            timenow = datetime.time(datetimenow.hour,datetimenow.minute)
            print(timenow,start_time,end_time)
            if(timenow > start_time and timenow < end_time):
                print('restarting')
                controller.start()
            else:
                time.sleep(60)
    else:
        print('Running Once')
        controller.start()

# p = Process(target=start)
# #p.daemon = True  # <-----
# p.daemon = False
# p.start()
# print('done')

if os.fork():
    print('done')
    sys.exit(0)
else:
    start()
