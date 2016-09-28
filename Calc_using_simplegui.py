import simplegui


def inp1(inp):
    global op
    op=int(inp)
def inp2(inp):
    global st
    st=int(inp)
    
def add():
    global op,st
    print op+st
def sub():
    
    global op,st
    print op-st
def mul():
    
    global op,st
    print op*st
def div():
    
    print op/st

frame=simplegui.create_frame("Calculator",500,500)

frame.add_input("Enter number",inp1,50)
frame.add_input("Enter number",inp2,50)

frame.add_button("+",add,50)
frame.add_button("-",sub,50)
frame.add_button("*",mul,50)
frame.add_button("/",div,50)

frame.start()

