import machine
import _thread
from time import sleep
import sys
import menu as mn
import ssd1306


class Button:
    def __init__(self, pinnb, fonction):
        self.p = machine.Pin(pinnb, machine.Pin.IN, machine.Pin.PULL_UP)
        self.f = fonction
        
        _thread.start_new_thread(self.allwaysrun, ())

    def istouch(self):
        if not self.p.value():
            return True
        else:
            return False

    def allwaysrun(self):
        while True:
            if self.istouch():
                self.f()
                

def addnb():
    nb[2].add()
    
    nb[1]=True
    sleep(0.5)
def runcodenb():
    nb[2].run()
    nb[1]=True
    sleep(0.5)
nb=[0,False,mn.menu(["test1","test2","code1","code2","test1","test2","code1","code2"],"rs")]
bt = Button(4, addnb)
btok=Button(19,runcodenb)
lamp=machine.Pin(15,machine.Pin.OUT)
l=False
nb[2].show()
while True:
    if(nb[1]):
        
        #show(nb[0])
        nb[2].show()
        nb[1]=False



