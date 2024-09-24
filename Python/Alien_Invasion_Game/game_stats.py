class GameStats:
    def __init__(self,ai_game):
        self.settings = ai_game.settings
        self.high_score = 0
        self.reset_stats()
    
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit    # 重置飞船数 #
        self.score = 0    # 重置游戏得分 #
        self.level = 1    # 重置等级 #
        
