from vpython import *
from players import *
import numpy as np
import datetime
import random

def roll(target,deg):
    target.rotate(angle=radians(deg))
    target.velocity = rotate(target.velocity,
                             angle=radians(deg),axis=target.axis)
def pitch(target,deg):
    deg = 0 - deg
    target.rotate(angle=radians(deg),axis=target.up)
    target.velocity = rotate(target.velocity,
                             angle=radians(deg),axis=target.up)

def yaw(target,deg):
    target.yawdir = rotate(target.axis,angle=radians(90),axis=target.up)
    target.rotate(angle=radians(deg),axis=target.yawdir)
    target.velocity = rotate(target.velocity,
                            angle=radians(deg),axis=target.yawdir)
    
def throttle(target,targetThrottle):
    target.velocity.mag = targetThrottle

def setMidPoint(point):
    point.pos = (vector((player1.pos + player2.pos))/2)
    return point.pos

def laserInitialize(lasers,player,i):
    random.seed = scene.seednum
    print(str(scene.seednum)+"/"+str(random.seed))
    lasers[i].visible=True
    lasers[i].pos = player.pos
    lasers[i].axis = player.axis
    lasers[i].velocity = player.velocity
    
    lasers[i].velocity.mag = 1
    lasers[i].velocity = lasers[i].velocity * 2.5
    
    roll(lasers[i],(i*50))
    pitch(lasers[i],2)
    #lasers[i].velocity = rotate(lasers[i].velocity,radians(2*i),lasers[i].axis)

    print(lasers[i].velocity)

    
def drift(target,pitch,roll,yaw):
    target.yawdir = rotate(target.axis,angle=radians(90),axis=target.up)
    target.rotate(angle=radians(yaw),axis=target.yawdir)
    target.rotate(angle=radians(roll))
    pitch = 0 - pitch
    target.rotate(angle=radians(pitch),axis=target.up)
    
    
def endGame():
    sleep(500)


def vectorizeString(string):
    return np.array(np.matrix(string)).ravel()




timestamp = datetime.datetime.now().strftime("%Y")+ datetime.datetime.now().strftime("%m")+ datetime.datetime.now().strftime("%d")+ datetime.datetime.now().strftime("%H")+ datetime.datetime.now().strftime("%M")+ datetime.datetime.now().strftime("%S")

fileName = "./Runs" + "./" + timestamp + ".txt"
def T(s):
    print(s.text)
    fileName = "./Runs" + "./" + s.text + ".txt"
    print(fileName)

filename = winput(pos=scene.title_anchor,type="string",
                  text=timestamp,bind=T,width=200)

def writeToSaveFile():
        
    scene.stepCounter = scene.stepCounter + 1
    saveFile = open(fileName,"a+")
    if scene.stepCounter == 1:
          saveFile.write("seednum: "+str(scene.seednum)+"\n")  
    saveFile.write("Step: " + str(scene.stepCounter) + "\n")
    saveFile.write("player1.pos: " + str(player1.pos))
    saveFile.write("\n")
    saveFile.write("player1.axis: " + str(player1.axis))
    saveFile.write("\n")
    saveFile.write("player1.velocity: " + str(player1.velocity))
    saveFile.write("\n")
    saveFile.write("player1.yawdir: " + str(player1.yawdir))
    saveFile.write("\n")
    saveFile.write("player1.throttle: " + str(player1.throttle))
    saveFile.write("\n")
    saveFile.write("player1.pitch: " + str(player1.pitch))
    saveFile.write("\n")
    saveFile.write("player1.yaw: " + str(player1.yaw))
    saveFile.write("\n")
    saveFile.write("player1.roll: " + str(player1.roll))
    saveFile.write("\n")
    saveFile.write("player1.isShooting: " + str(player1.isShooting))
    saveFile.write("\n")
    saveFile.write("player1.isBoosting: " + str(player1.isBoosting))
    saveFile.write("\n")
    
    saveFile.write("player2.pos: " + str(player2.pos))
    saveFile.write("\n")
    saveFile.write("player2.axis: " + str(player2.axis))
    saveFile.write("\n")
    saveFile.write("player2.velocity: " + str(player2.velocity))
    saveFile.write("\n")
    saveFile.write("player2.yawdir: " + str(player2.yawdir))
    saveFile.write("\n")
    saveFile.write("player2.throttle: " + str(player2.throttle))
    saveFile.write("\n")
    saveFile.write("player2.pitch: " + str(player2.pitch))
    saveFile.write("\n")
    saveFile.write("player2.yaw: " + str(player2.yaw))
    saveFile.write("\n")
    saveFile.write("player2.roll: " + str(player2.roll))
    saveFile.write("\n")
    saveFile.write("player2.isShooting: " + str(player2.isShooting))
    saveFile.write("\n")
    saveFile.write("player2.isBoosting: " + str(player2.isBoosting))
    saveFile.write("\n")
    saveFile.close()
    
def setPos(message):
    linesplit = message.split('\n')
    i = 0
    poses = [0,0,0,0,0,0,0,0]
    for l in linesplit:
        if i!=0:
            a,b = l.split(':')
            poses[i-1] = int(b)
        i+=1
    player1.pos = vector(poses[0],poses[1],poses[2])
    yaw(player1,poses[3])
    player2.pos = vector(poses[4],poses[5],poses[6])
    yaw(player2,poses[7])
    return True


c = cone(pos=vector(0,0,0),axis=player1.axis,
                     radius=2,visible=False)
c.velocity = vector(0,0,0)
def findTrajectory(a,b):
    xdif = b.pos.x - a.pos.x
    ydif = b.pos.y - a.pos.y
    zdif = b.pos.z - a.pos.z
    print(xdif,ydif,zdif)
    v2 = vector(0,0,0)
    if xdif < 0:
        v2.x = -1
    elif xdif > 0:
        v2.x = 1
    if ydif < 0:
        v2.y = 1
    elif ydif > 0:
        v2.y = -1
    if zdif < 0:
        v2.z = 1
    elif zdif > 0:
        v2.z = -1

    a.velocity.hat = a.velocity + v2
    a.axis.hat = a.velocity
    
    """
    c.axis = a.axis
    c.velocity = a.velocity
    c.pos = a.pos
    ypr = [0,0,0]
    up1 = degrees(diff_angle(c.up,b.up))
    roll(c,1)
    up2 = degrees(diff_angle(c.up,b.up))
    
    if up2 <= 1:
        ypr[2] = 0
    elif up2 < up1:
        ypr[2] = 1
        
    elif up2 > up1:
        ypr[2] = -1
    roll(c,-1)
    up1 = degrees(diff_angle(c.up,b.up))
    yaw(c,1)
    up2 = degrees(diff_angle(c.up,b.up))
    
    if up2 <= 1:
        ypr[0] = 0
    elif up2 < up1:
        ypr[0] = 1
        
    elif up2 > up1:
        ypr[0] = -1
    yaw(c,-1)
    print(up1,up2,ypr[2])
    return ypr
    """           
    
