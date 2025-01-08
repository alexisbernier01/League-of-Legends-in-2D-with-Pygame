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
    def __init__(self, position=(36, 476), health=500, respawn=False, speed=0.3, attack=20):
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
    def __init__(self, position=(96, 406), isEnemy=True, target_vector=(256, 256), attack=10, speed=0.3, health=100):
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

         # Set velocity to move toward the center
        self.target = pg.Vector2(target_vector)
        self.velocity = (self.target - self.position).normalize() * speed

    

    def update(self):

         # Move the minion toward the target
        self.position += self.velocity
        self.rect.center = (int(self.position.x), int(self.position.y))

        if self.health <= 0:
            self.kill()  # Removes the sprite from all groups



        


player = Player()
#minion = Minion()

friendly_minions = pg.sprite.Group()
enemy_minions = pg.sprite.Group()
spawn_timer = 0



while True:
    # Process player inputs.
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_position = pg.mouse.get_pos()
            player.set_target(mouse_position)

    # Get current time in milliseconds
    current_time = pg.time.get_ticks()
    current_time += 30000

    # Spawn minion groups every 30 seconds (30,000 ms)
    if current_time - spawn_timer > 30000:
        
        spawn_timer = current_time

        for i in range(3):  
            offset = i * 15  # Offset for each minion in the group
            minion = Minion(isEnemy=False, position=(96 + offset, 406 + offset))
            friendly_minions.add(minion)
        for i in range(3):  
            offset = i * 15  # Offset for each minion in the group
            minion = Minion(isEnemy=False, position=(409 + offset, 103 + offset))
            enemy_minions.add(minion)


    # Do logical updates here.
    # ...
    player.update()
    friendly_minions.update()
    enemy_minions.update()
    
   

    # Render the graphics here.
    # ...
    screen.blit(SR_jpg, (0, 0))
    player.player_jpg = pg.transform.scale(player.player_jpg, (50, 50))
    player.player_rect = player.player_jpg.get_rect(center=player.position)
    screen.blit(player.player_jpg, player.player_rect)
    for minion in friendly_minions:
        screen.blit(minion.image, minion.rect) 

    for minion in enemy_minions:
        screen.blit(minion.image, minion.rect) 

    pg.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)


    


