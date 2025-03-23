from commandes import forward,time, right, left
from detect import pair, impair, distance
def Parcoursauto():
    forward(-0.4,-0.4,1)
    while not(impair()):
        forward(0.5,0.5,0.1)
        time.sleep(0.6)
    while impair() and (distance()>30):
        a=distance()
        forward(0.52,-0.5,a/100*0.8)
    while not(impair()):
        forward(0.5,0.5,0.1)
        time.sleep(0.6)
    while impair() and (distance()>30):
        a=distance()
        forward(0.52,-0.5,a/100*0.8)
    while not(impair()):
        forward(0.5,0.5,0.1)
        time.sleep(0.6)
    while (impair() and (distance()>25)):
        a=distance()
        forward(0.52,-0.5,a/100*0.8)

    forward(0.4,0.4,1.5)
    while not(pair()):
        forward(0.4,0.4,0.1)
        time.sleep(1)
    while pair() and (distance()>30):
        a=distance()
        forward(0.52,-0.5,a/100*0.8)
    while not(pair()):
        forward(0.4,0.4,0.1)
        time.sleep(1.5)
    while pair() and (distance()>30):
        a=distance()
        forward(0.52,-0.5,a/100*0.8)
    while not(pair()):
        forward(0.4,0.4,0.1)
        time.sleep(1.5)
    while pair() and (distance()>30):
        a=distance()
        forward(0.52,-0.5,a/100*0.8)
    while not(pair()):
        forward(0.4,0.4,0.1)
        time.sleep(1)
    while pair():
        a=distance()
        forward(0.52,-0.5,a/100*0.8)
    
