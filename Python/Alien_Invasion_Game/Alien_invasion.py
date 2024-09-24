import sys
import pygame
from time import sleep
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from scoreboard import Scoreboard
from settings import *


class Alieninvasion:  # 管理游戏资源和行为 #
    def __init__(self):
        pygame.init()  # 初始化背景 #

        self.clock = pygame.time.Clock()  # 创建 Clock 类实例控制帧率 #

        self.settings = Settings()  # 创建 Settings 类实例控制设置 #

        self.stats = GameStats(self)  # 创建 GameStats 类实例统计游戏信息 #

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))  # 利用元组设置游戏窗口大小 self.screen 对象是 surface(游戏窗口) #

        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)    # 在全屏模式下运行游戏 #
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        self.sb = Scoreboard(self)  # 创建 Scoreboard 类实例统计玩家信息 #

        pygame.display.set_caption("Alien Invasion")  # 设置游戏页面标签 #

        self.ship = Ship(self)  # 创建 Ship 类实例控制飞船 #
        self.bullets = pygame.sprite.Group()  # 调用 pygame.sprite 中的 Group 类来创建所有子弹实例的编组 #
        self.aliens = pygame.sprite.Group()  # 调用 pygame.sprite 中的 Group 类来创建所有外星人实例的编组 #
        self._create_fleet()  # 创建 Alien 类实例控制外星人 #
        self.game_active = False  # 游戏启动标志变量 #
        self.play_button = Button(self, 'PLAY')

    def run_game(self):  # 游戏主循环 #
        while True:
            self._check_events()  # 检测键鼠事件 #

            if self.game_active:
                self.ship.update()  # 更新飞船信息 #
                self._update_bullets()  # 更新子弹信息 #
                self._update_aliens()  # 更新外星人信息 #

            self._update_screen()  # 更新游戏窗口 #
            self.clock.tick(60)  # 调用 tick 设置更新和检测频率(帧率) #

    def _check_events(self):  # 响应键盘和鼠标事件 #
        for event in pygame.event.get():  # 调用 pygame.event.get 来捕捉事件 #

            if event.type == pygame.QUIT:  # 检查到关闭页面时 #
                sys.exit()  # 关闭游戏窗口 #

            elif event.type == pygame.KEYDOWN:  # 当事件类型为按下时 #
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:  # 当事件类型为抬起时 #
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):  # 检测按下事件 #

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

        elif event.key == pygame.K_q:  # 检测到按下[Q]键 #
            sys.exit()

    def _check_keyup_events(self, event):  # 检测抬起事件 #

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_play_button(self, mouse_pos):  # 检测到鼠标点击 [PLAY] 时开始(重置)f游戏 #
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.settings.initialize_dynamic_settings()  # 重置游戏难度 #
            self.stats.reset_stats()  # 重置玩家信息 #
            self.sb.prep_score()  # 重置得分 #
            self.sb.prep_level()  # 重置等级 #
            self.sb.prep_ships()  # 重置飞船 #
            self.game_active = True
            pygame.mouse.set_visible(False)  # 设置光标不可见 #

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()

    def _update_screen(self):  # 更新屏幕内容 切换屏幕 #
        self.screen.fill(self.settings.bg_color)  # 调用 fill 方法在每次更新屏幕时指定颜色填充游戏窗口(surface) #

        for bullet in self.bullets.sprites():  # 遍历列表中的所有子弹实例 #
            bullet.draw_bullet()  # 绘制子弹 #

        self.ship.blitme()  # 绘制飞船 #

        self.aliens.draw(self.screen)  # 绘制外星人 #

        self.sb.show_score()  # 绘制得分 #

        if not self.game_active:  # 当游戏暂停时 #
            self.play_button.draw_button()  # 最后绘制按钮确保在最上方显示 #

        pygame.display.flip()  # 调用 pygame.display.flip 更新屏幕 保持游戏窗口可见 #

    def _fire_bullet(self):  # 开火 #
        if len(self.bullets) < self.settings.bullet_allowed:  # 判断游戏窗口中的子弹数是否符合标准 #
            new_bullet = Bullet(self)  # 创建新的 Bullet 对象 #
            self.bullets.add(new_bullet)  # 存放在 Group 对象中 #

    def _update_bullets(self):  # 更新子弹信息 #
        self.bullets.update()  # 更新子弹位置 #
        for bullet in self.bullets.copy():  # 删除游戏窗口外的子弹 #
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collision()  # 处理子弹击中外星人的情况 #

    def _check_bullet_alien_collision(self):  # 检测子弹和外星人元素的位置 #
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)  # 删除重叠的游戏元素 #
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()  # 更新得分图像 #
            self.sb.check_high_score()  # 更新最高分图像 #

        if not self.aliens:  # 当所有的外星人被消灭时 #
            self.bullets.empty()  # 清除当前剩下的子弹 #
            self._create_fleet()  # 创建新的外星人军队 #
            self.settings.increase_speed()  # 增加游戏难度 #
            self.stats.level += 1
            self.sb.prep_level()  # 增加等级 #

    def _create_fleet(self):  # 召集外星人军队 #
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size  # 获取外星人宽度和长度 #
        current_x, current_y = alien_width, alien_height

        while current_y < (self.settings.screen_height - 3 * alien_height):  # 循环处理每个外星人的起始位置信息(嵌套) #
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width  # 每行添加外星人预留一些空间 #

            current_x = alien_width  # 每一行循环后重置横向起始位置 #
            current_y += 2 * alien_height  # 每列添加外星人预留一些空间 #

    def _create_alien(self, x_position, y_position):  # 召集单个外星人并设置位置信息 #
        new_alien = Alien(self)  # 创建外星人实例 #
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)  # 存放在 Group 对象中 #

    def _check_fleet_edges(self):  # 检查是否有外星人到达游戏窗口边缘 #
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _check_aliens_bottom(self):  # 检查是否有外星人到达游戏窗口底部 #
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _change_fleet_direction(self):  # 改变到达边缘的外星人的移动轨迹 #
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):  # 更新每个外星人信息 #
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _ship_hit(self):  # 当飞船撞毁时的信息处理 #
        if self.stats.ships_left > 1:
            self.stats.ships_left -= 1
            self.sb.prep_ships()  # 更新飞船 #
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(1)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)  # 设置光标可见 #


if __name__ == '__main__':
    ai = Alieninvasion()
    ai.run_game()
