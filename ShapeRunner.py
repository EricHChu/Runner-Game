'''
Shape Runner.py
Eric Chu
June 2021
A Game Where You Dodge Moving Blocks
'''

#Setup
import math
import pygame
pygame.init()
try:
    file = open("highScore.py", "x")
    file.write("highScore = 0")
    file.close()
    import highScore
except:
    import highScore

#Constants
WIDTH = 650
HEIGHT = 750
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
LGREEN = (173,255,0)
ARIAL = pygame.font.SysFont("Arial",50)
ARIALBIG = pygame.font.SysFont("Arial",75)
ARIALSMALL = pygame.font.SysFont("Arial",25)
SHAPE = ARIAL.render("Shape",0,BLACK)
RUNNER = ARIAL.render("Runner",0,BLACK)
PLAY = ARIAL.render("Play",0,BLACK)
INSTRUCTIONS = ARIAL.render("Instructions",0,BLACK)
INSTRUCTIONSWHITE = ARIAL.render("Instructions",0,WHITE)
EXIT = ARIAL.render("Exit",0,BLACK)
BACK = ARIAL.render("Back",0,BLACK)
HIGHSCORE = ARIAL.render("HIGH SCORE!",0,LGREEN)
HIGHSCOREDISPLAY = ARIAL.render("High Score: " + str(highScore.highScore),0,LGREEN)
GAMEOVER = ARIALBIG.render("Game Over!",0,RED)
PLAYAGAIN = ARIAL.render("Play Again",0,BLACK)
MENU = ARIAL.render("Menu",0,BLACK)
INSTRUCONE = ARIALSMALL.render("In this game, you are a circle that",0,WHITE)
INSTRUCTWO = ARIALSMALL.render("needs to dodge the falling blocks.",0,WHITE)
INSTRUCTHREE = ARIALSMALL.render("If you touch a block, you lose!",0,WHITE)
INSTRUCFOUR = ARIALSMALL.render("You can move between three lanes,",0,WHITE)
INSTRUCFIVE = ARIALSMALL.render("the left, middle and right.",0,WHITE)
INSTRUCSIX = ARIALSMALL.render("Press 'A' to move Left.",0,WHITE)
INSTRUCSEVEN = ARIALSMALL.render("Press 'D' to move Right.",0,WHITE)
INSTRUCEIGHT = ARIALSMALL.render("Survive For As Long As Possible!",0,WHITE)
SONG1 = pygame.mixer.Sound('Edited Song.mp3')
SONG1.set_volume(0.5)
SONG2 = pygame.mixer.Sound('GameOver.mp3')
SONG2.set_volume(0.5)
SONG3 = pygame.mixer.Sound('WaitingMusic.mp3')
SONG3.set_volume(0.5)
MAPONE = [pygame.Rect(75,-300,150,300),
          pygame.Rect(425,-850,150,300),
          pygame.Rect(250,-1400,150,300),
          pygame.Rect(75,-1950,150,300),
          pygame.Rect(425,-1950,150,300),
          pygame.Rect(250,-2650,150,450),
          pygame.Rect(75,-3900,150,1000),
          pygame.Rect(250,-3750,150,300),
          pygame.Rect(425,-3200,150,300),
          pygame.Rect(425,-4550,150,400),
          pygame.Rect(250,-4800,150,300),
          pygame.Rect(75,-5350,150,300),
          pygame.Rect(425,-5900,150,550),
          pygame.Rect(250,-6200,150,300),
          pygame.Rect(75,-6750,150,300)]

#Functions
def updateFile(val):
    file = open("highScore.py", "w")
    file.write("highScore = " + str(val))
    file.close()

