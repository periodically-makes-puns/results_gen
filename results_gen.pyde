PRIZCOND = 0.1 # percentage who prize
SUB1PERC = 0.5 # percentage who lose one life
SUB3PERC = 0.2 # percentage who lose 3 lives
SUB3COND = 30 # lower than this loses extra 3
l = 0
p = 1
maxResps = 5
RESPH = 101
mini = 0
maxi = 0
fin = open("./input.tsv", "r").read()

def displayHeart(imge, x, y, i, mini):
    image(imge, 910 + 30 * x + 8 - 4 * y, 5 + (i-mini+1) * RESPH + 30 * y + 1 - RESPH) 

def contestant(i, mini):
    contestant = inp[i]
    nr = float((len(filter(lambda a: a[0] != "-", inp)) - float(contestant[0]) - 1)) / float((len(filter(lambda a: a[0] != "-", inp)) - 2))
    nl = float(contestant[3]) # original lives
    pl = 0
    sl = int(contestant[4]) # spell loss
    al = 0
    boost = float(contestant[7][:-2])
    u = f
    RANKX = 0
    RANKY = 0
    RANKF = 84
    NAMEX = 0
    NAMEY = 0
    NAMEF = 48
    RESPX = 0
    RESPY = 0
    RESPF = 20
    SHIFTX = 0
    SHIFTY = 0
    SCOREX = 0
    SCOREY = 0
    SCOREF = 36
    STDEVX = 0
    STDEVY = 0
    STDEVF = 36
    BOOSTX = 0
    BOOSTY = 0
    BOOSTF = 16
    if float(contestant[5][:-2]) + boost < SUB3COND:
        al = 2
        fill(160, 20, 20)
        rect(0, (i-mini+1) * RESPH - RESPH, 1200, RESPH)
        #fill(160, 90, 90)
    if nr > 1 - PRIZCOND:
        u = prize
        pl = 1
        fill(224, 207, 76)
        image(PBG, 0, (i-mini+1) * RESPH - RESPH)
        RANKX = 0
        RANKY = -3
        RANKF = 84
        NAMEX = 0
        NAMEY = 0
        NAMEF = 48
        RESPX = 0
        RESPY = 0
        RESPF = 20
        SHIFTX = 13
        SHIFTY = 0
        SCOREX = 13
        SCOREY = 10
        SCOREF = 24
        STDEVX = 17
        STDEVY = 0
        STDEVF = 24
        BOOSTX = 40
        BOOSTY = 13
        BOOSTF = 16
    elif nr < SUB3PERC:
        al += 3
        fill(209, 85, 85)
        rect(0, (i-mini+1) * RESPH - RESPH, 1200, RESPH)
        #fill(209, 147, 147)
        fill(255)
        RANKX = -2
        RANKY = -6
        RANKF = 84
        NAMEX = 0
        NAMEY = 2
        NAMEF = 48
        RESPX = 0
        RESPY = 0
        RESPF = 20
        SHIFTY = 0
        SHIFTX = 13
        SHIFTY = 0
        SCOREF = 24
        STDEVX = 20
        STDEVY = -2
        STDEVF = 24
        BOOSTX = 40
        BOOSTY = 10
        BOOSTF = 16
    elif nr < SUB1PERC:
        al += 1
        fill(242, 138, 138)
        rect(0, (i-mini+1) * RESPH - RESPH, 1200, RESPH)
        #fill(242, 190, 190)
        fill(255)
        RANKX = -2
        RANKY = -6
        RANKF = 84
        NAMEX = 0
        NAMEY = 2
        NAMEF = 48
        RESPX = 0
        RESPY = 0
        RESPF = 20
        SHIFTY = 0
        SHIFTX = 13
        SHIFTY = 0
        SCOREF = 24
        STDEVX = 20
        STDEVY = -2
        STDEVF = 24
        BOOSTX = 40
        BOOSTY = 10
        BOOSTF = 16
    else:
        al += 0
        fill(200, 200, 200)
        image(SBG, 0, (i-mini+1) * RESPH - RESPH)
        #fill(230, 230, 230)
        fill(255)
        RANKX = -2
        RANKY = -6
        RANKF = 84
        NAMEX = 0
        NAMEY = 2
        NAMEF = 48
        RESPX = 0
        RESPY = 0
        RESPF = 20
        SHIFTY = 0
        SHIFTX = 13
        SHIFTY = 0
        SCOREF = 24
        STDEVX = 20
        STDEVY = -2
        STDEVF = 24
        BOOSTX = 40
        BOOSTY = 11
        BOOSTF = 16
    if nl - sl - al + pl <= 0:
        fill(45, 45, 45)
        rect(0, (i-mini+1) * RESPH - RESPH, 1200, RESPH)
        #fill(90, 90, 90)
        fill(255)
        u = dead
        RANKX = -2
        RANKY = 10
        RANKF = 84
        NAMEX = 0
        NAMEY = 12
        NAMEF = 48
        RESPX = 0
        RESPY = 0
        RESPF = 20
        SHIFTX = 8
        SHIFTY = 10
        SCOREF = 24
        STDEVX = 22
        STDEVY = 3
        STDEVF = 24
        BOOSTX = 36
        BOOSTY = 20
        BOOSTF = 16
    nl -= sl + al - pl
    al += nl
    sl += al
    pl += sl
    
    textAlign(CENTER, CENTER)
    textFont(u, RANKF)
    text(contestant[0], 60+RANKX, (i-mini+1) * RESPH + 50 + RANKY - RESPH - 10)
    textAlign(LEFT, CENTER)
    textFont(u, NAMEF)
    offset = 0
    
    if textWidth(contestant[1]) > 650:
        textFont(u, NAMEF * 2 / 3)
        offset = 6
    text(contestant[1], 110 + NAMEX, (i-mini+1) * RESPH + 30 + NAMEY + offset - RESPH - 10)
    k = textWidth(contestant[1])
    textFont(u, RESPF)
    if textWidth(contestant[2]) > 700:
        textFont(u, RESPF * 4 / 5)
    fill(0)
    text(contestant[2], 120 + RESPX, (i-mini+1) * RESPH + 80 + RESPY - RESPH - 10)         
    '''   
    if nl == 1:
        scale(1.5)
        image(PERIL, (110 + k) * 2/3, ((i-mini+1) * RESPH + 25 - RESPH - 10) * 2/3)
        scale(0.666666666666666666666666666666)
    elif 1 < nl < 4:
        scale(1.5)
        image(DANGER, (110 + k) * 2/3, ((i-mini+1) * RESPH + 25 - RESPH - 10) * 2/3)
        scale(0.666666666666666666666666666666)
    '''
    fill(255)
    ad = 0
    for y in range(3):
        for x in range(3):
            pos = y * 3 + x + 1
            if pos <= nl:
                displayHeart(NOLOSSNOGAIN, x, y, i, mini)
            elif pos <= al:
                if pl > sl:
                    pl -= 1
                    ad += 1
                    displayHeart(NOLOSSNOGAIN, x, y, i, mini)
                else:
                    displayHeart(FULLLOSS, x, y, i, mini)
            elif pos <= sl:
                if pl > sl and pl - sl > sl - pos:
                    pl -= 1
                    ad += 1
                    displayHeart(GSPELLLOSS, x, y, i, mini)
                else:
                    displayHeart(SPELLLOSS, x, y, i, mini)
            elif pos <= pl:
                displayHeart(GAINFULL, x, y, i, mini)
            else:
                displayHeart(PREVFULLLOSS, x, y, i, mini)    
    if nl - sl - al + pl <= 0:
        fill(255)
    if nr >= SUB1PERC and nr < (1-PRIZCOND):
        u = f1
    textFont(u, SCOREF)
    if boost:
        text(contestant[5], 1025 + SHIFTX, (i-mini+1) * RESPH + 20 - RESPH + SHIFTY)
    else:
        textAlign(CENTER, CENTER)
        text(contestant[5], 1080 + SHIFTX, (i-mini+1) * RESPH + 20 - RESPH + SHIFTY)
        textAlign(LEFT, CENTER)
    q = textWidth(contestant[5])
    textFont(u, STDEVF)
    textAlign(CENTER, CENTER)
    text(contestant[6], 1080 + STDEVX, (i-mini+1) * RESPH + 70 + STDEVY - RESPH)
    textFont(u, BOOSTF)
    if boost:
        text("{:+.2f}%".format(boost), 1025 + q + BOOSTX, (i-mini+1) * RESPH + 10 + BOOSTY - RESPH)
    xoff = 0
    yoff = 0
    if contestant[8]:
        img = contestant[8]
        if img.height > img.width:
            img.resize(0, RESPH - 9)
            xoff = (RESPH - 4 - img.width) / 2
            yoff = 0
        else:
            img.resize(RESPH - 9, 0)
            xoff = 0
            yoff = (RESPH - 4 - img.height) / 2
        image(img, 810 + xoff + 6, 2 + RESPH * (i-mini+1) - RESPH + yoff) 
    if nl == 1:
        scale(1.5)
        image(PERIL, (810 + xoff - 55) * 2/3, (4 + RESPH * (i-mini+1) - RESPH) * 2/3)
        scale(0.666666666666666666666666666666)
    elif 1 < nl < 4:
        scale(1.5)
        image(DANGER, (810 + xoff - 60) * 2/3, (4 + RESPH * (i-mini+1) - RESPH) * 2/3)
        scale(0.666666666666666666666666666666)



