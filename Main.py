import pygame
import sys
import random
import numpy as np
import copy
import time
import pprint

pygame.init()

# 색 상수
ARMADILLO = (71, 66, 60)  # 배경색
PAMPAS = (240, 235, 229)  # 사각형 배경색, 페이지 텍스트 색
SILVER = (190, 190, 190)  # 사각형 테두리 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Hide_Seek:
    def __init__(self):
        self.FPS = 30
        infoObject = pygame.display.Info()
        self.screen_size = (infoObject.current_w, infoObject.current_h)
        self.players = [[10,10]]

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.screen = pygame.display.set_mode((1520,580))

        self.font = pygame.font.SysFont("notosanscjkkr", 30)
        pygame.display.set_caption("hide_seek")

        self.player_x = 0
        self.player_y = 0

        self.player_size = 50

        self.speed = 10

        self.pos = [0,0]

        self.first_pos = [0,0] #임시
        self.clicked = False

        #object location
        self.exit_button_pos = [1150, 0, 400, 200] #(1150,0)에서 x로 400 y로 200

        self.boxs = [[300,300,300,300], [700,700,100,100]]

    def show_background(self):
        pygame.draw.rect(self.screen, ARMADILLO, (0, 0, self.screen_size[0], self.screen_size[1]))  # 배경 채우기

    def show_objects(self):
        pygame.draw.rect(self.screen, RED, self.exit_button_pos) #print exit_button
        for box in self.boxs:
            pygame.draw.rect(self.screen, WHITE, box)

    def show_pos(self):
        font_position = (230,500)
        self.screen.blit(self.font.render(f"{self.pos}", True, WHITE), font_position)

    def show_player(self):
        for plyaer in self.players:
            pygame.draw.circle(self.screen, BLACK, (plyaer[0], plyaer[1]), self.player_size)
        #print(self.player_x,self.player_y)

    def move_player(self):
        if self.is_not_in_box():
            self.players[0][0] += self.player_x
            self.players[0][1] += self.player_y

    def create_box(self): #임시 마우스로 box생성
        new_box = [0, 0, 0, 0]
        new_box[0] = self.first_pos[0]
        new_box[1] = self.first_pos[1]
        new_box[2] = self.pos[0] - self.first_pos[0]
        new_box[3] = self.pos[1] - self.first_pos[1]
        self.boxs.append(new_box)

        self.clicked = False


    def is_not_in_box(self):
        result = 0
        for box in self.boxs:
            if self.players[0][0] + self.player_x <= box[0] - self.player_size - 10 or self.players[0][0] + self.player_x >= box[0] + box[2] + self.player_size + 10\
                or self.players[0][1] + self.player_y <= box[1] -   self.player_size - 10 or self.players[0][1] + self.player_y >= box[1] + box[3] + self.player_size + 10:
                result += 1
            else:
                result += 0
        if result == len(self.boxs):
            return True
        else:
            return False
    def click_is_in_exit_button(self):
        if self.pos[0] >= self.exit_button_pos[0] and self.pos[0] <= self.exit_button_pos[0] + self.exit_button_pos[2] \
                and self.pos[1] >= self.exit_button_pos[1] and self.pos[1] <= self.exit_button_pos[1] + self.exit_button_pos[3]:
            return True
        else:
            return False

    def click(self):
        if self.clicked == False:
            self.clicked = True
            self.first_pos = self.pos
        elif self.clicked == True:
            self.create_box()
            self.clicked = False

        if self.click_is_in_exit_button():
            pygame.quit()
            sys.exit()

    def main(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.pos = pygame.mouse.get_pos()
                    self.click()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.player_y += self.speed
                    if event.key == pygame.K_UP:
                        self.player_y -= self.speed
                    if event.key == pygame.K_LEFT:
                        self.player_x -= self.speed
                    if event.key == pygame.K_RIGHT:
                        self.player_x += self.speed
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                        self.player_y = 0
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.player_x = 0

            self.show_background()
            self.show_pos()
            self.show_objects()
            self.show_player()
            self.move_player()

            pygame.display.flip()


if __name__ == "__main__":
    Hide_Seek().main()