def instructions():
    show = True
    while show:
        pygame.event.get()
        window.fill(BLACK)
        window.blit(INSTRUCTIONSWHITE,(325 - INSTRUCTIONSWHITE.get_rect().width / 2,100))
        window.blit(INSTRUCONE,(325 - INSTRUCONE.get_rect().width / 2,175))
        window.blit(INSTRUCTWO,(325 - INSTRUCTWO.get_rect().width / 2,225))
        window.blit(INSTRUCTHREE,(325 - INSTRUCTHREE.get_rect().width / 2,275))
        window.blit(INSTRUCFOUR,(325 - INSTRUCFOUR.get_rect().width / 2,325))
        window.blit(INSTRUCFIVE,(325 - INSTRUCFIVE.get_rect().width / 2,375))
        window.blit(INSTRUCSIX,(325 - INSTRUCSIX.get_rect().width / 2,425))
        window.blit(INSTRUCSEVEN,(325 - INSTRUCSEVEN.get_rect().width / 2,475))
        window.blit(INSTRUCEIGHT,(325 - INSTRUCEIGHT.get_rect().width / 2,525))
        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()
        if mouse[0] >= 50 and mouse [0] <= 270 and mouse[1] >= 650 and mouse[1] <= 725:
            pygame.draw.rect(window, (225,225,225), (50,650,220,75))
            if clicked[0] == 1:
                show = False
        else:
            pygame.draw.rect(window, WHITE, (50,650,220,75))
        window.blit(BACK,(110,660))
        pygame.display.update()

def playGame():
    playing = True
    gaming = True
    gameOver = False
    firstTime = True
    inGame = True
    while playing:
        pygame.event.get()
        window.fill(BLACK)
        if gaming == True:
            circleX = 325
            rate = 10
            speed = 100
            speedRamper = 0
            score = 0
            keyTimer = 0
            while inGame:
                pygame.event.get()
                window.fill(BLACK)
                keys = pygame.key.get_pressed()
                pygame.draw.circle(window,WHITE,(circleX,650),75)
                circleRect = pygame.Rect(circleX - 75, 575, 150,150)
                if firstTime == True:
                    pygame.display.update()
                    pygame.time.delay(500)
                    firstTime = False
                    SONG1.play()
                for count in range(len(MAPONE)):
                    if MAPONE[count].top + MAPONE[count].height + rate >= 0 and MAPONE[count].top - MAPONE[count].height - rate <= 750:
                        pygame.draw.rect(window,WHITE,(MAPONE[count].left,MAPONE[count].top + rate,MAPONE[count].width,MAPONE[count].height))
                        rect = pygame.Rect(MAPONE[count].left,MAPONE[count].top + rate,MAPONE[count].width,MAPONE[count].height)
                        if rect.colliderect(circleRect):
                            SONG1.stop()
                            SONG2.play()
                            pygame.time.delay(4150)
                            gaming = False
                            gameOver = True
                            inGame = False
                if rate >= 6950:
                    rate = 500
                rate = rate + 10
                if speedRamper == 20:
                    speed = speed - 1
                    print("sped up")
                    speedRamper = 0
                else:
                    speedRamper = speedRamper + 1
                score = score + (speed / 100)
                scoreText = ARIAL.render("Score: " + str(math.floor(score)), 0, LGREEN)
                scoreRect = scoreText.get_rect()
                window.blit(scoreText,(325 - (scoreRect.width / 2),50))
                if keys[97]:
                    if circleX == 150:
                        if keyTimer == 0:
                            print("edge")
                            keyTimer = 1
                    else:
                        if keyTimer == 0:
                            pygame.draw.circle(window,BLACK,(circleX,650),75)
                            circleX = circleX - 175
                            pygame.draw.circle(window,WHITE,(circleX,650),75)
                            keyTimer = 1
                elif keys[100]:
                    if circleX == 500:
                        if keyTimer == 0:
                            print("edge")
                            keyTimer = 1
                    else:
                        if keyTimer == 0:
                            pygame.draw.circle(window,BLACK,(circleX,650),75)
                            circleX = circleX + 175
                            pygame.draw.circle(window,WHITE,(circleX,650),75)
                            keyTimer = 1
                else:
                    keyTimer = 0
                pygame.time.delay(speed)
                pygame.display.update()
        elif gameOver == True:
            endGame = True
            SONG3.play(-1)
            while endGame:
                pygame.event.get()
                window.fill(BLACK)
                mouse = pygame.mouse.get_pos()
                clicked = pygame.mouse.get_pressed()
                gameOverSize = GAMEOVER.get_rect()
                window.blit(GAMEOVER,(325 - gameOverSize.width / 2,150))
                if highScore.highScore < score :
                    highScoreSize = HIGHSCORE.get_rect()
                    window.blit(HIGHSCORE,(325 - highScoreSize.width / 2,225))
                    updateFile(math.floor(score))
                scoreText = ARIAL.render("Score: " + str(math.floor(score)),0,LGREEN)
                scoreSize = scoreText.get_rect()
                window.blit(scoreText,(325 - scoreSize.width / 2, 300))
                if mouse[0] >= 215 and mouse [0] <= 500 and mouse[1] >= 500 and mouse[1] <= 575:
                    pygame.draw.rect(window,(225,225,225),(215,500,220,75))
                    if clicked[0] == 1:
                        SONG3.stop()
                        playGame()
                else:
                    pygame.draw.rect(window,WHITE,(215,500,220,75))
                window.blit(PLAYAGAIN,(325 - PLAYAGAIN.get_rect().width / 2,510))
                if mouse[0] >= 215 and mouse [0] <= 500 and mouse[1] >= 600 and mouse[1] <= 675:
                    pygame.draw.rect(window,(225,225,225),(215,600,220,75))
                    if clicked[0] == 1:
                        endGame = False
                        gameOver = False
                        playing = False
                else:
                    pygame.draw.rect(window,WHITE,(215,600,220,75))
                window.blit(MENU,(325 - MENU.get_rect().width / 2,610))
                pygame.display.update()

