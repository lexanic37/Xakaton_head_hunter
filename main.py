#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Импортируем библиотеку pygame
import sys
import pygame
from pygame import *
from player import *
from dialog import *
from time import sleep



# Объявляем переменные
WIN_WIDTH = 640  # Ширина создаваемого окна
WIN_HEIGHT = 480  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_IMAGE = pygame.image.load("room1.png")

hero = Player(55,240) # создаем героя по (x,y) координатам
    # по умолчанию — стоим
def show_points(screen, dialog):
    fontObj = font.Font('ad.ttf', 20)
    textSurfaceObj = fontObj.render(str(dialog.points), True, red)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (20, 10 )
    screen.blit(textSurfaceObj, textRectObj)

def main():

    pygame.init()  # Инициация PyGame, обязательная строчка

    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Headhunter")  # Пишем в шапку
    global bg
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    bg.blit(BACKGROUND_IMAGE,[0,0])  # Заливаем поверхность сплошным цветом
    left = False
    right = False
    truth = False
    truth_show= False
    dialog = Dialog(430, 0,
                    ['*zvonit telefon*', '*zvonit telefon*', u'yan: kto eto chert vozmi zvonit tak', 'rano?',
                     '*beret trubku*',
                     'boss: pochemu eto ya ne vizhu tebya na', 'rabochem meste?',
                     'yan: ya zastryal v probke. skoro budu.',
                     'boss: yy tebe stoit potoropitsya,', 'inache nam pridetsya iskat novogo rekrutera!',
                     '*lozhit trubku*',
                     'yan: blin, tak golova bolit. poxodu', 'perebral vchera', 'yan: dumayu, vsyo-taki samoe vremya po',
                     'yavitsya na rabote./'],
                    ['asdsad1', 'asdsad2', 'asdsadasd3'],2,0)
    choice=0
    d = True
    p = 1

    timer = pygame.time.Clock()
    while 1:  # Основной цикл программы
        timer.tick(60)
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True


            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYDOWN and e.key == K_SPACE:
                if p == 1:
                    truth = True
                    p = 0
                    truth_show = True
                else :
                    truth = False
                    p = 1
                    truth_show = None
            if e.type ==KEYDOWN and e.key == K_n:
                truth_show = True

            if e.type == KEYDOWN and e.key == K_1:
                choice = 1
            if e.type == KEYDOWN and e.key == K_2:
                choice = 2
            if e.type == KEYDOWN and e.key == K_3:
                choice = 3
        # choice_manager
            if dialog.Is_next_scene==1:
                dialog = Dialog(430,0,['sds','boss: pochemu tak dolgo?','yan: ya zhe uzhe govoril chto byla ','ogromnaya probka.','boss: probka? u tebya kazhdyj den',
 'probka, a glaza u tebya kak u ','protuxshej ryby. privedi sebya v','poryadok', '1) naxamit','2) na samom dele ya nemnogo vypilvchera '  ,'s drugom vypil vchera s drugom',
'3) xorosho, ya privedu/' ],['ty eshhyo pogovori so mnoj tak !','o, nakonec taki ya uslyshal ottebya pravdu.','postarajsya . inache eto budet tvoyo poslednee opozdanie.'],3,dialog.points)
                bg.blit(pygame.image.load('office.png'), (0, 0))
            elif dialog.Is_next_scene ==2 :
                dialog = Dialog(430, 0,['*zaxodit na site*','Yan: tak, u nas est neskol','ko potencialno vozmojnih kadrov','Yan: kogo je vibrat','1 pretendnet','2pretendnet','3 pretendnet'],['a'],1,dialog.points,0)
                bg.blit(pygame.image.load('site_end.png'),(0,0))



        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
        hero.update(left=left, right=right)  # передвижение
        hero.draw(screen)
        dialog.open(screen, truth)
        dialog.show_next(screen,truth_show)
        truth_show = False
        dialog.show_next(screen,choice = choice)
        show_points(screen,dialog)
        choice = False


        pygame.display.update()  # обновление и вывод всех изменений на экран



if __name__ == "__main__":
    main()