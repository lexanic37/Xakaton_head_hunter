#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import pygame

MOVE_SPEED = 7
WIDTH = 76
HEIGHT = 220
COLOR = "#888888"


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.image.blit(pygame.image.load("test_gg1.png"),[0,0])
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект

    def update(self, left, right):
        if left:
            self.xvel = -MOVE_SPEED  # Лево = x- n

        if right:
            self.xvel = MOVE_SPEED  # Право = x + n

        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0

        self.rect.x += self.xvel  # переносим свои положение на xvel



    def draw(self, screen):  # Выводим себя на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))
