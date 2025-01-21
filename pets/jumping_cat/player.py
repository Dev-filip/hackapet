class Player:
    def __init__(self):
        self.x = 160
        self.y = 200
        self.vx = 0
        self.vy = 0
        self.width = 20
        self.height = 20

    def update(self):
        self.y += self.vy
        self.x += self.vx

    def draw(self, display):
        # Draw the player
        pass