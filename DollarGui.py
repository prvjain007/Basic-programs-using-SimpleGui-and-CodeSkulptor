import simplegui
val=0
def draw(canvas):
    global val
    canvas.draw_text(conv(val),[100,100],24,"White")
    

def conv(t):
    
    doll=int(val)
    cent=100*(val-doll)
    return str(doll)+" dollars and "+str(cent)+" cents"
def ivent(text):
    global val
    val=float(text)

f=simplegui.create_frame("Test",400,200)

f.set_draw_handler(draw)

f.add_input("Enter value",ivent,100)

f.start()