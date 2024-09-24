class Settings:  # 管理游戏设置 #
    def __init__(self):  # 初始化游戏基本设置 #
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # 设置背景颜色(用RPG值指定) #
        self.ship_limit = 3  # 飞船总数 #

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)  # 设置子弹颜色 #
        self.bullet_allowed = 20  # 设置游戏窗口的最大子弹存在数 #

        self.fleet_drop_speed = 10  # 设置外星人下坠速度 #

        self.speedup_scale = 1.2
        self.Score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):  # 初始化游戏难度设置 #
        self.ship_speed = 1.5  # 设置飞船速度 #
        self.bullet_speed = 2.0  # 设置子弹速度 #
        self.alien_speed = 1.0  # 设置外星人速度 #
        self.fleet_direction = 1  # 外星人移动方向(左右)的标志变量 #
        self.alien_points = 50  # 击落外星人得分 #

    def increase_speed(self):  # 增加游戏难度(提高速度 提高得分) #
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.Score_scale * self.alien_points)
