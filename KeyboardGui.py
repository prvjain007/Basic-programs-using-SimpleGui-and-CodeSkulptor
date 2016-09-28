import simplegui
import random
wid=600
hei=400
r=20

ball_pos=[wid/2,hei/2]
vel=[0,0]
def draw(can):
    global ball_pos,r
    t=random.randrange(1,20)
    ball_pos[0]+=vel[0]
    ball_pos[1]+=vel[1]
    if ball_pos[1] < 0 or ball_pos[1]>hei:
        vel[1]=-vel[1]
    
    if ball_pos[0]<0:
        ball_pos[0]=wid
    elif ball_pos[0]>wid:
        ball_pos[0]=wid
    can.draw_circle(ball_pos,r,t,"Red","White")
   
def keyd(key):
    acc=1
    if key==simplegui.KEY_MAP["left"]:
        vel[0]-=acc
    elif key==simplegui.KEY_MAP["right"]:
        vel[0]+=acc
    elif key==simplegui.KEY_MAP["down"]:
        vel[1]+=acc
    elif key==simplegui.KEY_MAP["up"]:
        vel[1]-=acc        
f=simplegui.create_frame("Circle Play",wid,hei)

f.set_draw_handler(draw)
f.set_keydown_handler(keyd)

f.start()