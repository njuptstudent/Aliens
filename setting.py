class Setting():
    def __init__(self):
        # 初始化静态设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        
        # 飞船设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        
        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右；为-1表示向左
        self.fleet_direction = 1
        
        # 游戏难度提升速度
        self.speedup_scale = 1.1
        
        # 初始化动态设置
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        
        # fleet_direction为1表示向右；为-1表示向左
        self.fleet_direction = 1
    
    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale