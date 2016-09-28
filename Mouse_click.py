import simplegui
import math

w=450
h=300
bpos=[w/2,h/2]
brad=20
blist=[]
def click(pos):
    global bpos
    blist.append(pos)
def draw(c):
    global bpos,brad,blist
    for bpos in blist:
        c.draw_circle(bpos,brad,1,"Red")
    
    
f=simplegui.create_frame("Ball",w,h)
f.set_canvas_background("White")
f.set_mouseclick_handler(click)
f.set_draw_handler(draw)
f.start()