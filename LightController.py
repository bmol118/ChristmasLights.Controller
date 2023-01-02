import Frame
import LightStrip
import time


class Controller:

    def __init__(self, path, width, height, framecount, skipInitialization=False):
        self.file = open(path,"rb")
        self.width = width
        self.height = height
        self.framecount = framecount
        self.frames = []
        self.skipInitialization = skipInitialization
        self.LightStrip = LightStrip.LightStrip() if not skipInitialization else None

    def getFrames(self):
        framesize = self.width * self.height

        frameindex = 0
        while(frameindex <= self.framecount):
            print(f'frameindex: {frameindex} framecount:{self.framecount}')
            #print(f"frameindex {frameindex}")
            byteindex = 0
            self.frames.append(Frame.Frame())
            while byteindex < framesize * 3:
                red = int.from_bytes(self.file.read(1),"big")
                #print(f"ByteIndex: {byteindex} RED {red}")
                byteindex +=1
                green =  int.from_bytes(self.file.read(1),"big")
                #print(f"ByteIndex: {byteindex} GREEN {green}")
                byteindex +=1
                blue =  int.from_bytes(self.file.read(1),"big")
                #print(f"ByteIndex: {byteindex} BLUE {blue}")
                byteindex +=1
                self.frames[frameindex].append(red,green,blue)
            whole = int.from_bytes(self.file.read(1),"big")
            #print(whole)
            fraction = int.from_bytes(self.file.read(1),"big")
            #print(fraction)
            #print(f"Duration: {whole}.{fraction}")
            self.frames[frameindex].set_duration(whole,fraction)
            frameindex += 1
            
    

    def start(self):
        for frame in self.frames:
            if not self.skipInitialization:
                self.LightStrip.update(frame)
            else:
                print(f'This is where it would render the frame{frame}')
            # offset for time it takes to read next frame
            time.sleep(frame.duration)

        