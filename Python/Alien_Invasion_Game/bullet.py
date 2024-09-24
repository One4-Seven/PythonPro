import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)    # 初始化子弹模型(矩形) #
        self.rect.midtop = ai_game.ship.rect.midtop    # 设置子弹位置 #
        self.y = float(self.rect.y)    # 存储子弹当前位置 #

    def update(self):    # 更新子弹位置 #
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):    # 填充(绘制)子弹模型 #
        pygame.draw.rect(self.screen,self.color,self.rect)
