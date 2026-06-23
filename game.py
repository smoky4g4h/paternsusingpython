# Based on Skulpt (https://github.com/skulpt/skulpt)
# Approximately corresponds Python 3.6

import turtle
t = turtle.Turtle()
screen = turtle.Screen()
# t.forward(60)
# t.left(120)
# t.circle(100, extent=None, steps=None)

# t.forward(60)
# t.left(120)
# t.circle(100, extent=None, steps=None)

# t.forward(60)
# t.circle(100, extent=None, steps=None)
t.speed(-1)
colors = ["cyan", "blue", "purple", "white", "pink"]

def loe(cnt , a , b):
    t.pencolor("blue")
    t.forward(a)
    t.pencolor("black")
    
    # t.fillcolor(colors)
    if(cnt>100):
        return
    t.pencolor("purple")
    t.forward(a)
    t.pencolor("cyan")
    t.circle(100, extent=None, steps=None)
    t.pencolor("black")
    t.left(b)
    # t.forward(a)
    loe(cnt+1,a,b)
    t.forward(a)
    # t.forward(a)
    # t.left(2*b)
    # t.circle(100, extent=None, steps=None)
    # t.forward(a)
    # # loe(cnt+1,a,b)
    # t.left(2*b)
    # t.forward(2*a)
    # t.circle(100, extent=None, steps=None)
    # t.forward(2*a)
    # loe(cnt+1,a,b)
    
    # t.backward(a)
    t.circle(100, extent=None, steps=None)
    t.left(2*b)
    t.forward(2*a)
    loe(cnt+1,a,b)
    
    # loe(cnt+1,a,b)
loe(0,60,120)
    


# def loe(x,y):
#     if(x<0 or y<0):
#         return
#     for i in range(3):
#         t.left(90)
#         t.forward(x)
#         t.right(90)
#         t.forward(y)
#         t.left(90)
#     loe(x-2,y)
#     loe(x,y-2)
#     # loe(x+1,y+1)
#     # loe(x,y+1)
# loe(100,100)

# def loe(cnt):
#     if(cnt==10):
#         return;
#     t.forward(50)
#     t.left(60)
#     loe(cnt+1)
#     t.forward(50)
#     t.right(60)
#     loe(cnt+1)
#     t.forward(50)
#     # loe(cnt+1)
# loe(0)
# import turtle
# t = turtle.Turtle()
# screen = turtle.Screen()
# t.left(90)
# # t.backward(100)
# # t.
# t.speed(0)
# def tree(length):
#     if length < 10:
#         return
#     t.forward(length)
#     t.left(30)
#     tree(length * 0.7)
#     t.right(60)
#     tree(length * 0.7)
#     t.left(30)
#     t.backward(length)
# t.sety(-100)
# tree(100)
# turtle.done()





