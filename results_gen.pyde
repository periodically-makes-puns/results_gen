PRIZCOND = 0.1 # percentage who prize
SUB1PERC = 0.5 # percentage who lose one life
SUB3PERC = 0.2 # percentage who lose 3 lives
SUB3COND = 30 # lower than this loses extra 3
l = 0
p = 1
maxResps = 4
RESPH = 101

fin = open("./input.tsv", "r").read()

def displayHeart(imge, x, y, i, mini):
    image(imge, 910 + 30 * x + 8 - 4 * y, 5 + (i-mini+1) * 100 + 30 * y - 100) 

def contestant(i, mini):
    contestant = inp[i]
    nr = float((len(filter(lambda a: a[0] != "-", inp)) - float(contestant[0]) - 1)) / float((len(filter(lambda a: a[0] != "-", inp)) - 2))
    nl = float(contestant[3]) # original lives
    pl = 0
    sl = int(contestant[4]) # spell loss
    al = 0
    boost = float(contestant[7][:-2])
    if float(contestant[5][:-2]) + boost < SUB3COND:
        al = 2
        fill(160, 20, 20)
        rect(0, (i-mini+1) * RESPH - RESPH, 1200, RESPH)
        #fill(160, 90, 90)
    if nr > 1 - PRIZCOND:
        pl = 1
        fill(224, 207, 76)
        image(PBG, 0, (i-mini+1) * RESPH - RESPH)
    elif nr < SUB3PERC:
        al += 3
        fill(209, 85, 85)
        rect(0, (i-mini+1) * RESPH - RESPH, 1200, RESPH)
        #fill(209, 147, 147)
        fill(255)
    elif nr < SUB1PERC:
        al += 1
        fill(242, 138, 138)
        rect(0, (i-mini+1) * RESPH - RESPH, 1200, RESPH)
        #fill(242, 190, 190)
        fill(255)
    else:
        al += 0
        fill(200, 200, 200)
        rect(0, (i-mini+1) * RESPH - RESPH, 1200, RESPH)
        #fill(230, 230, 230)
        fill(255)
    if nl - sl - al + pl <= 0:
        fill(45, 45, 45)
        rect(0, (i-mini+1) * RESPH - RESPH, 1200, RESPH)
        #fill(90, 90, 90)
        fill(255)
    nl -= sl + al - pl
    al += nl
    sl += al
    pl += sl
    textAlign(CENTER, CENTER)
    textFont(f, 84)
    text(contestant[0], 60-4, (i-mini+1) * RESPH + 50 - RESPH - 10)
    textAlign(LEFT, CENTER)
    textFont(f, 48)
    if textWidth(contestant[1]) > 700:
        textFont(f, 32)
    text(contestant[1], 110, (i-mini+1) * RESPH + 32 - RESPH - 10)
    k = textWidth(contestant[1])
    textFont(f, 20)
    if textWidth(contestant[2]) > 700:
        textFont(f, 16)
    fill(0, 0, 0)
    text(contestant[2], 119, (i-mini+1) * RESPH + 80 - RESPH - 10) 
    
        
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
    for y in range(3):
        for x in range(3):
            pos = y * 3 + x + 1
            if pos <= nl:
                displayHeart(NOLOSSNOGAIN, x, y, i, mini)
            elif pos <= al:
                if pl > sl:
                    pl -= 1
                    displayHeart(NOLOSSNOGAIN, x, y, i, mini)
                else:
                    displayHeart(FULLLOSS, x, y, i, mini)
            elif pos <= sl:
                if pl > sl and pl - sl > sl - pos:
                    pl -= 1
                    displayHeart(GSPELLLOSS, x, y, i, mini)
                else:
                    displayHeart(SPELLLOSS, x, y, i, mini)
            elif pos <= pl:
                displayHeart(GAINFULL, x, y, i, mini)
            else:
                displayHeart(PREVFULLLOSS, x, y, i, mini)    
    textFont(f, 36)
    text(contestant[5], 1010, (i-mini+1) * RESPH + 20 - RESPH)
    q = textWidth(contestant[5])
    textFont(f1)
    text("STDEV", 1010, (i-mini+1) * RESPH + 78 - RESPH)
    w = textWidth("STDEV")
    text("SCORE", 1010 + q + 5, (i-mini+1) * RESPH + 28 - RESPH)
    textFont(f, 36)
    text(contestant[6], 1010 + w + 5, (i-mini+1) * RESPH + 70 - RESPH)
    textFont(f, 16)
    if boost:
        text("{:+.2f}%".format(boost), 1010 + q - 2, (i-mini+1) * RESPH + 12 - RESPH)
        
    xoff = 0
    yoff = 0
    if contestant[8]:
        img = contestant[8]
        if img.height > img.width:
            img.resize(0, RESPH - 10)
            xoff = (RESPH - 4 - img.width) / 2
            yoff = 0
        else:
            img.resize(RESPH - 10, 0)
            xoff = 0
            yoff = (RESPH - 4 - img.width) / 2
            
        image(img, 810 + xoff + 8, 2 + RESPH * (i-mini+1) - RESPH + yoff) 
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

def setup():
    global inp
    global f
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
    size(1200, maxResps * RESPH)
    background(255, 255, 255, 100)
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
    PBG.resize(1200, 0)
    inp = [a.split("\t") for a in fin.split("\n")]
    print(PFont.list())
    for i in range(len(inp)):
        cont = inp[i]
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
    f = createFont("Agency FB Bold", 16, True)
    f1 = createFont("Segoe UI Bold", 16, True)
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
    mini = max(l - maxResps + 1, 1)
    maxi = l + 1
    background(255,255,255)
    for i in range(mini, maxi):
        if inp[i][0] == "-":
            dummy(i, mini)
        else:
            contestant(i, mini)
    

def keyTyped():
    global l
    global p
    if key == "s" or key == DOWN:
        if l < len(inp) - 1:
            l += 1
            print(l)
    if key == "e":
        save("{:d}.png".format(p))
        p += 1
    if key == "w" or key == UP:
        if l > 0:
            l -= 1
            print(l)
    if key == ENTER:
        if maxResps == len(inp) - 1:
            l = len(inp) - 1
    if key == "d":
        l = min(l + maxResps, len(inp) - 1)
    if key == "a":
        l = max(l - maxResps, 0)
