from vpython import *
from players import *
from smallfunctions import *
from savefilereader import *
from singleplayer import *
import datetime
import asyncio
import discord
from multiplayer import *
import random
    
##DELTE BEFORE SHIP
yaw(player1,-45)
##----


    
midPoint = sphere(radius=0)
                 
scene.seednum = 0
    
deltat = 0.005
t = 0

#scene.width=800
#scene.height= 800
scene.autoscale = False
scene.camera.follow(midPoint)

scene.visible = False
scene.stepCounter = 0


def onlinePass(s):
    loop = asyncio.get_event_loop()
    online()
    


#pitch(player2,180)
#yaw(player2,180)
#newStep()
client = discord.Client()

def main():
    scene.select()
    scene.visible=False
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
    startOffline = button(text = "Start Offline Game",bind=newStep)
    scene.append_to_caption()
    startReplay = button(text = "Replay Past Game",bind=replayGame)
    def butt(s):
        print(p1ActionList)
        print(p2ActionList)
        print(p1Ready[0])
        print(p2Ready[0])
    bu = button(text = "Bot Test",bind=butt)
    def online():
        pnum = input("type your player number: ")        
        @client.event

        async def on_ready():
            print('We have logged in as {0.user}'.format(client))
            logChannel = client.get_channel(928013475345731594)
            await logChannel.send('Hello. Player ' + pnum + " is online. Type `/bfm help` for help")
            if pnum == "1":
                await logChannel.send('p1 online')
                await logChannel.send('p1 ready')
                p1ReadyUp()
            elif pnum == "2":
                await logChannel.send('p2 online')
                await logChannel.send('p2 ready')
                p2ReadyUp()


        @client.event
        

        async def on_message(message):
            if message.author == client.user:
                return

            if message.content.startswith('/bfm help'):
                await message.channel.send('type `/p1 ready` or `/p2 ready` to ready up player 1 or player 2 respectively\n type `/ready status` to check the status of each player')
                await message.channel.send('to perform an action for, format your message exactly like this:')
                await message.channel.send('/p# action\nthrottle:0-100\npitch:-90-90\nyaw:-90-90\nroll:-90-90\nshoot:y/n\nboost:y/n\nmissile:y/n')
                await message.channel.send('you can copy your last instructions and only change the ones you want to \n if you don\'t recieve a confirmation message after sending you actions, please check the formatting')
                await message.channel.send('If you wish to set different positions for the players, type ```/set positions\np1x:#\np1y:#\np1z:#\np1yaw:#\np2x:#\np2y:#\np2z:#\np2yaw:#```')
            if message.content.startswith("/p1 action") and p1Ready[0] and p2Ready[0]:     
                if parseP1Actions(message.content):
                    await message.add_reaction('\U0001F44D')
                    pOn(1)
                    onlineNewStep()
                else:
                    await message.channel.send('player 1\'s actions were formatted incorrectly. Please try again.')
            elif message.content.startswith("/p2 action") and p2Ready[0] and p1Ready[0]:
                if parseP2Actions(message.content):
                    await message.add_reaction('\U0001F44D')
                    pOn(2)
                    onlineNewStep()
                else:
                    await message.channel.send('player 2\'s actions were formatted incorrectly. Please try again.')
            elif message.content.startswith('p1 ready'):
                p1ReadyUp()
                await message.channel.send('player 1 ready status set to ' + str(p1Ready[0]))
            elif message.content.startswith('p2 ready'):
                p2ReadyUp()
                await message.channel.send('player 2 ready status set to ' + str(p2Ready[0]))
            elif message.content.startswith('/ready status'):
                await message.channel.send("Player 1 Ready: " + str(p1Ready[0]) + "\nPlayer 2 Ready: " + str(p2Ready[0]))
            elif message.content.startswith('p2 online'):
                
                p1ReadyUp()
                await message.channel.send('player 1 ready status set to ' + str(p1Ready[0]))
                await message.channel.send('p1 ready')
                scene.seednum = random.randrange(0,100)
                await message.channel.send('seednum:'+str(scene.seednum))
            elif message.content.startswith('p1 online'):
                p2ReadyUp()
                await message.channel.send('player 2 ready status set to ' + str(p2Ready[0]))
                await message.channel.send('p2 ready')
                scene.seednum = random.randrange(0,100)
                await message.channel.send('seednum:'+str(scene.seednum))
            elif message.content.startswith('seednum:'):
                a,b = message.content.split(':')
                scene.seednum = int(b)
                await message.channel.send('seednum `'+str(scene.seednum)+'` recieved')
            elif message.content.startswith('/set positions'):
                if setPos(message.content):
                    await message.channel.send("Successfully set positions")
                
        if pnum == "1":
            client.run('ODkxOTIyMTgzMjMwNzQyNTQ4.YVFZQw.B32PFzcAxi-4XZEPvgqW0wSUD9M')
            
        elif pnum == "2":
            client.run('NjgzNDI5Njg3ODkxOTg0NDIx.Xlrbfw.9U5dzGt57MJP7wejVYxQh9KfwBg')
            

            
        else:
            print("That was not a valid player number. Please restart the program and try again")

    onlineButton = button(text = "Play an online Game",bind=online)


    
    
main()
