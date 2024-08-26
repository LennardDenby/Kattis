from collections import deque
import sys

leftDeque = deque()
rightDeque = deque()

def push_back(x):
    rightDeque.append(x)
    balance()

def push_front(x):
    leftDeque.appendleft(x)
    balance()
    
def push_middle(x):
    leftDeque.append(x)
    balance()

def get(i):
    if i >= len(leftDeque):
        print(rightDeque[i-len(leftDeque)])
    else:
        print(leftDeque[i])

def balance():
    if len(leftDeque) > len(rightDeque) + 1:
        rightDeque.appendleft(leftDeque.pop())
    elif len(rightDeque) > len(leftDeque):
        leftDeque.append(rightDeque.popleft())

def main():
    sys.stdin.readline()
    
    for linje in sys.stdin:
        linjeSplit = linje.split(" ")
        kommando = linjeSplit[0]
        verdi = int(linjeSplit[1])
        
        if kommando == "push_back":
            push_back(verdi)
        elif kommando == "push_front":
            push_front(verdi)
        elif kommando == "push_middle":
            push_middle(verdi)
        elif kommando == "get":
            get(verdi)
        
if __name__ == '__main__':
    main()