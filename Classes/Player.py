
class Player:
    def __init__(self, map, speed_vector, max_hp, damage, position, bullet_type = 0):
        self.map = map
        self.speed_vector = speed_vector
        self.damage = damage
        self.hp = max_hp
        self.bullet_type = bullet_type
        self.position = position

    def shoot(self):
        return self.bullet_type


    def take_damage(self, damage):
        self.hp -= damage

    def getPosition(self):
        return self.getPosition
