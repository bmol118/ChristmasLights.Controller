
class Frame:

    def __init__(self):
        self.frameBuf = []
        self.duration = 1

    def append(self, r,g,b):
        #print(f"Appending {r},{b},{g}")
        self.frameBuf.append((r,g,b))
        
    def set_duration(self, whole, fraction):
        var = str(whole) + '.' + str(fraction)
        #print("Setting Duration to:", var)
        self.duration = float(var)
        



        