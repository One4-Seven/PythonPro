import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/alien.bmp')    # 设置外星人外观 #
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width    # 默认外星人在左上角出现 #
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):    # 更新外星人位置 #
        self.x += self.settings.alien_speed * self.settings.fleet_direction    # 速度 x 方向 #
        self.rect.x = self.x

    def check_edges(self):    # 检查外星人是否到达游戏窗口边缘 #
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)    # 到达边缘就会返回 True #
