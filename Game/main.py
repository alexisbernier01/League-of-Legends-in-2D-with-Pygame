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
    def __init__(self, position=(36, 476), health=500, respawn=False, speed=1):
        super().__init__()
        self.player_jpg = pg.image.load("Assets/player.png").convert_alpha()
        self.player_rect = self.player_jpg.get_rect(center=(position))
        self.position = position
        self.health = health
        self.respawn = respawn
        self.speed = speed
    def move(self, initial_position, new_position):
        #self.position = new_position
        #self.player_rect.center = new_position
        x_final, y_final = new_position
        x_initial, y_initial = initial_position
        location_over_time = []

        while ((x_final - x_initial) > 0) & ((y_final - y_initial) > 0):
           # location_over_time.append(x_initial)
            
            





        






player = Player()

while True:
    # Process player inputs.
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_position = pg.mouse.get_pos()
            player.move(player.position, mouse_position)

    # Do logical updates here.
    # ...
    
   

    # Render the graphics here.
    # ...
    player.player_jpg = pg.transform.scale(player.player_jpg, (50, 50))
    player.player_rect = player.player_jpg.get_rect(center=player.position)
    screen.blit(player.player_jpg, player.player_rect)
    pg.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)


    


