import pygame

'''
Entity information:

Contains entities analogous to league of legends which include
-Nexus
-Turret
-Minions
-Controlable champion (aka 'player')

'''

class Player:
    def __init__(self, hitpoints=200, img='Assets/player.png', position=(60, 650), attack_damage=20, move_speed=2):
        self.hitpoints = hitpoints
        self.position = position
        self.attack_damage = attack_damage
        self.move_speed = move_speed

        # resize image
        original_img = pygame.image.load(img).convert_alpha()
        self.img = pygame.transform.scale(original_img, (50, 50))

        # convert to Rect object
        self.img_rect = self.img.get_rect(center=position)
        

    # def attack():
    # def move():
    # def killed():

class Minion:
    def __init__(self, hitpoints=100, position=(0, 0), attack_damage=10, move_speed=1):
        self.hitpoints = hitpoints
        self.position = position
        self.attack_damage = attack_damage
        self.move_speed = move_speed
    
    # def attack()
    # def killed()

class Turret:
    def __init__(self, hitpoints=500, img='Assets/turret.png', position=(0, 0), attack_damage=40, entity_in_range=False):
        self.hitpoints = hitpoints
        self.img = pygame.image.load(img).convert_alpha()
        self.position = position
        self.attack_damage = attack_damage
        self.entity_in_range = entity_in_range

    # def attack
    # def destroyed

class Nexus:
    def __init__(self, hitpoints=400, img='Assets/nexus.png', position=(0, 0)):
        self.hitpoints = hitpoints
        self.img = pygame.image.load(img).convert_alpha()
        self.position = position

    # def destroyed
    
