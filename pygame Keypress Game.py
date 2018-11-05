##########################################
##  Matthew Brown, Bayside Secondary    ##
##  School.                             ##
##                                      ##
##  V1.0 created Apr.10 to June.15,     ##
##  2017.                               ##
##                                      ##
##  All assets made 100% by Me,         ##
##  including sounds.                   ##
##                                      ##
##  The game itself was inspired by     ##
##  Nerd³'s game, Systems Nominal.      ##
##  https://www.nerdcubed.co.uk/games/  ##
##########################################

import pygame, math, sys, time, random, os, pygame.gfxdraw

pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()
pygame.mixer.init()

##Define some colours

BLACK       = (0, 0, 0)
WHITE       = (255, 255, 255)
GRAY        = (230, 230, 230)
GREEN       = (10, 160, 55)
RED         = (215, 35, 35)
LIGHTGREEN  = (75, 245, 125)
LIGHTRED    = (255, 60, 60)
DARKRED     = (153, 0, 0)
YELLOW      = (255, 230, 35)
BLUE        = (0, 0, 255)
SKYBLUE     = (150, 215, 255)

WN_WIDTH    = 1000 #these two lines make it easeir to place things on the screen by relating it to the window's size.
WN_HEIGHT   = 800  #they are also useful because they let you quickly change the window size and keep most things in the same place.

size    = (WN_WIDTH, WN_HEIGHT)
screen  = pygame.display.set_mode((size))

pygame.display.set_caption("Keypress Game")

clock = pygame.time.Clock()

##Define some Fonts

monitorFont = pygame.font.Font("C:/Windows/Fonts/consola.ttf", 17)
monitorFontBold = pygame.font.Font("C:/Windows/Fonts/consolab.ttf", 17)
monitorFontBig = pygame.font.Font("C:/Windows/Fonts/consola.ttf", 62)
monitorFontBigBold = pygame.font.Font("C:/Windows/Fonts/consolab.ttf", 62)

##Define some Texts

def timerText(x, y): ## This has a special function so I can blit two chunks of text together using x and y as arugments. It keeps things relative.
    if int((timer-elapsed)*100+0.5)/100 > 0 and strikes > mistakes:
        timerText1 = monitorFont.render(">>> You have " + str(int((timer - elapsed)*100+0.5)/100), True, WHITE)
        timerText2 = monitorFont.render(" seconds left!", True, WHITE)
        screen.blit(timerText1,[x, y])
        screen.blit(timerText2,[x+162.5, y])

    elif int((timer-elapsed)*100+0.5)/100 <= 0 or strikes <= mistakes:
        timerText = monitorFont.render(">>> You have 0.00 seconds left!", True, WHITE)
        screen.blit(timerText,[x, y])

def highscoresText(x, y): ## Running this command will blit a block of the highscores onto the screen as if it was a sprite.
    highscores = scoresSTRING() #the scoresSTRING() function returns a list made of tuples, that look like: (ANA, 14313) #(not that she'd ever get a score that high)
    names = scoresSTRING()

    for i in range(0, (len(highscores))):
        highscores[i] = (highscores[i])[0]
    for i in range(0, (len(names))):
        names[i] = (names[i])[1]

    ## ^^ that block takes the two lists names and highscores (which both look the same currently)
    ## and makes them things like (ANA, MAT, ZAC, MVM) and (132, 20000, 1220, 0) (except in order).

    highscoresText    = monitorFont.render(">>> Highscores are:", True, WHITE)

    if "b" not in highscores[0]:
        highscore1Text      = monitorFont.render(">>> 1.  " + names[0] + " -- " + highscores[0], True, WHITE)
    elif "b" in highscores[0]:
        highscore1Text      = monitorFontBold.render(">>> 1.  " + names[0] + " -- " + highscores[0].split(":")[0], True, YELLOW)

    if "b" not in highscores[1]:
        highscore2Text      = monitorFont.render(">>> 2.  " + names[1] + " -- " + highscores[1], True, WHITE)
    elif "b" in highscores[1]:
        highscore2Text      = monitorFontBold.render(">>> 2.  " + names[1] + " -- " + highscores[1].split(":")[0], True, YELLOW)

    if "b" not in highscores[2]:
        highscore3Text      = monitorFont.render(">>> 3.  " + names[2] + " -- " + highscores[2], True, WHITE)
    elif "b" in highscores[2]:
        highscore3Text      = monitorFontBold.render(">>> 3.  " + names[2] + " -- " + highscores[2].split(":")[0], True, YELLOW)

    if "b" not in highscores[3]:
        highscore4Text      = monitorFont.render(">>> 4.  " + names[3] + " -- " + highscores[3], True, WHITE)
    elif "b" in highscores[3]:
        highscore4Text      = monitorFontBold.render(">>> 4.  " + names[3] + " -- " + highscores[3].split(":")[0], True, YELLOW)

    if "b" not in highscores[4]:
        highscore5Text      = monitorFont.render(">>> 5.  " + names[4] + " -- " + highscores[4], True, WHITE)
    elif "b" in highscores[4]:
        highscore5Text      = monitorFontBold.render(">>> 5.  " + names[4] + " -- " + highscores[4].split(":")[0], True, YELLOW)

    if "b" not in highscores[5]:
        highscore6Text      = monitorFont.render(">>> 6.  " + names[5] + " -- " + highscores[5], True, WHITE)
    elif "b" in highscores[5]:
        highscore6Text      = monitorFontBold.render(">>> 6.  " + names[5] + " -- " + highscores[5].split(":")[0], True, YELLOW)

    if "b" not in highscores[6]:
        highscore7Text      = monitorFont.render(">>> 7.  " + names[6] + " -- " + highscores[6], True, WHITE)
    elif "b" in highscores[6]:
        highscore7Text      = monitorFontBold.render(">>> 7.  " + names[6] + " -- " + highscores[6].split(":")[0], True, YELLOW)

    if "b" not in highscores[7]:
        highscore8Text      = monitorFont.render(">>> 8.  " + names[7] + " -- " + highscores[7], True, WHITE)
    elif "b" in highscores[7]:
        highscore8Text      = monitorFontBold.render(">>> 8.  " + names[7] + " -- " + highscores[7].split(":")[0], True, YELLOW)

    if "b" not in highscores[8]:
        highscore9Text      = monitorFont.render(">>> 9.  " + names[8] + " -- " + highscores[8], True, WHITE)
    elif "b" in highscores[8]:
        highscore9Text      = monitorFontBold.render(">>> 9.  " + names[8] + " -- " + highscores[8].split(":")[0], True, YELLOW)

    if "b" not in highscores[9]:
        highscore10Text      = monitorFont.render(">>> 10. " + names[9] + " -- " + highscores[9], True, WHITE)
    elif "b" in highscores[9]:
        highscore10Text      = monitorFontBold.render(">>> 10. " + names[9] + " -- " + highscores[9].split(":")[0], True, YELLOW)

    ## ^^ pretty self-explanatory. The one that is the newly achieved high scores is bolded, hence the ":b".

    screen.blit(highscoresText, [x, y])
    screen.blit(highscore1Text, [x, y+40])
    screen.blit(highscore2Text, [x, y+60])
    screen.blit(highscore3Text, [x, y+80])
    screen.blit(highscore4Text, [x, y+100])
    screen.blit(highscore5Text, [x, y+120])
    screen.blit(highscore6Text, [x, y+140])
    screen.blit(highscore7Text, [x, y+160])
    screen.blit(highscore8Text, [x, y+180])
    screen.blit(highscore9Text, [x, y+200])
    screen.blit(highscore10Text, [x, y+220])

    ## ^^ put them all on the screen right after each other

