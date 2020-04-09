from .BulletInterface import BulletInterface
from .Mob import Mob

class BulletMob(BulletInterface):
    def __init__(self, bullet_type, mob: Mob):
        BulletInterface.__init__(self, bullet_type)
        self.position = mob.getPosition
