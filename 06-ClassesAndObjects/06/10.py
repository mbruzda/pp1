class Tv:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0
    
    def on(self):
        self.is_on = True
        
    def off(self):
        self.is_on = False
        
    def show_status(self):
            
        if not self.is_on:
            print("Telewior jest wyłączony")
        else:
            if self.channel_no <= len(self.channels):
                print("Telewizor jest właczony, kanal:", self.channel_no, f"({self.channels[self.channel_no-1]}), glosnosc:", self.volume)
            else:
                print("Telewizor jest właczony, kanal:", self.channel_no,", glosnosc:", self.volume)
            
    
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
    
    def set_channels(self):
        self.channels = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", "Nat Geo"]
    
    def show_channels(self):
        print("Lista kanalow TV:")
        j=1
        for i in self.channels:
            print(j, i)
            j-=-1
        if not self.channels:
            print("BRAK")
    
    def vol_up(self):
        if self.volume<10:
            self.volume+=1
            
    def vol_down(self):
        if self.volume > 0:
            self.volume-=1
        
        
            
t1 = Tv()
t1.show_status()
t1.on()
t1.show_status()
t1.vol_up()
t1.vol_up()
t1.show_channels()
t1.set_channels()
t1.show_status()
t1.show_channels()
t1.set_channel(5)
for i in range(5):
    t1.vol_down()
t1.show_status()
t1.set_channel(7)
t1.show_status()
t1.off()
