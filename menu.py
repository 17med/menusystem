import machine
import ssd1306
import math

i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C, external_vcc=False)
class element:
    def __init__(self,text,action=None):
        self.text=text
        self.nb=0
    def titlestr(self,t):
        x=16-len(t)
        if(x%2==1):
            x-=1
            
        x=x//2
        
        print(" "*x+t+" "*x)
        return " "*x+t+" "*x
    def title(self):
        x = 0
        y = 0
        width = 120
        height = 16
        color = 1
        radius = 2
        oled.fill_rect(x + radius, y, width - (2 * radius), height, color)
        oled.fill_rect(x, y + radius, radius, height - (2 * radius), color)
        oled.fill_rect(x + width - radius, y + radius, radius, height - (2 * radius), color)
        self.draw_circle(x + radius, y + radius, radius, color)
        self.draw_circle(x + width - radius - 1, y + radius, radius, color)
        self.draw_circle(x + radius, y + height - radius - 1, radius, color)
        self.draw_circle(x + width - radius - 1, y + height - radius - 1, radius, color)
        x = 1
        y = 1
        width = 118
        height = 14
        color = 1  # 1 for white, 0 for black
        oled.fill_rect(x, y, width, height, color)
        oled.text(self.titlestr(self.text), 1, 5,0)
    
    def active(self,nb):

        x = 0
        y = 21+(nb*23)
        width = 100
        height = 20
        color = 1
        radius = 2
        oled.fill_rect(x + radius, y, width - (2 * radius), height, color)
        oled.fill_rect(x, y + radius, radius, height - (2 * radius), color)
        oled.fill_rect(x + width - radius, y + radius, radius, height - (2 * radius), color)
        self.draw_circle(x + radius, y + radius, radius, color)
        self.draw_circle(x + width - radius - 1, y + radius, radius, color)
        self.draw_circle(x + radius, y + height - radius - 1, radius, color)
        self.draw_circle(x + width - radius - 1, y + height - radius - 1, radius, color)
        x = 1
        y =22+(nb*23)
        width = 98
        height = 18
        color = 0  # 1 for white, 0 for black
        oled.fill_rect(x, y, width, height, color)
        oled.text(self.text, 7, (nb*23)+26)

        pass
    def passif(self,nb):

        oled.text(self.text, 7, (nb*23)+26)

    def draw_circle(self,x_center, y_center, radius, color):
        global oled
        for i in range(int(0.8 * radius), radius + 1):
            y = y_center - i
            arc = int(math.sqrt(radius ** 2 - i ** 2))
            x_left = x_center - arc
            x_right = x_center + arc
            oled.fill_rect(x_left, y, x_right - x_left, 1, color)
            oled.fill_rect(x_left, y + (2 * i), x_right - x_left, 1, color)
class menu:
    def __init__(self,l,title):
        self.max=16
        self.title=element(self.strresize(title))
        self.e=self.resize(l)
        self.nb=0
        self.e=[element(self.e[i]) for i in range(len(self.e))]
        pass
    def strresize(self,l):
        if(len(l)>self.max):
            return l[:len(l)-2]+".."
        else:
            return l
        
    def arrow(self):
        global oled
        oled.text('*', 120, 20)
        oled.text('*', 120, 55)
        
        oled.fill_rect(123, 22, 1, 35, 1)
        x=(len(self.e)+1)//2
        r=self.nb//2
        oled.fill_rect(122, 28+((25//x)*r), 4, 25//x, 1)

        #oled.fill_rect(x + radius, y, width - (2 * radius), height, color)
    def resize(self,l):
        t=[]
        for i in l:
            t.append(self.strresize(i))
        return t
    def show(self):
        global oled
        oled.fill(0)
        if(self.nb<2):
            self.title.title()
        
        if(self.nb%2==0):
            self.e[self.nb].active(0)
            if(len(self.e)>self.nb+1):
                self.e[self.nb+1].passif(1)
        else:
            
            self.e[self.nb].active(1)
            self.e[self.nb-1].passif(0)
        self.arrow()
        oled.show()
    def add(self):
        if(self.nb+1==len(self.e)):
            pass