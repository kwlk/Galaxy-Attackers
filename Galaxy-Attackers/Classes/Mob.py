class Mob:
    def __init__(self, mob_cluster, hp, position, bullet_type, hit_box_size):
        self.position = position
        self.mob_cluster = mob_cluster
        self.hp = hp
        self.bullet_type = bullet_type
        self.hit_box_size = hit_box_size

    def get_position(self):
        return self.position

    def get_mob_cluster(self):
        return self.mob_cluster

    def die(self):
        self.mob_cluster.kill_mob(self)

    def check_for_collision(self, bullet):
        distance = self.position.distance(bullet.position)
        if distance < self.hit_box_size or distance < bullet.hit_box_size:
            self.hp -= bullet.dmg
            if self.hp < 1:
                self.die()
