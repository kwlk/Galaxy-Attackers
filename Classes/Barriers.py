class Barriers:
    def __init__(self, barriers):
        self.barriers = barriers

    def get_position(self):
        return self.position

    def get_hp(self):
        return self.hp

    def die(self):
        self.barriers.kill_barrier(self)

    def check_for_collision(self, bullet):
        distance = self.position.distance(bullet.position)
        if distance < self.hit_box_size or distance < bullet.hit_box_size:
            self.hp -= bullet.dmg
            if self.hp < 1:
                self.die()
