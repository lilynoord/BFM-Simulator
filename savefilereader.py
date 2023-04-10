from vpython import *
from smallfunctions import *
from players import *
scene.data = []


midPoint = sphere()
midPoint.visible=False
scene.autoscale = False
scene.camera.follow(midPoint)
scene.rater = 100
scene.stepper = 0

def moveStep(step):
    print(step)
    #player1.pos = scene.data[step][0][0]
    #player1.axis = scene.data[step][0][1]
    #player1.velocity = scene.data[step][0][2]
    #player1.yawdir = scene.data[step][0][3]
    player1.throttle = scene.data[step][0][4]
    player1.pitch = scene.data[step][0][5]
    player1.yaw = scene.data[step][0][6]
    player1.roll = scene.data[step][0][7]
    player1.isShooting = scene.data[step][0][8]
    player1.isBoosting = scene.data[step][0][9]
    #player2.pos = scene.data[step][1][0]
    #player2.axis = scene.data[step][1][1]
    #player2.velocity = scene.data[step][1][2]
    #player2.yawdir = scene.data[step][1][3]
    player2.throttle = scene.data[step][1][4]
    player2.pitch = scene.data[step][1][5]
    player2.yaw = scene.data[step][1][6]
    player2.roll = scene.data[step][1][7]
    player2.isShooting = scene.data[step][1][8]
    player2.isBoosting = scene.data[step][1][9]
    player1.visible = True
    player2.visible = True
    p1Left.visible=True
    p1Right.visible=True
    p2Left.visible=True
    p2Right.visible=True
    replayStep()

def replayStep():
    print( scene.stepper)
    scene.visible=True
    deltat = 0.005
    t = 0
    p1ThrottleRate = player1.throttle*deltat
    p1RollRate = player1.roll*deltat
    p1PitchRate = player1.pitch*deltat
    p1YawRate = player1.yaw*deltat
    p2ThrottleRate = player2.throttle*deltat
    p2RollRate = player2.roll*deltat
    p2PitchRate = player2.pitch*deltat
    p2YawRate = player2.yaw*deltat
    if player1.isBoosting:
            if player1.boostTimer <= 5:
                player1.boostTimer = player1.boostTimer + 1
                p1ThrottleRate = 150*deltat
            else:
                player1.boostTimer = 0
                player1.isBoosting = False
                p1ThrottleRate = player1.throttle*deltat
    if player2.isBoosting:
            if player2.boostTimer <= 5:
                player2.boostTimer = player2.boostTimer + 1
                p2ThrottleRate = 150*deltat
            else:
                player2.boostTimer = 0
                player2.isBoosting = False
                p2ThrottleRate = player2.throttle*deltat
    while t < 1:
        
        midPoint.pos = setMidPoint(midPoint)
        rate(scene.rater)
        throttle(player1,p1ThrottleRate)
        yaw(player1,p1YawRate)
        roll(player1,p1RollRate)
        pitch(player1,p1PitchRate)
        
            #throttle(player1,p1ThrottleRate)
            #drift(player1,p1PitchRate,p1RollRate,p1YawRate)
            
        player1.pos = player1.pos + player1.velocity
        
        if player1.isShooting:
            x = int(200 * t)
            if x  == 1:
                laserInitialize(orangeLasers,player1,0)
            elif x == 25:
                laserInitialize(orangeLasers,player1,1)
            elif x == 50:
                laserInitialize(orangeLasers,player1,2)
            elif x == 75:
                laserInitialize(orangeLasers,player1,3)
            elif x == 100:
                laserInitialize(orangeLasers,player1,4)
            elif x == 125:
                laserInitialize(orangeLasers,player1,5)
            elif x == 150:
                laserInitialize(orangeLasers,player1,6)
            elif x == 175:
                laserInitialize(orangeLasers,player1,7)
        if player2.isShooting:
            x = int(200 * t)
            if x  == 1:
                laserInitialize(greenLasers,player2,0)
            elif x == 25:
                laserInitialize(greenLasers,player2,1)
            elif x == 50:
                laserInitialize(greenLasers,player2,2)
            elif x == 75:
                laserInitialize(greenLasers,player2,3)
            elif x == 100:
                laserInitialize(greenLasers,player2,4)
            elif x == 125:
                laserInitialize(greenLasers,player2,5)
            elif x == 150:
                laserInitialize(greenLasers,player2,6)
            elif x == 175:
                laserInitialize(greenLasers,player2,7)

        for i in orangeLasers:
            if i.visible == True:
                i.pos = i.pos + i.velocity
                i.lifetime = i.lifetime + 1
                
                if int((i.pos-player2.pos).mag) <= 2:
                    gameover = text(pos=midPoint.pos,height=50,text="orange Wins!",align='center')
                    writeToSaveFile()
                    endGame()
                if i.lifetime > 100:
                    i.lifetime = 0
                    i.visible = False
                    
        for i in greenLasers:
            if i.visible == True:
                i.pos = i.pos + i.velocity
                i.lifetime = i.lifetime + 1
                if int((i.pos-player1.pos).mag) <= 2:
                    gameover = text(pos=midPoint.pos,height=50,text="Green Wins!",align='center')
                    writeToSaveFile()
                    endGame()
                if i.lifetime > 100:
                    i.lifetime = 0
                    i.visible = False
        

        
        

        
        throttle(player2,p2ThrottleRate)
        roll(player2,p2RollRate)
        pitch(player2,p2PitchRate)
        yaw(player2,p2YawRate)
        player2.pos = player2.pos + player2.velocity

        t = t + deltat
    scene.stepper += 1
    moveStep(scene.stepper)

def replayGame():
    """
    player1.visible = False
    player2.visible = False
    p1Left.visible=False
    p1Right.visible=False
    p2Left.visible=False
    p2Right.visible=False
    """
    replayName = input("Enter Replay  File Name: ")
    replayName = "./Runs/"+replayName
    lines = []
    with open(replayName) as f:
        lines = f.readlines()

    count = 0
    for line in lines:
        if count != 0:
            name, val = line.split(":")
            if name == "Step":
                if count > 1:
                    scene.data.append(step)
                
                step = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
                stepIterator = 0
            else:
                stepIterator += 1
                col, var = name.split(".")
                if (stepIterator <= 4): #p1 vectors
                    val = val.split("<")
                    val = val[1].split(">")
                    x,y,z = val[0].split(",")
                    val = vector(float(x),float(y),float(z))
                    step[0][stepIterator-1] = val
                elif (stepIterator >= 11 and stepIterator <= 14): #p2 vectors
                    val = val.split("<")
                    val = val[1].split(">")
                    x,y,z = val[0].split(",")
                    val = vector(float(x),float(y),float(z))
                    step[1][stepIterator-11] = val
                    
                elif stepIterator == 9 or stepIterator == 10: #p1 Bools
                    val = val.split("\n")
                    if val[0] == " True":
                        print(val)
                        step[0][stepIterator-1]=True
                    else:
                        step[0][stepIterator-1]=False
                elif stepIterator == 19 or stepIterator == 20: #p2 Bools
                    val = val.split("\n")
                    if val[0] == " True":
                        step[1][stepIterator-11]=True
                    else:
                        step[1][stepIterator-11]=False
                elif stepIterator >= 5 and stepIterator <=8: #p1 Ints
                    step[0][stepIterator-1]=int(val)
                else: #p2 Ints
                    step[1][stepIterator-11]=int(val)

        else:
            name, val = line.split(":")
            scene.seednum = int(val)
            
        count += 1
    print(scene.data)
    def start(s):  
        moveStep(scene.stepper)
    startbutt = button(text="Start Replay",bind=start)