timeLeft = monitorFontBold.render("Time:", True, WHITE)
mistakesLeft = monitorFontBold.render("Mistakes Remaining:", True, WHITE)

##Define some Images

imgBKGD = pygame.image.load("metal texture.png")#.convert()

## Define some variables
## most of these are declared here so the game has a starting point.

timer = 30
strikes = 6

startingTimer = math.pi #because why not?

turn = 0
mistakes = 0
score = 0
timeTaken = 0

shamepick = 0

global CORRECTKEY
CORRECTKEY = 0

global keyPressed
keyPressed = ""

resetCheck = False
y_pressed = False
e_pressed = False
s_pressed = False

global highscores
global highscoresINT

meme_hack = False ## a hidden function they can activate in the game :P

## Define some game functions

def timerGraphic(cx, cy, radius):

    ##This function, along with its arguments, allows for the timer circle to be drawn
    #anywhere on the screen, and have all it's pieces stay together.

    angle = int(elapsed/timer * 360)
    ## ^^This basically says, "What percent through their time are they?"
    ## and then finds what x percent of 360 is, to see what angle the pie
    ## shape should be drawn to.

    points = [(cx, cy)]
    points_s = [(cx, cy)]

    ## ^^ starts two lists

    for i in range(0, angle):
        x = cx + int(radius*math.cos((i-90)*math.pi/180))
        y = cy + int(radius*math.sin((i-90)*math.pi/180))
        points.append((x, y))
    points.append((cx, cy))

    for i in range(0, angle):
        x = cx + int((radius-0.7)*math.cos((i-90)*math.pi/180))
        y = cy + int((radius-0.7)*math.sin((i-90)*math.pi/180))
        points_s.append((x, y))
    points_s.append((cx, cy))

    ## ^^ ^^ Adds points around the outside of the "circle" that will
    ## be the pie shape. Because pygame doesn't have a filled_pie()
    ## function, I need to use a workaround like this.
    ## The points_s list contains an identical polygon, but 0.7 pixels smaller.

    pygame.gfxdraw.aacircle(screen, cx, cy, radius+3, DARKRED)
    pygame.gfxdraw.filled_circle(screen, cx, cy, radius+3, DARKRED)
    pygame.gfxdraw.filled_circle(screen, cx, cy, radius, LIGHTRED)

    if len(points) > 2:
        pygame.gfxdraw.filled_polygon(screen, points_s, DARKRED)
        pygame.gfxdraw.aapolygon(screen, points, DARKRED)

    pygame.gfxdraw.aacircle(screen, cx, cy, radius, DARKRED)
    pygame.gfxdraw.aacircle(screen, cx, cy, (radius-1), DARKRED)

    ## ^^ those just draw the shapes that alias and hide rough edges of the
    ## un antialiasable shapes, like the polygon.

    ## So, for example of this whole function, the player has used up 12.4 seconds,
    ## and pressed 6 keys. Their total time will now be 33 seconds, because of the
    ## +0.5 seconds for each key.
    ## That means that the circle needs to fill (12.4/33*100 = 37.57)% of itself.
    ## For a circle, that means multiplying 0.3757 by 360. In this case, 135 degrees.
    ## Then, the for loop takes the list of the center points, and adds 135 points,
    ## plus the center point again to close the polygon.

    ## This drawing uses a trick: Instead of drawing a light circle and emptying it,
    ## since that would involve knowing every point on the circle and pulling all but
    ## the first and last out over time, it draws a light circle with a dark circle
    ## over top of it, and covers it up. That's why there are so many layers: to
    ## conceal the gap between the two.

    screen.blit(timeLeft, [cx-radius*1.75, cy-(radius/9)])

