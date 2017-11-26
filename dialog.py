import pygame
import string
from pygame import *
import sys
import codecs
# -*- coding: utf-8 -*-
COLOR = (0, 0, 0, 75)
TOP = 0
BOT = 480
LEFT = 0
RIGHT = 705
aqua      = (  0, 255, 255)   # ??????? ?????
black     = (  0,   0,   0)   # ??????
blue      = (  0,   0, 255)   # ?????
fuchsia   = (255,   0, 255)   # ??????
gray      = (128, 128, 128)   # ?????
green     = (  0, 128,   0)   # ???????
lime      = (  0, 255,   0)   # ???? ?????
maroon    = (128,   0,   0)   # ?????-????????
navy_blue = (  0,   0, 128)   # ?????-?????
olive     = (128, 128,   0)   # ?????????
purple    = (128,   0, 128)   # ??????????
red       = (255,   0,   0)   # ???????
silver    = (192, 192, 192)   # ??????????
teal      = (  0, 128, 128)   # ??????-???????
white     = (255, 255, 255)   # ?????
yellow    = (255, 255,   0)   # ??????
class Dialog(sprite.Sprite):
    def __init__(self,x,y, phrases, choice_dialogs, true_choice, points,sdvig=0):
        sprite.Sprite.__init__(self)
        self.body = Surface((270,480), pygame.SRCALPHA)
        self.startX = x  # ????????? ??????? ?, ?????????? ????? ????? ???????????? ???????
        self.startY = y
        self.body.fill(COLOR)
        self.player = []
        self.enemy = []
        self.phrases= phrases
        self.current_phrase = 0
        self.phr_away = []
        self.choice_dialogs = choice_dialogs
        self.Is_next_scene = 0
        self.true_choice = true_choice
        self.points = points
        self.sdvig = sdvig
    def open(self, screen, truth):
        if truth:
            screen.blit(self.body, (370,0))
        else:
            self.close()

    def show_next(self,screen,truth=False,choice=0):
        margin = 0

        if choice:
            self.choice_manager(choice)
        elif not len(self.phr_away) >= len(self.phrases)+1:

            if not truth:
                for i in self.phr_away:
                    margin+=15
                    self.show(screen,i,margin)
            elif truth == None:
                pass
            else:
                if  not len(self.phrases) == self.current_phrase:
                    self.current_phrase +=1
                    try:
                        self.phr_away.append(self.phrases[self.current_phrase])
                    except:
                        self.Is_next_scene = +1
                    for i in self.phr_away:
                        margin+=15
                        self.show(screen,i,margin)
        else:
            pass

    def close(self):
        pass

    def show(self,screen,phrase, margin):
        fontObj = font.Font('arial.ttf', 15)
        textSurfaceObj = fontObj.render(phrase, True, red)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (RIGHT-200, TOP + 10 + margin)
        screen.blit(textSurfaceObj, textRectObj)


    def choice_manager(self,choice):
        if choice ==1 :
            self.phrases.append(self.choice_dialogs[0])

        elif choice ==2  :
            self.phrases.append(self.choice_dialogs[1])

        elif choice ==3 :
            self.phrases.append(self.choice_dialogs[2])
        if choice == self.true_choice:
            self.points+= 100
        else:
            self.points -=100



