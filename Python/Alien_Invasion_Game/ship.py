import pygame
from pygame.sprite import Sprite


class Ship(Sprite):  # 管理飞船属性 #
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')  # 设置飞船外观 #

        self.rect = self.image.get_rect()

        self.center_ship()

        self.moving_right = False  # 飞船移动标志 #
        self.moving_left = False

    def update(self):  # 更新飞船位置 #
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):  # 在游戏窗口显示飞船 #
        self.screen.blit(self.image, self.rect)
