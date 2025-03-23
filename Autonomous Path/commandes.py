from adafruit_motorkit import MotorKit
kit = MotorKit(0x40)
import time


def stop_tot():
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0

def forward(speed1,speed2, t) :
    kit.motor1.throttle = speed1
    kit.motor2.throttle = speed2
    time.sleep(t)
    stop_tot()

def backward(speed1,speed2,t):
    kit.motor1.throttle = -speed1
    kit.motor2.thottle = -speed2
    time.sleep(t)
    stop_tot()

def left(speed, t):
    kit.motor1.throttle = speed
    kit.motor2.throttle = -speed
    time.sleep(t)
    stop_tot()

def right(speed, t):
    kit.motor1.throttle = -speed
    kit.motor2.throttle = speed
    time.sleep(t)
    stop_tot()
