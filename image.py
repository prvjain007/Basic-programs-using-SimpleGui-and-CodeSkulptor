import simplegui
import math
im=simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg")

w,h,s=1521,1818,3

canw=w//s
canh=h//s
magsize=120
magpos=[canw/2,canh/2]

def click(pos):
	global magpos
	magpos=list(pos)
	
def draw(c):
	c.draw_image(im,[w//2,h//2],[w,h],[canw//2,canh//2],[canw,canh])
	
	mapc=[s*magpos[0],s*magpos[1]]
	mapr=[magsize,magsize]
	magc=magpos
	magr=[magsize,magsize]
	c.draw_image(im,mapc,mapr,magc,magr)	

f=simplegui.create_frame("Ball",w,h)
f.set_canvas_background("White")
f.set_mouseclick_handler(click)
f.set_draw_handler(draw)
f.start()