def dummy(i, mini):
    fill(60, 60, 60)
    rect(0, (i-mini+1) * RESPH - RESPH, 1200, RESPH)
    fill(255, 255, 255)
    contestant = inp[i]
    textAlign(CENTER, CENTER)
    textFont(f, 84)
    text(contestant[0], 60, (i-mini+1) * RESPH + 50 - RESPH - 10)
    textAlign(LEFT, CENTER)
    textFont(f, 48)
    text(contestant[1], 110, (i-mini+1) * RESPH + 35 - RESPH - 10)
    k = textWidth(contestant[1])
    textFont(f, 16)
    text(contestant[2], 110, (i-mini+1) * RESPH + 80 - RESPH - 10)
    textFont(f, 36)
    text(contestant[5], 1010, (i-mini+1) * RESPH + 20 - RESPH)
    q = textWidth(contestant[5])
    textFont(f1)
    text("STDEV", 1010, (i-mini+1) * RESPH + 78 - RESPH)
    w = textWidth("STDEV")
    text("SCORE", 1010 + q, (i-mini+1) * RESPH + 28 - RESPH)
    textFont(f, 36)
    text(contestant[6], 1010 + w + 8, (i-mini+1) * RESPH + 70 - RESPH)
    if contestant[8]:
        img = contestant[8]
        if img.height > img.width:
            img.resize(0, 96)
            xoff = (96 - img.width) / 2
            yoff = 0
        else:
            img.resize(96, 0)
            xoff = 0
            yoff = (RESPH - 4 - img.width) / 2
        image(img, 810 + xoff + 4, 4 + RESPH * (i-mini+1) - RESPH + yoff) 
    if nl == 1:
        scale(1.5)
        image(PERIL, (810 + xoff - 69) * 2/3, (4 + RESPH * (i-mini+1) - RESPH) * 2/3)
        scale(0.666666666666666666666666666666)
    elif 1 < nl < 4:
        scale(1.5)
        image(DANGER, (810 + xoff - 70) * 2/3, (4 + RESPH * (i-mini+1) - RESPH) * 2/3)
        scale(0.666666666666666666666666666666)



