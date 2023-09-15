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
        keyPress(F,0.1)
        keyPress(F,0.1)
        keyPress(E,0.1)
        keyPress(E,0.1)
        t.sleep(5)
        Mouse(-118*d1,24*d1,)
        sprint(1)
        PressKey(J)
        t.sleep(0.1)
        PressKey(O)
        t.sleep(0.1)
        keyPress(P,0.1)
        t.sleep(5)
        ReleaseKey(O)
        ReleaseKey(J)
        t.sleep(5)
        cycle+=1
        

if __name__ == "__main__":
    main()