#Program
window = pygame.display.set_mode((WIDTH,HEIGHT))
height = 300
looped = False
active = True
SONG3.play(-1)
while active:
    pygame.event.get()
    window.fill(BLACK)
    if looped == False:
        for count in range(188):
            window.fill(BLACK)
            pygame.draw.rect(window, WHITE,(250,height,150,150))
            height = height - 1
            pygame.display.update()
            pygame.time.delay(7)
        looped = True
    else:
        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()
        pygame.draw.rect(window,WHITE,(250,height,150,150))
        window.blit(SHAPE,(265,127))
        window.blit(RUNNER,(257,187))
        if mouse[0] >= 215 and mouse [0] <= 435 and mouse[1] >= 345 and mouse[1] <= 420:
            pygame.draw.rect(window, (225,225,225), (215,345,220,75))
            if clicked[0] == 1:
                SONG3.stop()
                playGame()
        else:
            pygame.draw.rect(window, WHITE, (215,345,220,75))
        window.blit(PLAY,(285,353))
        if mouse[0] >= 215 and mouse [0] <= 435 and mouse[1] >= 425 and mouse[1] <= 500:
            pygame.draw.rect(window, (225,225,225), (215,425,220,75))
            if clicked[0] == 1:
                instructions()
                pygame.time.delay(100)
        else:
            pygame.draw.rect(window, WHITE, (215,425,220,75))
        window.blit(INSTRUCTIONS,(220,433))
        if mouse[0] >= 215 and mouse [0] <= 435 and mouse[1] >= 505 and mouse[1] <= 580:
            pygame.draw.rect(window, (225,225,225), (215,505,220,75))
            if clicked[0] == 1:
                pygame.quit()
        else:
            pygame.draw.rect(window, WHITE, (215,505,220,75))
        window.blit(EXIT,(285,513))
    window.blit(HIGHSCOREDISPLAY,(325 - HIGHSCOREDISPLAY.get_rect().width / 2,650))
    pygame.display.update()