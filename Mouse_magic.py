import simplegui
import math

w,h,r=450,300,20
blist=[]
bcol="Red"

def dis(p,q):
	return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)
	
def click(pos):
	remove=[]
	for ball in blist:
		if dis(ball,pos)<r:
			remove.append(ball)
			
	if remove==[]:
		blist.append(pos)
		
	else :
	for ball in blist:
		blist.pop(blist.index(ball))
		
def draw(c):
	for ball in blist:
		c.draw_circle([ball[0],ball[1]],r,1,"Black",bcol)
		
