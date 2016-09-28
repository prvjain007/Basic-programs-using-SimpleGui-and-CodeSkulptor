#import modules
import simplegui
import random

#global
msg="Daada Mahan Hain"
pos=[50,50]
wid=500
hei=500
interval=20


#handler for text
def update(txt):
	global msg
	msg=txt

#handler for timer
def tick():
	x=random.randrange(0,wid)
	y=random.randrange(0,hei)
	pos[0]=x
	pos[1]=y
#handler to draw 
def draw(can):
	can.draw_text(msg,pos,24,"Red")

#create frame
f=simplegui.create_frame("Home",wid,hei)
t=simplegui.create_timer(interval,tick)
#event handlers
txt=f.add_input("Mesage",update,150)
f.set_draw_handler(draw)
#start frame
f.start()
t.start()

