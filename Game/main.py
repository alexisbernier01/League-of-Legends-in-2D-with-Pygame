import pygame as pg 

pg.init()

screen = pg.display.set_mode((512,512))

clock = pg.time.Clock()

# load SR
SR_jpg = pg.image.load("Assets/summoners_rift.jpg").convert()
screen.blit(SR_jpg, (0,0))

class Player(pg.sprite.Sprite):
    '''
    Player and controllable charecter.
    Returns: Player object
    Functions: move, attack, respawn, update
    Attributes: position, health, respawn
    '''
    def __init__(self, position=(36, 476), health=500, respawn=False, speed=0.5, attack=20):
        super().__init__()
        self.player_jpg = pg.image.load("Assets/player.png").convert_alpha()
        self.player_rect = self.player_jpg.get_rect(center=(position))
        self.position = position
        self.health = health
        self.respawn = respawn
        self.speed = speed
        self.target_position = 0
    def set_target(self, new_position):
       '''
        Sets the target position for the player.
        
        '''
       self.target_position = pg.Vector2(new_position)
       print(self.target_position)
       
    def update(self):
        '''
        Moves the player toward the target position if one is set.

        '''
        if self.target_position == 0:
            return
        
        if self.target_position:

            direction = self.target_position - self.position

            if direction.length() <= self.speed:
                self.position = self.target_position
                self.target_position = None

            else:
                self.position += direction.normalize() * self.speed

            self.player_rect.center = (int(self.position.x), int(self.position.y))

    def attack():
        pass

class Minion(pg.sprite.Sprite):
    def __init__(self, isEnemy=True, attack=10, speed=0.5, health=100, position=(96, 406)):
        super().__init__()
        self.attack = attack
        self.speed = speed
        self.health = health
        self.position = position
        self.isEnemy = isEnemy

        # draw square representing a minion
        self.size = 10
        self.image = pg.Surface((self.size, self.size)) 
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=position)

    def update():
        pass


player = Player()
minion = Minion()

while True:
    # Process player inputs.
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_position = pg.mouse.get_pos()
            player.set_target(mouse_position)

    # Do logical updates here.
    # ...
    player.update()
    
   

    # Render the graphics here.
    # ...
    screen.blit(SR_jpg, (0, 0))
    player.player_jpg = pg.transform.scale(player.player_jpg, (50, 50))
    player.player_rect = player.player_jpg.get_rect(center=player.position)
    screen.blit(player.player_jpg, player.player_rect)
    screen.blit(minion.image, minion.rect)
    pg.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)


    


