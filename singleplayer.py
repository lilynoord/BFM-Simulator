from vpython import *
from players import *
from smallfunctions import *
from savefilereader import *
import datetime



scene.seednum = 0
midPoint = sphere(radius=0)

                 
midPoint.visible = False
    

scene.width=1500
scene.height= 600
scene.autoscale = False
scene.camera.follow(midPoint)
canvas.stepCounter = 0
def stepForward():
    #global midPoint
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
    newStep()
        

player1.pitch = 0
player1.roll = 0
player1.yaw = 0
player2.pitch = 0
player2.roll = 0
player2.yaw = 0
def newStep():
    scene.visible = True
    scene.caption = "\n Set Actions \n (Red Arrow: Left, negative | Green: Right, Positive\n"
    def focO(s):
        scene.camera.follow(player1)
    def focG(s):
        scene.camera.follow(player2)
    def focM(s):
        scene.camera.follow(midPoint)
    focOb = button(text = "Focus orange",bind=focO)
    focMb = button(text = "Focus midpoint",bind=focM)
    focGb = button(text = "Focus green",bind=focG)
    scene.append_to_caption('\n')
    stepForwardButton = button(color=color.black, bind=stepForward,
                               text="End Step", background=color.red)
    scene.append_to_caption(' \n')
    p1Tt = wtext(text="orange Throttle:")
    scene.append_to_caption(' \t\t\t\t\t\t\t\t\t\t\t\t')
    p1Pt = wtext(text="orange Pitch:")
    scene.append_to_caption(' \t\t\t\t\n')
    player1.isShooting = False
    player2.isShooting = False
    
    
    #orange Throttle Slider
    def p1T(s):
        p1Twt.text = '{:1.2f}'.format(s.value)
        player1.throttle = s.value
    
    
    p1Ts = slider(min=1,max=100,value=player1.throttle,length=500,step=1,
                  bind=p1T,right=15)
    p1Twt = wtext(text='{:1.2f}'.format(p1Ts.value))
    
    scene.append_to_caption('  ')

    #orange Pitch Slider
    
    def p1P(s):
        p1Pwt.text = '{:1.2f}'.format(s.value)
        player1.pitch = s.value
    
    
    p1Ps = slider(min=-90,max=90,value=player1.pitch,length=500,step=1,
                  bind=p1P,right=15)
    p1Pwt = wtext(text='{:1.2f}'.format(p1Ps.value))
    
    scene.append_to_caption('o\t')

    def orangeBoost(s):
        player1.isBoosting = s.checked
        if s:
            player1.isDrifting = False
            #odrift.checked = False
    oboost= checkbox(bind = orangeBoost, checked = player1.isBoosting,
                     text = "Boost")
    scene.append_to_caption('\n')

    
    p1Rt = wtext(text="orange Roll:")
    scene.append_to_caption(' \t\t\t\t\t\t\t\t\t\t\t\t\t')
    p1Yt = wtext(text="orange Yaw:")
    scene.append_to_caption(' \t\t\t\t\t\t\t\t\t\t\t\t\t')
    
    def orangeFire(s):
        player1.isShooting = s.checked
        
    orangeFireRadio = radio(bind=orangeFire,text="Fire")
    scene.append_to_caption("   ")
    def orangeMissile(s):
        player1.missileShot = s.checked
    orangeMissileRadio = radio(bind=orangeMissile,text="Fire Missile")
    scene.append_to_caption('\n')
    
    #orange Roll Slider
    
    def p1R(s):
        p1Rwt.text = '{:1.2f}'.format(s.value)
        player1.roll = s.value
    
    
    p1Rs = slider(min=-90,max=90,value=player1.roll,length=500,step=1,
                  bind=p1R,right=15)
    p1Rwt = wtext(text='{:1.2f}'.format(p1Rs.value))
    
    scene.append_to_caption('o')
    
    #orange Yaw Slider
    
    def p1Y(s):
        p1Ywt.text = '{:1.2f}'.format(s.value)
        player1.yaw = s.value
  
    
    p1Ys = slider(min=-90,max=90,value=player1.yaw,length=500,step=1,
                  bind=p1Y,right=15)
    p1Ywt = wtext(text='{:1.2f}'.format(p1Ys.value))
    
    scene.append_to_caption('o\t\t')
    def orangeDrift(s):
        if s and (player1.isBoosting or player1.isDrifting):
            player1.isBoosting = False
            player1.isDrifting = True
            oboost.checked = False
        else:
            player1.isDrifting = False
            s.checked = False
    #odrift= checkbox(bind = orangeDrift, checked = player1.isDrifting,text = "Drift")
    scene.append_to_caption('\n\n\n')

    p1Tt = wtext(text="Green Throttle:")
    scene.append_to_caption(' \t\t\t\t\t\t\t\t\t\t\t\t')
    p1Pt = wtext(text="Green Pitch:")
    scene.append_to_caption(' \t\n')

    #Green Throttle Slider
    
    def p2T(s):
        p2Twt.text = '{:1.2f}'.format(s.value)
        player2.throttle = s.value
    
    p2Ts = slider(min=1,max=100,value=player2.throttle,length=500,step=1,
                  bind=p2T,right=15)
    p2Twt = wtext(text='{:1.2f}'.format(p2Ts.value))
    
    scene.append_to_caption('   ')
    
    #Green Pitch Slider
    
    def p2P(s):
        p2Pwt.text = '{:1.2f}'.format(s.value)
        player2.pitch = s.value
    
    p2Ps = slider(min=-90,max=90,value=player2.pitch,length=500,step=1,
                  bind=p2P,right=15)
    p2Pwt = wtext(text='{:1.2f}'.format(p2Ps.value))
    
    scene.append_to_caption('o\t')

    def greenBoost(s):
        player2.isBoosting = s.checked
        if s:
            player2.isDrifting = False
            #gdrift.checked = False
    gboost= checkbox(bind = greenBoost, checked = player2.isBoosting,
                     text = "Boost")
    scene.append_to_caption('\n')

    p1Rt = wtext(text="Green Roll:")
    scene.append_to_caption(' \t\t\t\t\t\t\t\t\t\t\t\t')
    p1Yt = wtext(text="Green Yaw:")
    scene.append_to_caption(' \t\t\t\t\t\t\t\t\t\t\t\t\t')
    
    def greenFire(s):
        player2.isShooting = s.checked
        
    greenFireRadio = radio(bind=greenFire,text="Fire")
    scene.append_to_caption("   ")
    def greenMissile(s):
        player2.missileShot = s.checked
    greenMissileRadio = radio(bind=greenMissile,text="Fire Missile")
    scene.append_to_caption('\n')
    
    #Green Roll Slider
    
    def p2R(s):
        p2Rwt.text = '{:1.2f}'.format(s.value)
        player2.roll = s.value
    
    p2Rs = slider(min=-90,max=90,value=player2.roll,length=500,step=1,
                  bind=p2R,right=15)
    p2Rwt = wtext(text='{:1.2f}'.format(p2Rs.value))
    
    scene.append_to_caption('o')
    
    #Green Yaw Slider
    
    def p2Y(s):
        p2Ywt.text = '{:1.2f}'.format(s.value)
        player2.yaw = s.value
    
    p2Ys = slider(min=-90,max=90,value=player2.yaw,length=500,step=1,
                  bind=p2Y,right=15)
    p2Ywt = wtext(text='{:1.2f}'.format(p2Ys.value))
    
    scene.append_to_caption('o\t\t')
    def greenDrift(s):
        if s and player2.isBoosting:
            player2.isBoosting = False
            player2.isDrifting = True
            gboost.checked = False
        else:
            player2.isDrifting = False
            s.checked = False
    #gdrift= checkbox(bind = greenDrift, checked = player2.isDrifting,text = "Drift")
    scene.append_to_caption('\n\n\n')
