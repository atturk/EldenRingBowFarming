from directkeys import PressKey, ReleaseKey, Mouse, W, J, E, F, G, Q, P, SPACE
import time, keyboard, threading, os

def keySequence(keyDurationDict:dict[int:list[float, int]]) -> None: # {key:[duration, amount]}
    for key, details in keyDurationDict.items():
        duration:float = details[0]
        amount:int = details[1]
        for _ in range(amount):
            PressKey(key)
            time.sleep(duration)
            ReleaseKey(key)
            time.sleep(0.1)

def sprint(duration) -> None:
    PressKey(W)
    PressKey(SPACE)
    time.sleep(duration)
    ReleaseKey(SPACE)
    ReleaseKey(W)

def finish() -> None:
    while True:
        time.sleep(0.01)
        if keyboard.is_pressed("enter"):
            os._exit(0)

def main() -> None:
    degrees:int = 20
    cycle:int = 1
    for j in range(1,6):
        print(f"{j}...")
        time.sleep(1)
    while True:
        print(cycle)
        keySequence({G:[0.1, 1], F:[0.1, 2], E:[0.1, 2]})
        time.sleep(5)
        #------
        Mouse(-23*degrees,20*degrees)
        sprint(3)
        Mouse(-90*degrees,10*degrees)
        sprint(0.3)
        time.sleep(0.1)
        Mouse(-20*degrees,-5*degrees)
        time.sleep(0.5)
        #------
        PressKey(J)
        time.sleep(1)
        keySequence({Q:[0.1, 1], P:[0.5, 1]})
        time.sleep(5)
        keySequence({Q:[0.1, 1]})
        ReleaseKey(J)
        time.sleep(0.5)
        Mouse(160*degrees,-30*degrees)
        keySequence({W:[0.1, 1]})
        sprint(7)
        cycle+=1
        

if __name__ == "__main__":
    threads = [threading.Thread(target=main, daemon=True), threading.Thread(target=finish, daemon=False)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
