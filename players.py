from vpython import *


player1Body = pyramid(pos=vector(0,0,0),size=vector(12,10,4),
                  color=color.orange, )
player1Cockpit = ellipsoid(pos=vector(4,0,2), length=7,height=2,width=2,
                           color=color.black)
trailLength = 3000
player1 = compound([player1Body,player1Cockpit],make_trail=True,
                   retain=trailLength,trail_color=color.orange)
player2Body = pyramid(pos=vector(100,50,0),size=vector(12,10,4),
                  color=color.green,make_trail=True)
player2Cockpit = ellipsoid(pos=vector(104,50,2), length=7,height=2,width=2,
                           color=color.black)
player2 = compound([player2Body,player2Cockpit],make_trail=True,
                   retain=trailLength,trail_color=color.green)


player1.velocity = vector(75,0,0)
player2.velocity = vector(75,0,0)
player1.throttle = 75
player2.throttle = 75
player1.yawdir = rotate(player1.axis,angle=radians(90),axis=player1.up)
player2.yawdir = rotate(player2.axis,angle=radians(90),axis=player2.up)
player1.isShooting = False
player2.isShooting = False
player1.missileShot = False
player2.missileShot = False
player1.isDrifting = False
player2.isDrifting = False
player1.isBoosting = False
player2.isBoosting = False
player1.driftTimer = 0
player1.boostTimer = 0
player2.driftTimer = 0
player2.boostTimer = 0
p1Left = attach_arrow(player1,"up",shaftwidth=0.8,scale=6.5,color=color.red)
p1Right = attach_arrow(player1,"up",shaftwidth=0.8,scale=-6.5,color=color.green)

p2Left = attach_arrow(player2,"up",shaftwidth=0.8,scale=6.5,color=color.red)
p2Right = attach_arrow(player2,"up",shaftwidth=0.8,scale=-6.5,color=color.green)


orangeLaser1 = ellipsoid(pos=vector(0,20,0),length=2,height=1,width=1,
                       color=color.orange,
                       shininess=0,visible=False)
orangeLaser1.velocity = vector(0,0,0)
orangeLaser2 = orangeLaser1.clone()
orangeLaser3 = orangeLaser1.clone()
orangeLaser4 = orangeLaser1.clone()
orangeLaser5 = orangeLaser1.clone()
orangeLaser6 = orangeLaser1.clone()
orangeLaser7 = orangeLaser1.clone()
orangeLaser8 = orangeLaser1.clone()

orangeLasers = [orangeLaser1,orangeLaser2,orangeLaser3,orangeLaser4,
              orangeLaser5,orangeLaser6,orangeLaser7,orangeLaser8]
for i in orangeLasers:
    i.visible=False
    i.velocity=vector(0,0,0)
    i.lifetime = 0

greenLaser1 = ellipsoid(pos=vector(0,20,0),length=2,height=1,width=1,
                       color=color.green, 
                       shininess=0,visible=False)
greenLaser1.velocity = vector(0,0,0)
greenLaser2 = greenLaser1.clone()
greenLaser3 = greenLaser1.clone()
greenLaser4 = greenLaser1.clone()
greenLaser5 = greenLaser1.clone()
greenLaser6 = greenLaser1.clone()
greenLaser7 = greenLaser1.clone()
greenLaser8 = greenLaser1.clone()

greenLasers = [greenLaser1,greenLaser2,greenLaser3,greenLaser4,
               greenLaser5,greenLaser6,greenLaser7,greenLaser8]

orangeMissile = cone(pos=vector(0,0,0),axis=player1.axis,
                     radius=2,color=color.orange,make_trail=True)
orangeMissile.visible=False
orangeMissile.lifetime = 1000
orangeMissile.velocity = vector(0,0,0)
greenMissile = cone(pos=vector(0,0,0),axis=player1.axis,
                     radius=2,color=color.green,make_trail=True)
greenMissile.visible=False
greenMissile.lifetime = 1000
greenMissile.velocity = vector(0,0,0)
for i in greenLasers:
    
    i.visible=False
    i.velocity=vector(0,0,0)
    i.lifetime = 0




