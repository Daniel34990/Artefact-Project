from commandes import forward,time
from detect import pair, impair, distance
def Parcoursauto():
    while not(pair()):
        forward(0.4,0.4,0.2)
        time.sleep(0.6)
    while pair() and distance()>21:
        a=distance()
        forward(0.5,-0.5,a/100*0.8)
    while not(pair()):
        forward(0.4,0.4,0.2)
        time.sleep(0.6)
    while pair() and distance()>21:
        a=distance()
        forward(0.5,-0.5,a/100*0.8)
    while not(pair()):
        forward(0.4,0.4,0.2)
        time.sleep(0.6)
    while pair() and distance()>21:
        a=distance()
        forward(0.5,-0.5,a/100*0.8)
    while not(pair()):
        forward(0.4,0.4,0.2)
        time.sleep(0.6)
    while pair() and distance()>21:
        a=distance()
        forward(0.5,-0.5,a/100*0.8)
    
    
    
    
Parcoursauto()