def lifeGraphic(cx, cy, h, w):
    x = cx - w/2
    y = cy - h/2

    pygame.draw.rect(screen, DARKRED, [x, y, w, h])
    pygame.draw.rect(screen, DARKRED, [x, y, w, h], 4)
    if mistakes < 5:
        pygame.draw.rect(screen, LIGHTRED, [x+1, y+1, w-(w*(mistakes/(strikes-1)))-1, h-1])

    ## this life bar is pretty simple. I use center-x and center-y so it would be easier to
    ## put in the same place as the timer. The (w-(w*(mistakes/(strikes-1)))-1) thing is
    ## the width of the red bar: The full width, minus whatever fraction of it is used up.
    ## So, if they've made 2 out of their 5 mistakes (the strikes variable is 6 because
    ## it's the sixth that kills them, hence the -6), and the width is 480 pixels, then
    ## it will become (480 - (480*2/5)), or two fifths less than 480. The negative one on
    ## the w and h is just to make it fit nicer in the outer box.

    screen.blit(mistakesLeft, [x + (w*1/100), y - (h*2/3)])

def drawKeys(color):

    key_locations_top_X = [x[0] for x in key_locations_top]
    key_locations_top_Y = [y[1] for y in key_locations_top]
    ## ^^ separates x from y and stores them in separate lists
    key_locations_mid_X = [x[0] for x in key_locations_mid]
    key_locations_mid_Y = [y[1] for y in key_locations_mid]
    ## ^^ this is the only code I found on the internet, LOL
    key_locations_bot_X = [x[0] for x in key_locations_bot]
    key_locations_bot_Y = [y[1] for y in key_locations_bot]

    for i in range(len(key_locations_top)):
        key_location_top_X = key_locations_top_X[i]
        key_location_top_Y = key_locations_top_Y[i]

        pygame.draw.rect(screen, color, [key_location_top_X, key_location_top_Y, 52, 52])

    for i in range(len(key_locations_mid)):
        key_location_mid_X = key_locations_mid_X[i]
        key_location_mid_Y = key_locations_mid_Y[i]

        pygame.draw.rect(screen, color, [key_location_mid_X, key_location_mid_Y, 52, 52])

    for i in range(len(key_locations_bot)):
        key_location_bot_X = key_locations_bot_X[i]
        key_location_bot_Y = key_locations_bot_Y[i]

        pygame.draw.rect(screen, color, [key_location_bot_X, key_location_bot_Y, 52, 52])

    if color == LIGHTGREEN:
        pygame.draw.line(screen, GREEN, (360, 630), (396, 630), 2) #F key's bump
        pygame.draw.line(screen, GREEN, (528, 630), (564, 630), 2) #J key's bump

    elif color == LIGHTRED:
        pygame.draw.line(screen, RED, (360, 630), (396, 630), 2) #F key's bump
        pygame.draw.line(screen, RED, (528, 630), (564, 630), 2) #J key's bump

def getCORKey():
    CORkey = random.randint(97, 122)
    return CORkey
    ## The randint is 97, 122 because the numbers 97 to 122 in ASCII represent "a" to "z".

def getCORSpot(key):
    ## This determines what row, and what key on that row starting from the left, each letter
    ## belongs to. This makes it very easy to use with lists.
    global CORKeyRow
    global CORKeyN

    if key == 113 or key == 119 or key == 101 or key == 114 or key == 116 or key == 121 or key == 117 or key == 105 or key == 111 or key == 112:
        CORKeyRow = 0
        if key == 113: CORKeyN = 0
        elif key == 119: CORKeyN = 1
        elif key == 101: CORKeyN = 2
        elif key == 114: CORKeyN = 3
        elif key == 116: CORKeyN = 4
        elif key == 121: CORKeyN = 5
        elif key == 117: CORKeyN = 6
        elif key == 105: CORKeyN = 7
        elif key == 111: CORKeyN = 8
        elif key == 112: CORKeyN = 9
        
    elif key == 97 or key == 115 or key == 100 or key == 102 or key == 103 or key == 104 or key == 106 or key == 107 or key == 108:
        CORKeyRow = 1
        if key == 97: CORKeyN = 0
        elif key == 115: CORKeyN = 1
        elif key == 100: CORKeyN = 2
        elif key == 102: CORKeyN = 3
        elif key == 103: CORKeyN = 4
        elif key == 104: CORKeyN = 5
        elif key == 106: CORKeyN = 6
        elif key == 107: CORKeyN = 7
        elif key == 108: CORKeyN = 8

    elif key == 122 or key == 120 or key == 99 or key == 118 or key == 98 or key == 110 or key == 109:
        CORKeyRow = 2
        if key == 122: CORKeyN = 0
        elif key == 120: CORKeyN = 1
        elif key == 99: CORKeyN = 2
        elif key == 118: CORKeyN = 3
        elif key == 98: CORKeyN = 4
        elif key == 110: CORKeyN = 5
        elif key == 109: CORKeyN = 6

