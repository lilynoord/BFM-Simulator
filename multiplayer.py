from vpython import *
from players import *
from smallfunctions import *
from savefilereader import *
import datetime
from botvars import *
import asyncio

midPoint = sphere(radius=0)
                 
scene.waitStatus = "waiting"


scene.width=800
scene.height= 800
scene.autoscale = False
scene.camera.follow(midPoint)

scene.visible = False
scene.stepCounter = 0



    
def onlineStepForward():

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
        if player1.missileShot:
            if orangeMissile.lifetime > 0:  
                if orangeMissile.visible == False:
                    orangeMissile.make_trail = True
                    orangeMissile.lifetime = 1100
                    orangeMissile.retain = 100
                    orangeMissile.pos = player1.pos
                    orangeMissile.axis = player1.axis
                    orangeMissile.velocity = vector(1,0,0)
                    orangeMissile.velocity.hat = player1.velocity
                    print(orangeMissile.velocity.mag)
                    orangeMissile.visible = True
                else:
                    rad = 25
                    if (orangeMissile.pos-player2.pos).mag > 10:
                        rad = 2
                    elif (orangeMissile.pos-player2.pos).mag > 5:
                        rad = 5
                    else:
                        rad = 25
                    v2 = vector(orangeMissile.velocity)
                    v2.hat = player2.pos - orangeMissile.pos
                    #v2 = v2 / deltat
                    dif = v2 / rad
                    #print(v2,dif)
                    orangeMissile.pos = orangeMissile.pos + orangeMissile.velocity
                    orangeMissile.lifetime -= 1
                    orangeMissile.axis.hat = orangeMissile.axis + dif
                    #orangeMissile.axis.hat = v2
                    orangeMissile.velocity.hat = orangeMissile.axis
                    print(int((orangeMissile.pos-player2.pos).mag))
                    if int((orangeMissile.pos-player2.pos).mag) <= 8:
                        gameover = text(pos=midPoint.pos,height=50,text="orange Wins!",align='center')
                        writeToSaveFile()
                        writeToSaveFile()
                        endGame()
            else:
                player1.missileShot = False
                orangeMissile.visible = False
                orangeMissile.make_trail = False
                orangeMissile.lifetime = 400

            if player2.missileShot:
                if greenMissile.lifetime > 0:
                    if greenMissile.visible == False:
                        greenMissile.make_trail = True
                        greenMissile.lifetime = 1100
                        greenMissile.retain = 100

                        greenMissile.pos = player2.pos
                        greenMissile.axis = player2.axis
                        greenMissile.velocity = vector(1,0,0)
                        greenMissile.velocity.hat = player2.velocity
                        print(greenMissile.velocity.mag)
                        greenMissile.visible = True
                    else:
                        rad = 25
                        if (greenMissile.pos-player1.pos).mag > 10:
                            rad = 2
                        elif (greenMissile.pos-player1.pos).mag > 5:
                            rad = 5
                        else:
                            rad = 25
                        v2 = vector(greenMissile.velocity)
                        v2.hat = player1.pos - greenMissile.pos
                        #v2 = v2 / deltat
                        dif = v2 / rad
                        #print(v2,dif)

                        greenMissile.pos = greenMissile.pos + greenMissile.velocity
                        greenMissile.lifetime -= 1
                        greenMissile.axis.hat = greenMissile.axis + dif
                        #greenMissile.axis.hat = v2
                        greenMissile.velocity.hat = greenMissile.axis
                        print(int((greenMissile.pos-player1.pos).mag))
                        if int((greenMissile.pos-player1.pos).mag) <= 8:
                            gameover = text(pos=midPoint.pos,height=50,text="green Wins!",align='center')
                            writeToSaveFile()
                            writeToSaveFile()
                            endGame()
            else:
                player2.missileShot = False
                greenMissile.visible = False
                greenMissile.make_trail = False
                greenMissile.lifetime = 400
        midPoint.pos = setMidPoint(midPoint)

        rate(100)
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
        
    writeToSaveFile()
    scene.seednum += 1
    scene.waitStatus = "waiting"



def onlineNewStep():
    scene.visible=True
    print(' /n1:')
    print(p1Actions[0])
    print(p2Actions[0])
    print(scene.waitStatus)
    if scene.waitStatus == "waiting":
        if p1Actions[0] and p2Actions[0]:
            p1Actions[0] = False
            p2Actions[0] = False
            print(' /n2:')
            print(p1Actions[0])
            print(p2Actions[0])
            print(scene.waitStatus)
            player1.throttle = p1ActionList[0]
            player1.pitch = p1ActionList[1]
            player1.yaw = p1ActionList[2]
            player1.roll = p1ActionList[3]
            player1.isShooting = p1ActionList[4]
            player1.isBoosting = p1ActionList[5]
            player1.missileShot = p1ActionList[6]
            player2.throttle = p2ActionList[0]
            player2.pitch = p2ActionList[1]
            player2.yaw = p2ActionList[2]
            player2.roll = p2ActionList[3]
            player2.isShooting = p2ActionList[4]
            player2.isBoosting = p2ActionList[5]
            player2.missileShot = p2ActionList[6]
            waitStatus = "playing"
            onlineStepForward()
            print(' /n3:')
            print(p1Actions[0])
            print(p2Actions[0])
            print(scene.waitStatus)
            







def tester():
    p1Actions[0] = True
    p2Actions[0] = True
    p1ActionList[0] = 75
    p2ActionList[0] = 75
    onlineNewStep()

    














    
#pitch(player2,180)
#yaw(player2,180)
#newStep()
"""
def online():
    pnum = input("type your player number")
    
    if pnum == "1":
        
        @client.event
        async def on_ready():
            print('We have logged in as {0.user}'.format(client))
            


        @client.event
        async def on_message(message):
            if message.author == client.user:
                return

            if message.content.startswith('/bfmhelp'):
                await message.channel.send('type `/p1 ready` to ready up player 1 \n type `/ready status` to check the status of each player')
                await message.channel.send('to perform an action for player 1, format your message exactly like this:')
                await message.channel.send('/p1 action\nthrottle:0-100\npitch:-90-90\nyaw:-90-90\nroll:-90-90\nshoot:y/n\nboost:y/n')
                await message.channel.send('you can copy your last instructions and only change the ones you want to \n if you don\'t recieve a confirmation message after sending you actions, please check the formatting')
            
            if message.content.startswith("/p1 action") and p1Ready[0] and p2Ready[0]:     
            
                if parseP1Actions(message.content):
                    await message.channel.send('player 1\'s actions succesfully recieved')
                else:
                    await message.channel.send('player 1\'s actions were formatted incorrectly. Please try again.')
            elif message.content.startswith("/p2 action") and p2Ready[0] and p1Ready[0]:
                await message.channel.send('player 2\'s actions recieved')
                parseP2Actions(message.content)
            elif message.content.startswith('/p1 ready'):
                p1ReadyUp()
                await message.channel.send('player 1 ready status set to ' + str(p1Ready[0]))
            elif message.content.startswith('/p2 ready'):
                p2ReadyUp()
                await message.channel.send('player 2 ready status set to ' + str(p2Ready[0]))
            elif message.content.startswith('/ready status'):
                await message.channel.send("Player 1 Ready: " + str(p1Ready[0]) + "\nPlayer 2 Ready: " + str(p2Ready[0]))
                

        client.run('ODkxOTIyMTgzMjMwNzQyNTQ4.YVFZQw.B32PFzcAxi-4XZEPvgqW0wSUD9M')
    elif pnum == "2":
        print("P2")
    else:
        print("That was not a valid player number. Please restart the program and try again")
"""
