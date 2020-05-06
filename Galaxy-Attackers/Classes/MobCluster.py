class MobCluster:
    def __init__(self, bottom_left, upper_right, mobs, speed, speed_rise, speed_rise_rise):
        self.bottom_left = bottom_left
        self.bottom_right = upper_right
        self.mobs = mobs
        self.speed = speed
        self.speed_rise = speed_rise
        self.speed_rise_rise = speed_rise_rise

    def get_bottom_left(self):
        return self.bottom_left

    def get_upper_right(self):
        return self.bottom_right

    def get_mobs(self):
        return self.mobs

    def check_gameover(self, limit):
        if self.bottom_left.y < limit:
            return True
        return False

    def check_for_win(self):
        if len(self.mobs) < 1:
            return True
        return False

    def kill_mob(self, mob):
        self.mobs.remove(mob)
        self.speed += self.speed_rise
        self.speed_rise += self.speed_rise_rise

