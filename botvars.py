p1ActionList =[100,0,0,0,0,0,0]
p2ActionList =[100,0,0,0,0,0,0]
p1Ready = [False]
p2Ready = [False]
p1Actions = [False]
p2Actions = [False]
def parseP1Actions(message):
    print(message)
    linesplit = message.split('\n')
    i = 0
    for l in linesplit:
        if i != 0:
            a,b = l.split(':')
            if i < 5 and i != 1:
                c = int(b)
                if c < -90:
                    c = -90
                elif c > 90:
                    c = 90
                p1ActionList[i-1] = c
            elif i >= 5:
                if b == "y":
                    p1ActionList[i-1] = True
                else:
                    p1ActionList[i-1] = False
            elif i == 1:
                c = int(b)
                if c < 0:
                    c = 1
                elif c > 100:
                    c = 100
                p1ActionList[i-1] = c

        i+= 1
    return True
def parseP2Actions(message):
    linesplit = message.split('\n')
    i = 0
    for l in linesplit:
        if i != 0:
            a,b = l.split(':')
            if i < 5 and i != 1:
                c = int(b)
                if c < -90:
                    c = -90
                elif c > 90:
                    c = 90
                p2ActionList[i-1] = c
            elif i >= 5:
                if b == "y":
                    p2ActionList[i-1] = True
                else:
                    p2ActionList[i-1] = False
            elif i == 1:
                c = int(b)
                if c < 0:
                    c = 1
                elif c > 100:
                    c = 100
                p2ActionList[i-1] = c

        i+= 1
    return True

def p1ReadyUp():
    p1Ready[0] = True
    #return p1Ready
def p2ReadyUp():
    p2Ready[0] = True
    #return p2Ready
    
def pOn(p):
    if p == 1:
        p1Actions[0] = True
    elif p == 2:
        p2Actions[0] = True

def pOff(p):
    if p == 1:
        p1Actions[0] = False
        
    elif p == 2:
        p2Actions[0] = False
