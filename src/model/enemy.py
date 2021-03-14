class Enemy(object):
    def __init__(self):
        self.name = ""
        self.sprite_slug = ""
        self.max_health = 0
        self.attack = 0
        self.defence = 0
        self.melee_accuracy = 0
        self.ranged_accuracy = 0
        self.speed = 0
        self.spawn_rate = 0
        self.tags = []