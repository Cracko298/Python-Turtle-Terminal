import turtle as trtl
import os
import time
painter = trtl.Turtle()

# Varriables to Define
penup = "penup"
pendown = "pendown"


forward = "forward"
backward = "backward"
left = "left"
right = "right"
circle = "circle"

help = "help"
cmd = "cmd"
reset = "reset"
cmd_det = "cmd_det"

pensize = "pensize"
pencolor = "pencolor"
turtlesize = "turtlesize"
stamp = "stamp"
shape = "shape"
beginfill = "beginfill"
endfill = "endfill"

# End of Varriables

def begin():  # Clears Screen for Most of the Apllication
    os.system('clear')
    print("For Command List. Type: 'help' or 'cmd'")
    print(" ")


begin()


def Commands():  #Command List for the 'cmd' & 'help' commands
    print(" ")
    print("Command List:")
    print(
        "cmd, help, penup, pendown, forward, backward, left, right, circle, pensize, turtlesize, reset, beginfill, endfill, pencolor, shape, stamp"
    )
    print(" ")
    print("For a More Detailed View on Commands. Type: 'cmd_det'")
    print(" ")
    DemCommands()


def DemCommands():  # Main Program/Script
    while 1 == 1:
        command = input("> ")
        if command == penup:
            painter.penup()
        if command == forward:
            painter.forward(50)
        if command == help:
            Commands()
        if command == cmd:
            Commands()
        if command == pendown:
            painter.pendown()
        if command == backward:
            painter.backward(50)
        if command == left:
            painter.left(90)
        if command == right:
            painter.right(90)
        if command == reset:
            begin()
        if command == pencolor:
            os.system('clear')
            print("What Color of Pen Do You Want?")
            print(" ")
            color = input("> ")
            painter.pencolor(color)
            begin()
        if command == pensize:
            os.system('clear')
            print("What Size of Pen Do You Want?")
            print(" ")
            pen = int(input("> "))
            painter.pensize(pen)
            begin()
        if command == stamp:
            painter.stamp()
        if command == turtlesize:
            os.system('clear')
            print("What Size of Turtle Do You Want?")
            print(" ")
            size = int(input("> "))
            painter.turtlesize(size)
            begin()
        if command == shape:
            os.system('clear')
            print("What Type of Shape Would You Like Your Turtle?")
            print(" ")
            hape = input("> ")
            painter.shape(hape)
            begin()
        if command == cmd_det:
            os.system('clear')
            print("This Command Is Being Worked On...")
            time.sleep(3)
            begin()
        if command == beginfill:
            painter.begin_fill()
        if command == endfill:
            painter.end_fill()
        if command == circle:
            os.system('clear')
            print("What Is The Radius of The Circle?")
            print(" ")
            circlein = int(input("> "))
            painter.circle(circlein)
            begin()


DemCommands()

wn = trtl.Screen()
wn.mainloop()
