class BulletInterface:
    def __init__(self, bullet_type):
        self.bullet_type = bullet_type
        BulletInterface.recogniseBulletType(self, bullet_type)
        pass

    def recogniseBulletType(self, bullet_type):
        if bullet_type == 0:
            self.speed = 1
            self.damage = 1

    def get_damage(self):
        return self.damage

    def get_speed(self):
        return self.speed

    def collide(self, object):
        object.take_damage(self.damage)
        self.delete

    def delete(self):
        ##gotta delete
        self.speed = 0

