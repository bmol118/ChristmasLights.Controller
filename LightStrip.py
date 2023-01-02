import time
import board
import neopixel
import Consts
import Frame

class LightStrip:

    def __init__(self):
        self.lights = neopixel.NeoPixel(
            board.D18, 
            Consts.NEOPIXEL_LENGTH, 
            pixel_order=Consts.NEOPIXEL_LIGHT_ORDER,
            auto_write=False
            )
    
    def update(self, frame):
        counter = 0
        for rgb in frame.frameBuf:
            if(counter < Consts.NEOPIXEL_LENGTH):
                self.lights[counter] = rgb
            counter += 1
        self.lights.show()

