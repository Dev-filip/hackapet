import time
from player import Player
from platform import Platform
from bonus import Bonus
from hazard import Hazard
from utils import check_collision
import displayio
import blinka_displayio_pygamedisplay

class Game:
    def __init__(self):
        self.display = blinka_displayio_pygamedisplay.PygameDisplay(width=320, height=240)
        self.player = Player()
        self.platforms = [Platform(160, 220, 'standard')]
        self.bonuses = []
        self.hazards = []
        self.score = 0

    def run(self):
        while True:
            self.update()
            self.render()
            time.sleep(0.016)  # 60 FPS

    def update(self):
        self.player.update()
        for platform in self.platforms:
            platform.update()
        for bonus in self.bonuses:
            bonus.update()
        for hazard in self.hazards:
            hazard.update()

        # Collision detection
        for platform in self.platforms:
            if check_collision(self.player, platform):
                # Handle collision
                pass
        for bonus in self.bonuses:
            if check_collision(self.player, bonus):
                # Handle collision
                pass
        for hazard in self.hazards:
            if check_collision(self.player, hazard):
                # Handle collision
                pass

    def render(self):
        self.display.show(None)  # Clear the display
        self.player.draw(self.display)
        for platform in self.platforms:
            platform.draw(self.display)
        for bonus in self.bonuses:
            bonus.draw(self.display)
        for hazard in self.hazards:
            hazard.draw(self.display)