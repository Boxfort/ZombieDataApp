class Attack(object):
    def __init__(self):
        self.is_ranged = False
        self.damage = 0
        self.chance = 0
        self.effects = []
        self.attack_type = ""
        self.projectile_slug = ""