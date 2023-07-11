class State:
    def __init__(self):
        self.motion_inside = 0
        self.motion_outside = 0
        self.force = 0

    def is_security_alert(self):
        return (not self.motion_inside) and self.motion_outside and self.force > 50
