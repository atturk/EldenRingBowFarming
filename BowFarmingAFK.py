import time as t
from directkeys import PressKey, ReleaseKey, W, A, S, D, J, E, F, G, Q, I, O, P, Mouse, UP, DOWN, LEFT, RIGHT, SPACE
import signal
import sys
import keyboard as k
run = True

def keyPress(key, dur):
    exit1()
    PressKey(key)
    exit1()
    t.sleep(dur)
    exit1()
    ReleaseKey(key)
    exit1()
    t.sleep(0.1)     

def sprint(dur):
    exit1()
    PressKey(W)
    exit1()
    PressKey(SPACE)
    exit1()
    t.sleep(dur)
    exit1()
    ReleaseKey(SPACE)
    exit1()
    ReleaseKey(W)
    exit1()

def sprintback(dur):
    exit1()
    PressKey(S)
    exit1()
    PressKey(SPACE)
    exit1()
    t.sleep(dur)
    exit1()
    ReleaseKey(SPACE)
    exit1()
    ReleaseKey(S)
    exit1()

def exit1():
    if k.is_pressed("enter"):
        raise KeyboardInterrupt
def main():
    d=20
    d1=18
    a=3.5
    b=0.9
    c=0.8
    diff=+0.8
    angle=75
    cycle=1
    for j in range(1,6):
            print(j,"...")
            exit1()
            t.sleep(1)
    while run:
        print(cycle)
        keyPress(G,0.1)
        t.sleep(0.1)
        keyPress(F,0.1)
        t.sleep(0.1)
        keyPress(F,0.1)
        t.sleep(0.1)
        keyPress(E,0.1)
        t.sleep(0.1)
        keyPress(E,0.1)
        t.sleep(5)

        #------

        Mouse(-23*d,20*d)
        sprint(3)
        Mouse(-90*d,10*d)
        sprint(0.3)
        t.sleep(0.1)
        Mouse(-20*d,-5*d)
        t.sleep(0.5)
        
        #------
        
        PressKey(J)
        t.sleep(1)
        keyPress(Q,0.1)
        keyPress(P,0.5)
        t.sleep(5)
        keyPress(Q,0.1)
        ReleaseKey(J)
        t.sleep(0.5)
        Mouse(160*d,-30*d)
        keyPress(W,0.1)
        sprint(7)
        cycle+=1
        

if __name__ == "__main__":
    main()