def scoresDEF(): ##<< This function grabs the scores from the highscores.txt and puts the new score in it's place
    highscores = []
    highscoresINT = []

    file = open("highscores.txt", "r+") ## r+ means it gets opened in read/write mode

    for i in range(0, 10):
        data = file.readline() ## this command runs the next line each time it is run
        highscores.append(data) ## hence it being put in a loop

    file.close() ## once the data is in a list, it doesn't need to be open, using resources

    for i in range(0, 10): ## because the lines are imported as "11111:ABC\n", they have to be turned into (11111, "ABC").
        highscores[i] =  ( int(highscores[i].split(":")[0]), ((highscores[i]).split(":")[1]).split("\n")[0] )
        ## highscores[i] = "11111:ABC", so split(":")[0] is just 11111, and [1] is ABC. The ABC then has \n hacked off.
        highscoresINT.append((highscores[i])[0])

    for i in range(0, 10): #checks each item individually in the list against a list of just the numbers
        if score > (highscores[i])[0] and score not in highscoresINT:
            oldscore = highscores[i] # saves the score being replaced so it can move down in the list

            highscores[i] = (score, name)
            highscores.append(oldscore)

            highscoresINT.append(score)
            highscoresINT = (sorted(highscoresINT, reverse=True))[:10]

    highscores = (sorted(highscores, reverse=True))[:10]

    highscoresINT.append(score)
    highscoresINT = (sorted(highscoresINT, reverse=True))[:10] #[:10] keeps only the first 10 items.

    ## the score sorting works by putting the replaced score at the 11th spot, then sorting to get it into place, then taking off the last one.

    return highscores


def scoresSTRING(): ##<< this function returns the same list as the first function, but all in strings so it can be printed.
    highscores = scoresDEF()
    for i in range(0, 10):
        if (highscores[i])[0] == score:
            highscores[i] = ( str((highscores[i])[0]) + ":b", (highscores[i])[1])
            ##^^ the "new" score on the list is now (11111:b, ABC) so the program knows to bold it
        else:
            highscores[i] = ( str((highscores[i])[0]), (highscores[i])[1] )

    return highscores

def scoresWRITE(): ##<< writes the new list to file for storage
    highscores = scoresDEF()
    for i in range(0, 10):
        highscores[i] = ( str((highscores[i])[0]) + ":" + (highscores[i])[1] + "\n")

    file = open("highscores.txt", "r+")
    file.seek(0)
    file.truncate()
    for i in range(0, 10):
        file.write(highscores[i])
    file.close()

def scoresRESET(): ##<< resets the file and score to preset defaults.
    file = open("highscores.txt", "r+")
    file.seek(0)
    file.truncate()

    resetList = [
        '20000:aaa\n',
        '17500:bbb\n',
        '15000:ccc\n',
        '12500:ddd\n',
        '10000:eee\n',
        '7500:fff\n',
        '5000:ggg\n',
        '2500:hhh\n',
        '1000:iii\n',
        '50:jjj\n'
    ]

    score = 0
    name = ["A", "A", "A"]

    for i in range(0, 10):
        file.write(resetList[i])

    file.close()