def sortFunc(a):
    AVG = float(a[5][:-2]) + float(a[7][:-2])
    STV = float(a[6][:-2])
    return (AVG, STV)



def setup():
    global inp
    global f
    global dead
    global prize
    global f1
    global NOLOSSNOGAIN
    global GAINFULL
    global HALFLOSS
    global FULLLOSS
    global SPELLLOSS
    global GSPELLLOSS
    global PREVHALFLOSS
    global PREVFULLLOSS
    global PERIL
    global DANGER
    global numResps
    global PBG
    global SBG
    size(1200, maxResps * RESPH)
    frameRate(12)
    background(255,255,255,255)
    NOLOSSNOGAIN = loadImage("Full.png") # unchanged full
    GAINFULL     = loadImage("Gain.png") # +1 to fill
    HALFLOSS     = loadImage("Half-Loss.png") # -0.5
    FULLLOSS     = loadImage("Loss.png") # -1 also -0.5 if only 0.5 left
    SPELLLOSS    = loadImage("SpellLoss.png")
    GSPELLLOSS   = loadImage("GainSpellLoss.png")
    PREVHALFLOSS = loadImage("PrevHalf-Loss.png") # unchanged 0.5
    PREVFULLLOSS = loadImage("PrevLoss.png") # unchanged 0
    PERIL        = loadImage("peril.png")
    DANGER       = loadImage("danger.png")
    PLACEHOLDER  = loadImage("Placeholder.png")
    PBG          = loadImage("PBG.png")
    SBG          = loadImage("SBG.png")
    PBG.resize(1200, 0)
    inp = [a.split("\t") for a in fin.split("\n")]
    del inp[0]
    print(PFont.list())
    inp.sort(key=sortFunc, reverse=True)
    counter = 1
    for i in range(len(inp)):
        cont = inp[i]
        if cont[3] != 0:
            cont[0] = str(counter)
            counter += 1
        else:
            cont[0] = "-"
        while (len(cont) <= 8):
            cont.append(0)
        new = ""
        throw = False
        arg = "",
        for ch in cont[1][::-1]:
            if ch == "]":
                throw = True
            elif ch == "[":
                throw = False
            elif not throw:
                new += ch
        k = loadImage("Books/{:}.png".format(new[::-1].strip()))
        if k:
            cont[8] = k
        else:
            cont[8] = PLACEHOLDER
    prize = createFont("DS_Mysticora", 16, True)
    f = createFont("Alegreya Regular", 16, True)
    dead = createFont("Special Elite", 16, True)
    f1 = createFont("Alegreya Bold", 16, True)
    fbc = createFont("Segoe UI Symbol", 16, True)

