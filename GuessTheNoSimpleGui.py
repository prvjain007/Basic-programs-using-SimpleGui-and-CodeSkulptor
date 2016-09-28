import simplegui
import random
def new_game():
    range100()
    
def range100():
    global r,c
    c=0
    r=random.randrange(0,100)
    
    
def gs(gs):
    global r,c
    c=c+1
    gs=int(gs)
    if gs<r:
        print("Higher")
    elif gs>r:
        print("lower")
    else :
        print "Congrats you won",gs,"is right number"
        new_game()
    if c is 7:
        print "You failed"
        new_game()

new_game()
f=simplegui.create_frame("Guess the number",300,300)
f.add_button("Range",range100,100)
f.add_input("Enter a guess",gs,100)