## Main Game: ----------------------------------------------------------------------------------------------------------------------------------------------------------!!!
while True:
    ## initializes the key's locations --
    key_locations = []

    ## Top row
    global key_locations_top
    key_locations_top = []
    topRowX = 162
    topRowY = 532

    for i in range(0,10):
        key_locations_top.append(((topRowX + 56 * i), topRowY))

    ## Middle Row
    global key_locations_mid
    key_locations_mid = []
    midRowX = 184
    midRowY = 590
    #F = 352, 590
    #J = 520, 590

    for i in range(0,9):
        key_locations_mid.append(((midRowX + 56 * i), midRowY))

    ## Bottom Row
    global key_locations_bot
    key_locations_bot = []
    botRowX = 207
    botRowY = 648

    for i in range(0,7):
        key_locations_bot.append(((botRowX + 56 * i), botRowY))

    ## Whole Keyboard
    key_locations.append(key_locations_top)
    key_locations.append(key_locations_mid)
    key_locations.append(key_locations_bot)

    ## --

    ## Introduction: -----------------------------------------------
    opening = True

    while opening:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(), sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: pygame.quit(), sys.exit()
                elif event.key == pygame.K_BACKQUOTE and meme_hack == False: meme_hack = True
                elif event.key == pygame.K_BACKQUOTE and meme_hack == True: meme_hack = False
                else:
                    opening = False

        screen.blit(imgBKGD, [0,0]) ##Background
        pygame.draw.rect(screen, BLACK, [140, 80, 720, 355]) ##Monitor Screen
        drawKeys(LIGHTRED)

        explainText1 = monitorFont.render(">>> In this game, you will have to press keys as they turn red on", True, WHITE)
        explainText2 = monitorFont.render(">>> the keyboard you see below you.", True, WHITE)
        explainText3 = monitorFont.render(">>> You have 30 seconds, although each key you press will", True, WHITE)
        explainText4 = monitorFont.render(">>> earn you 0.5 extra.", True, WHITE)
        explainText5 = monitorFont.render(">>> You can make 5 mistakes, the sixth will make you lose.", True, WHITE)
        explainText6 = monitorFont.render(">>> Press any key when you are ready to continue.", True, WHITE)

        screen.blit(explainText1, [160, 100])
        screen.blit(explainText2, [160, 120])
        screen.blit(explainText3, [160, 140])
        screen.blit(explainText4, [160, 160])
        screen.blit(explainText5, [160, 180])
        screen.blit(explainText6, [160, 200])

        pygame.display.flip()
        clock.tick(60)

    startTime = time.time()
    endTime = time.time()
    elapsed = abs(endTime - startTime)
    elapsed = int(elapsed*100+0.5)/100

    while elapsed < startingTimer:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(), sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: pygame.quit(), sys.exit()
                elif event.key == pygame.K_BACKQUOTE and meme_hack == False: meme_hack = True
                elif event.key == pygame.K_BACKQUOTE and meme_hack == True: meme_hack = False

        pygame.draw.rect(screen, BLACK, [140, 80, 720, 355])

        countdown = monitorFont.render(">>> Starting in " + str(int((startingTimer - elapsed)*100+0.5)/100), True, WHITE)
        countdown2 = monitorFont.render("seconds.", True, WHITE)

        screen.blit(countdown, [160, 100])
        screen.blit(countdown2, [350, 100])
        pygame.display.flip()

        endTime = time.time()
        elapsed = abs(endTime - startTime)
        elapsed = int(elapsed*100+0.5)/100

        clock.tick(60)

    ## Main Game Loop: ---------------------------------------------
    startTime = time.time()
    starting = True
    mainGame = True

    while mainGame:

        ###
        if meme_hack:
            wrong = pygame.mixer.Sound("wrongmeme.wav")
            right = pygame.mixer.Sound("rightmeme.wav")
        else:
            wrong = pygame.mixer.Sound("wrong.wav")
            right = pygame.mixer.Sound("right.wav")

        ###

        endTime = time.time()
        elapsed = abs(endTime - startTime)
        elapsed = int(elapsed*100+0.5)/100

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(), sys.exit()

            if event.type == pygame.KEYDOWN:
                ##
                if event.key == pygame.K_q: keyPressed = 113
                elif event.key == pygame.K_w: keyPressed = 119
                elif event.key == pygame.K_e: keyPressed = 101
                elif event.key == pygame.K_r: keyPressed = 114
                elif event.key == pygame.K_t: keyPressed = 116
                elif event.key == pygame.K_y: keyPressed = 121
                elif event.key == pygame.K_u: keyPressed = 117
                elif event.key == pygame.K_i: keyPressed = 105
                elif event.key == pygame.K_o: keyPressed = 111
                elif event.key == pygame.K_p: keyPressed = 112
                ##-------------------------------------------
                elif event.key == pygame.K_a: keyPressed = 97
                elif event.key == pygame.K_s: keyPressed = 115
                elif event.key == pygame.K_d: keyPressed = 100
                elif event.key == pygame.K_f: keyPressed = 102
                elif event.key == pygame.K_g: keyPressed = 103
                elif event.key == pygame.K_h: keyPressed = 104
                elif event.key == pygame.K_j: keyPressed = 106
                elif event.key == pygame.K_k: keyPressed = 107
                elif event.key == pygame.K_l: keyPressed = 108
                ##-------------------------------------------
                elif event.key == pygame.K_z: keyPressed = 122
                elif event.key == pygame.K_x: keyPressed = 120
                elif event.key == pygame.K_c: keyPressed = 99
                elif event.key == pygame.K_v: keyPressed = 118
                elif event.key == pygame.K_b: keyPressed = 98
                elif event.key == pygame.K_n: keyPressed = 110
                elif event.key == pygame.K_m: keyPressed = 109
                ##
                elif event.key == pygame.K_ESCAPE: pygame.quit(), sys.exit()
                ##
                elif event.key == pygame.K_SPACE and game == "off": mainGame = False
                ##
                elif event.key == pygame.K_BACKQUOTE and meme_hack == False: meme_hack = True
                elif event.key == pygame.K_BACKQUOTE and meme_hack == True: meme_hack = False
                ##

        ## -- Game logic

        if starting == True: #this is what generates specifically the first key
            CORRECTKEY = getCORKey() ## Generates the new correct letter
            getCORSpot(CORRECTKEY)   ## and it's corresponding red key's location
            ## ^^ these two are in separate functions intead of being in one so that
            ## I could pull the integer of the right key out in case I needed to.
            REDKEY = (key_locations[CORKeyRow])[CORKeyN]
            REDKEY_X = REDKEY[0]
            REDKEY_Y = REDKEY[1]
            game = "running"

        if game == "running":
            if elapsed < timer and strikes > mistakes:

                if keyPressed == CORRECTKEY: ##If they get it right ------------------------------- !! RIGHT
                    keyPressed = ""
                    turn += 1
                    timer += 0.5

                    CORRECTKEY = getCORKey() ## this is the line that grabs the correct character
                    getCORSpot(CORRECTKEY)   ## this is the line that tells that spot on the screen to be red

                    REDKEY = (key_locations[CORKeyRow])[CORKeyN]
                    REDKEY_X = REDKEY[0]
                    REDKEY_Y = REDKEY[1]

                    right.play()

                elif keyPressed != CORRECTKEY and keyPressed == "": ##If they press nothing ------- !! NOTHING
                    keyPressed = ""

                else: ##wrong --------------------------------------------------------------------- !! WRONG
                    keyPressed = ""
                    mistakes += 1

                    ##

                    CORRECTKEY = getCORKey() ## this is the line that grabs the correct character
                    getCORSpot(CORRECTKEY)   ## this is the line that tells that spot on the screen to be red

                    REDKEY = (key_locations[CORKeyRow])[CORKeyN]
                    REDKEY_X = REDKEY[0]
                    REDKEY_Y = REDKEY[1]

                    ## ^^ those lines make it so that when you get it wrong you get a new key

                    wrong.play()

                game = "running"

            elif strikes <= mistakes: ### Failure condition one
                game = "off"
                reason = "mistakes"
                endendTime = time.time()
                endendTime = int(round(endendTime))

            elif elapsed >= timer: ### failure condition
                game = "off"
                reason = "time"
                endendTime = time.time()
                endendTime = int(round(endendTime))

        elif game == "off":
            endScreen = True
            timeTaken = abs(endendTime - startTime)
            score = (turn * (round(timeTaken*1.75)))-(mistakes * 100)

        ## -- Drawing code goes here ------------------------------------------------------------------------

            ## Define some texts

        if mistakes == 1:   ## makes sure it doesn't say "1 mistakeS"
            mistakesText    =   monitorFont.render(">>> You've made " + str(mistakes) + " mistake so far.", True, WHITE)
        else:
            mistakesText    =   monitorFont.render(">>> You've made " + str(mistakes) + " mistakes so far.", True, WHITE)

        goodText            =   monitorFont.render(">>> Goood job!", True, WHITE)

        failMistakes        =   monitorFont.render(">>> You made one too many mistakes!", True, WHITE)
        failTime            =   monitorFont.render(">>> Outta time!", True, WHITE)

        if shamepick == 0:   shamepick = random.randint(1, 4) ## if you get less than 0, you have 4 ways the game makes fun of you
        if shamepick == 1:   shameText           =   monitorFont.render(">>> Less than 0? " + str(score) + "? You really suck, dude.", True, WHITE)
        elif shamepick == 2: shameText           =   monitorFont.render(">>> Good grief, you're worse than I thought.", True, WHITE)
        elif shamepick == 3: shameText           =   monitorFont.render(">>> Try harder next time, okay?", True, WHITE)
        elif shamepick == 4: shameText           =   monitorFont.render(">>> " + str(score) + "? Jeez, you stink.", True, WHITE)

        keysHit             =   monitorFont.render(">>> You managed to hit " + str(turn) + " keys correctly.", True, WHITE)

        if mistakes == 1:   ## makes sure it doesn't say "1 mistakeS"
            mistakesMade    =   monitorFont.render(">>> You made " + str(mistakes) + " mistake.", True, WHITE)
        else:
            mistakesMade    =   monitorFont.render(">>> You made " + str(mistakes) + " mistakes.", True, WHITE)

        thankText1          =   monitorFont.render(">>> Thank you for playing.", True, WHITE)
        thankText2          =   monitorFont.render(">>> Game, as well as all assets created by Matthew Brown.", True, WHITE)
        thankText3          =   monitorFont.render(">>> Inspired by 'Systems Nominal', a game by Nerd³.", True, WHITE)

        memeText        =   monitorFontBold.render(">>> MEME HACK ACTIVATED", True, RED)

            ## ----------------

        screen.blit(imgBKGD, [0,0]) ##Background
        pygame.draw.rect(screen, BLACK, [140, 80, 720, 355]) ##Monitor Screen

        if game == "running":
            drawKeys(LIGHTGREEN)
            pygame.draw.rect(screen, LIGHTRED, [REDKEY_X, REDKEY_Y, 52, 52]) ##THE red key that you have to press

            if CORKeyRow == 1 and CORKeyN == 3:
                pygame.draw.line(screen, RED, (360, 630), (396, 630), 2) #F key's bump
            elif CORKeyRow == 1 and CORKeyN == 6:
                pygame.draw.line(screen, RED, (528, 630), (564, 630), 2) #J key's bump

            timerText(160,100)
            timerGraphic(cx = 500, cy = 260, radius = 80) #cx and cy = center's x and y point of the timer circle
            lifeGraphic(cx = 500, cy = 380, h = 25, w = 500)
            screen.blit(mistakesText, [160, 140])

            if meme_hack: screen.blit(memeText, [0,0])

        elif game == "off":
            endScreen = True
            nameGet = True
            name = ["A", "A", "A"]

            timeTaken = abs(endendTime - startTime)
            timeAlive = monitorFont.render(">>> You stayed alive for " + str(round(timeTaken)) + " seconds.", True, WHITE)

            if score < 0:
                scoreText = monitorFontBold.render(">>> Your final score is: " + str(score) + ".", True, LIGHTRED)
            else:
                scoreText = monitorFontBold.render(">>> Your final score is: " + str(score) + ".", True, YELLOW)

            contText = monitorFont.render(">>> Press Space to continue.", True, WHITE)

            screen.blit(imgBKGD, [0,0]) ##Background
            pygame.draw.rect(screen, BLACK, [140, 80, 720, 355]) ##Monitor Screen
            drawKeys(LIGHTRED)

            if reason == "mistakes":
                screen.blit(failMistakes, [160, 100])
            elif reason == "time":
                screen.blit(failTime, [160, 100])

            screen.blit(keysHit, [160, 140])
            screen.blit(timeAlive, [160,160])
            screen.blit(mistakesMade, [160, 180])
            screen.blit(scoreText, [160, 240])

            #screen.blit(thankText1, [160, 280])
            #screen.blit(thankText2, [160, 300])
            #screen.blit(thankText3, [160, 320])

            screen.blit(contText, [160, 360])

            if score < 0:
                screen.blit(shameText, [160, 260])

        starting = False
        ## This variable is used only on the first run through to generate the first key.
        ## After that, it is generated when the user gets it right/wrong.
        pygame.display.flip()
        clock.tick(60)

    ### ending screen

    while endScreen:
        pos = 0
        ### get their name for highscores
        while nameGet == True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(), sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: pygame.quit(), sys.exit()
                    if event.key == pygame.K_RETURN: pos += 1
                    if pos != 2:
                        if event.key == pygame.K_RIGHT: pos += 1
                    if pos != 0:
                        if event.key == pygame.K_LEFT: pos -= 1
                        if event.key == pygame.K_BACKSPACE: pos -= 1

                    if pos == 2:
                        if event.key == pygame.K_a: name[pos] = "A"
                        elif event.key == pygame.K_b: name[pos] = "B"
                        elif event.key == pygame.K_c: name[pos] = "C"
                        elif event.key == pygame.K_d: name[pos] = "D"
                        elif event.key == pygame.K_e: name[pos] = "E"
                        elif event.key == pygame.K_f: name[pos] = "F"
                        elif event.key == pygame.K_g: name[pos] = "G"
                        elif event.key == pygame.K_h: name[pos] = "H"
                        elif event.key == pygame.K_i: name[pos] = "I"
                        elif event.key == pygame.K_j: name[pos] = "J"
                        elif event.key == pygame.K_k: name[pos] = "K"
                        elif event.key == pygame.K_l: name[pos] = "L"
                        elif event.key == pygame.K_m: name[pos] = "M"
                        elif event.key == pygame.K_n: name[pos] = "N"
                        elif event.key == pygame.K_o: name[pos] = "O"
                        elif event.key == pygame.K_p: name[pos] = "P"
                        elif event.key == pygame.K_q: name[pos] = "Q"
                        elif event.key == pygame.K_r: name[pos] = "R"
                        elif event.key == pygame.K_s: name[pos] = "S"
                        elif event.key == pygame.K_t: name[pos] = "T"
                        elif event.key == pygame.K_u: name[pos] = "U"
                        elif event.key == pygame.K_v: name[pos] = "V"
                        elif event.key == pygame.K_w: name[pos] = "W"
                        elif event.key == pygame.K_x: name[pos] = "X"
                        elif event.key == pygame.K_y: name[pos] = "Y"
                        elif event.key == pygame.K_z: name[pos] = "Z"

                    else:
                        if event.key == pygame.K_a:
                            name[pos] = "A"
                            pos += 1
                        elif event.key == pygame.K_b:
                            name[pos] = "B"
                            pos += 1
                        elif event.key == pygame.K_c:
                            name[pos] = "C"
                            pos += 1
                        elif event.key == pygame.K_d:
                            name[pos] = "D"
                            pos += 1
                        elif event.key == pygame.K_e:
                            name[pos] = "E"
                            pos += 1
                        elif event.key == pygame.K_f:
                            name[pos] = "F"
                            pos += 1
                        elif event.key == pygame.K_g:
                            name[pos] = "G"
                            pos += 1
                        elif event.key == pygame.K_h:
                            name[pos] = "H"
                            pos += 1
                        elif event.key == pygame.K_i:
                            name[pos] = "I"
                            pos += 1
                        elif event.key == pygame.K_j:
                            name[pos] = "J"
                            pos += 1
                        elif event.key == pygame.K_k:
                            name[pos] = "K"
                            pos += 1
                        elif event.key == pygame.K_l:
                            name[pos] = "L"
                            pos += 1
                        elif event.key == pygame.K_m:
                            name[pos] = "M"
                            pos += 1
                        elif event.key == pygame.K_n:
                            name[pos] = "N"
                            pos += 1
                        elif event.key == pygame.K_o:
                            name[pos] = "O"
                            pos += 1
                        elif event.key == pygame.K_p:
                            name[pos] = "P"
                            pos += 1
                        elif event.key == pygame.K_q:
                            name[pos] = "Q"
                            pos += 1
                        elif event.key == pygame.K_r:
                            name[pos] = "R"
                            pos += 1
                        elif event.key == pygame.K_s:
                            name[pos] = "S"
                            pos += 1
                        elif event.key == pygame.K_t:
                            name[pos] = "T"
                            pos += 1
                        elif event.key == pygame.K_u:
                            name[pos] = "U"
                            pos += 1
                        elif event.key == pygame.K_v:
                            name[pos] = "V"
                            pos += 1
                        elif event.key == pygame.K_w:
                            name[pos] = "W"
                            pos += 1
                        elif event.key == pygame.K_x:
                            name[pos] = "X"
                            pos += 1
                        elif event.key == pygame.K_y:
                            name[pos] = "Y"
                            pos += 1
                        elif event.key == pygame.K_z:
                            name[pos] = "Z"
                            pos += 1

            if pos >= 3:
                name = "".join(name) #takes their input as ['M', 'A', 'T'] and turns it into "MAT"
                scoresWRITE()
                nameGet = False

            if pos == 0:
                letter1 = monitorFontBigBold.render(name[0], True, YELLOW)
                letter2 = monitorFontBig.render(name[1], True, WHITE)
                letter3 = monitorFontBig.render(name[2], True, WHITE)
            if pos == 1:
                letter1 = monitorFontBig.render(name[0], True, WHITE)
                letter2 = monitorFontBigBold.render(name[1], True, YELLOW)
                letter3 = monitorFontBig.render(name[2], True, WHITE)
            if pos == 2:
                letter1 = monitorFontBig.render(name[0], True, WHITE)
                letter2 = monitorFontBig.render(name[1], True, WHITE)
                letter3 = monitorFontBigBold.render(name[2], True, YELLOW)

            nameSplainText = monitorFont.render(">>> Type your initials/name. This will be used to keep track of highscores.", True, WHITE)

            screen.blit(imgBKGD, [0,0]) ##Background
            pygame.draw.rect(screen, BLACK, [140, 80, 720, 355]) ##Monitor Screen
            drawKeys(LIGHTRED)

            screen.blit(nameSplainText, [160, 100])
            screen.blit(letter1, [415, 180])
            screen.blit(letter2, [465, 180])
            screen.blit(letter3, [515, 180])

            clock.tick(60)
            pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(), sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:

                    timer = 30

                    turn = 0
                    mistakes = 0
                    score = 0
                    timeTaken = 0

                    shamepick = 0

                    mainGame = True
                    endScreen = False

                elif event.key == pygame.K_r:
                    resetCheck = True

                elif event.key == pygame.K_n: pygame.quit(), sys.exit()
                ##
                elif event.key == pygame.K_ESCAPE: pygame.quit(), sys.exit()

        ## screen drawing

        askText = monitorFont.render(">>> Do you want to play again? Press either 'Y' or 'N'.", True, WHITE)
        askText2 = monitorFont.render(">>> Do you want to reset the highscores? Press 'R' if you do.", True, WHITE)

        screen.blit(imgBKGD, [0,0]) ##Background
        pygame.draw.rect(screen, BLACK, [140, 80, 720, 355]) ##Monitor Screen
        drawKeys(LIGHTRED)

        highscoresText(160, 100)
        screen.blit(askText, [160, 360])
        screen.blit(askText2, [160, 380])

        clock.tick(60)
        pygame.display.flip()

        while resetCheck: ##if they can't take the pain and want some easier scores to beat.

            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(), sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: pygame.quit(), sys.exit()
                    elif event.key == pygame.K_y: y_pressed = True
                    elif event.key == pygame.K_e: e_pressed = True
                    elif event.key == pygame.K_s: s_pressed = True

                    elif event.key == pygame.K_c: resetCheck = False

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_y: y_pressed = False
                    elif event.key == pygame.K_e: e_pressed = False
                    elif event.key == pygame.K_s: s_pressed = False

            if y_pressed and e_pressed and s_pressed:

                scoresRESET()

                y_pressed = False
                e_pressed = False
                s_pressed = False

                resetCheck = False

            ## screen drawing

            doubleCheckText = monitorFont.render(">>> Are you extra, super sure? If you are, hold down 'Y', 'E', and 'S'", True, WHITE)
            doubleCheckText2 = monitorFont.render(">>> all at the same time. Press 'C' to cancel.", True, WHITE)

            y_text = monitorFont.render(">>> Y", True, WHITE)
            e_text = monitorFont.render(">>> E", True, WHITE)
            s_text = monitorFont.render(">>> S", True, WHITE)

            screen.blit(imgBKGD, [0,0]) ##Background
            pygame.draw.rect(screen, BLACK, [140, 80, 720, 355]) ##Monitor Screen
            drawKeys(LIGHTRED)

            screen.blit(doubleCheckText, [160, 100])
            screen.blit(doubleCheckText2, [160, 120])

            if y_pressed: screen.blit(y_text, [160, 160])
            if e_pressed: screen.blit(e_text, [160, 180])
            if s_pressed: screen.blit(s_text, [160, 200])

            clock.tick(60)
            pygame.display.flip()
