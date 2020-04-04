import BulletInterface
import Player

class BulletPlayer(BulletInterface):
    def __init__(self, bullet_type, player: Player):
        BulletInterface.__init__(self, bullet_type)
        self.position = player.getPosition
