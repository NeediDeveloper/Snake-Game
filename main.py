import pygame
import random
import os
from pygame.locals import *

pygame.init()
pygame.mixer.init()

white = (255,255,255)
black = (0,0,0)
red = (255, 2, 2)
green = (4, 186, 46)
yellow =(217, 245, 2)

ScreenWidth = 600
ScreenHeight = 600
Screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption("Snakes By Mr.M.N.A")
bgimg = pygame.image.load('background.png')
bgimg = pygame.transform.scale(bgimg,(ScreenWidth , ScreenHeight)).convert_alpha()

pygame.display.update()
Clock = pygame.time.Clock()

def Snake_Plot(Screen,color,SnakeList,SnakeSize):
    for x,y in SnakeList:
        pygame.draw.rect(Screen,color,[x,y,SnakeSize,SnakeSize])

Font = pygame.font.SysFont(None,40)
def TextOnScreen(text, color,x ,y):
    ScreenText = Font.render(text,True, color)
    Screen.blit(ScreenText,[x,y])

wlcmimg = pygame.image.load('welcomeScreen.jpg')
wlcmimg = pygame.transform.scale(wlcmimg,(ScreenWidth , ScreenHeight)).convert_alpha()


GOver = pygame.image.load('game_over.png')
GOver = pygame.transform.scale(GOver,(ScreenWidth , ScreenHeight)).convert_alpha()

def Welcome():
    ExitGame = False
    while not ExitGame:
        Screen.blit(wlcmimg,(0,0))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ExitGame = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        ExitGame = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        GameLoop()        
        pygame.display.update()
        Clock.tick(60)


Food = pygame.image.load('food.png')
Food = pygame.transform.scale(Food,(25 , 25)).convert_alpha()
def GameLoop():
    Score = 0
    Fps = 40
    SnakeList = []
    SnakeLenght = 1
    FoodX = random.randint(50,550) 
    FoodY = random.randint(50, 550) 
    SnakeX = 45
    SnakeY = 55
    SnakeSize = 25
    VelocityX = 0
    VelocityY = 0
    InitVelocity = 5
    ExitGame = False
    GameOver = False

    if (not os.path.exists("HiScore.txt")):
        with open("HiScore.txt", "w")as f:
            f.write("0")
    else:
        with open("HiScore.txt", "r")as f:
            HiScore = f.read()
        
    while not ExitGame:
        if GameOver:
            with open("HiScore.txt", "w")as f:
                f.write(str(HiScore))
            Screen.blit(GOver,(0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ExitGame = True
                if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        ExitGame = True
                    
                if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        GameLoop()
        else:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ExitGame = True
                if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        ExitGame = True
                    if event.type ==pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            VelocityX -= InitVelocity 
                            VelocityY = 0
                        if event.key == pygame.K_RIGHT:
                            VelocityX += InitVelocity 
                            VelocityY = 0
                        if event.key == pygame.K_UP:
                            VelocityY -= InitVelocity 
                            VelocityX = 0
                        if event.key == pygame.K_DOWN:
                            VelocityY += InitVelocity 
                            VelocityX = 0
                    
            SnakeX += VelocityX   
            SnakeY += VelocityY   
            
            if abs(SnakeX - FoodX)<20 and abs(SnakeY - FoodY)< 20:
                Score += 1
                pygame.mixer.music.load('beep.mp3')
                pygame.mixer.music.play()
                FoodX = random.randint(50,550) 
                FoodY = random.randint(50, 550) 
                SnakeLenght += 5
                if Score > int(HiScore):
                    HiScore = Score
                
            Screen.blit(bgimg,(0,0))
            TextOnScreen("Score : " + str( Score ) , white , 5 , 5)
            TextOnScreen("High Score : " + str(HiScore),red , 150 , 5)
            Screen.blit(Food,(FoodX,FoodY))
            
            Head = []
            Head.append(SnakeX)
            Head.append(SnakeY)
            SnakeList.append(Head)
            
            if len (SnakeList) > SnakeLenght:
                del SnakeList[0]
            
            if SnakeX < 0 or SnakeX > ScreenWidth or SnakeY < 0 or SnakeY > ScreenHeight:
                GameOver = True
                pygame.mixer.music.load('crash.mp3')
                pygame.mixer.music.play()
            if Head in SnakeList [:-1]:
                GameOver = True
                pygame.mixer.music.load('crash.mp3')
                pygame.mixer.music.play()
            Snake_Plot(Screen,yellow,SnakeList,SnakeSize,)
            
        pygame.display.update()
        Clock.tick(Fps)

    pygame.quit()
    quit()
Welcome()