def draw():
    global l
    global inp
    global f
    global f1
    global NOLOSSNOGAIN
    global GAINFULL
    global HALFLOSS
    global FULLLOSS
    global PREVHALFLOSS
    global PREVFULLLOSS
    global PERIL
    global maxResps
    background(255, 255, 255)
    for i in range(mini, maxi):
        if inp[i][0] == "-":
            dummy(i, mini)
        else:
            contestant(i, mini)
    

def keyTyped():
    global l
    global p
    global mini
    global maxi
    global maxResps
    if key == "s" or key == DOWN:
        if l < len(inp):
            l += 1
            print(l)
    if key == "e":
        img = get(0, 0, 1200, RESPH * (maxi - mini))
        img.save("{:d}.png".format(p))
        p += 1
    if key == "w" or key == UP:
        if l > 0:
            l -= 1
            print(l)
    if key == ENTER:
        if maxResps == len(inp):
            l = len(inp)
    if key == "d":
        l = min(l + maxResps, len(inp))
        print(l)
        if l == len(inp):
            maxResps = l - maxi
            this.surface.setSize(1200, maxResps * 101)
    if key == "a":
        l = max(l - maxResps, 0)
        print(l)
    if "1" <= key and "9" >= key:
        l = min(l - maxResps + int(key), len(inp))
            
        maxResps = int(key)
        this.surface.setSize(1200, maxResps * 101)
    mini = max(l - maxResps + 0, 0)
    maxi = l 
