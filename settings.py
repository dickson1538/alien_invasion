class Settings:
    def __init__(self):
        # screen settings
        self.screen_width = 1100  # 1280
        self.screen_height = 600  # 700
        self.bg_color = (230, 230, 230)

        self.ship_speed = 1.5
        self.ship_limit = 3

        self.alien_speed = 1
        self.fleet_drop_speed = 10  # how quickly the fleet drops down
        self.fleet_direction = 1   # 1 means right -1 means left

        self.bullet_speed = 1
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 9
