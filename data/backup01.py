import pygame as py
import os, sys, time

os.environ['SDL_VIDEO_CENTERED'] = '1'

#load images
load = py.image.load

stand = load('stand.png')
stage1_BG = load('stage_1.png')
start = load('start_button.png')
stage2_BG = load('main_lobby_1.png')
chair = load('chair.png')


def walls_stage_1():
    pos = (127, 168, 1, 365), (127, 125, 520, 1),(490, 150, 200, 1),(127,532,550,1),(675,250,1,280), (646,169,1,80),(646,248,50,1)
    for i in range(len(pos)):
        wall = py.Rect(pos[i])
        py.draw.rect(screen, (124,252,0), (wall))

        collision_tolerance = 10
        if player.colliderect(wall):
            if abs(wall.top - player.bottom) < collision_tolerance:
                player.y -= 5
            if abs(wall.bottom - player.top) < collision_tolerance:
                player.y += 5
            if abs(wall.right - player.left) < collision_tolerance:
                player.x += 5
            if abs(wall.left - player.right) < collision_tolerance:
                player.x -= 5
                
def walls_stage_2():
    pos = (528,63,1,175),(528,63,250,1),(528,235,160,1),(690,234,1,50),(604,290,85,1),(604,290,1,105),(436,395,170,1),(436,400,1,100)
    for i in range(len(pos)):
        wall = py.Rect(pos[i])
        py.draw.rect(screen, (124,252,0), (wall))

        collision_tolerance = 10
        if player.colliderect(wall):
            if abs(wall.top - player.bottom) < collision_tolerance:
                player.y -= 5
            if abs(wall.bottom - player.top) < collision_tolerance:
                player.y += 5
            if abs(wall.right - player.left) < collision_tolerance:
                player.x += 5
            if abs(wall.left - player.right) < collision_tolerance:
                player.x -= 5
        
    
def collision_rect():
    # collision with screen borders
    if player.right >= screen_width:
        player.x -= 5
    if player.bottom >= screen_height:
        player.y -= 5
    if player.left <= 0:
        player.x += 5
    if player.top <= 0:
        player.y += 5
    
    #py.draw.rect(screen, (255,0,0),player, 1) #rect visible edge
    py.draw.rect(screen, py.SRCALPHA,player, 1) #rect invisible
       
    
class GameStages():
    def __init__(self):
        self.stage = 'intro'

    def stage_manager(self):
        if self.stage == 'intro':
            self.intro()
        if self.stage == 'stage_1':
            self.stage_1()
        if self.stage == 'stage_2':
            self.stage_2()
    
    def intro(self):
        if event.type == py.MOUSEBUTTONDOWN:
            self.stage = 'stage_1'
        screen.blit(start ,(120, 100))
        py.display.update()
        
    def stage_2(self):
        keys = py.key.get_pressed()
        if event.type == py.KEYDOWN:
            if keys[py.K_w]:
                player.y -= vel
            if keys[py.K_s]:
                player.y += vel
            if keys[py.K_a]:
                player.x -= vel
            if keys[py.K_d]:
                player.x += vel

        if event.type == py.KEYUP:
            if keys[py.K_w]:
                player.y -= vel
            if keys[py.K_s]:
                player.y += vel
            if keys[py.K_a]:
                player.x -= vel
            if keys[py.K_d]:
                player.x += vel
                
                    
        screen.fill((0, 0, 0))
        screen.blit(stage2_BG,(0, 0))
        screen.blit(stand, (player.x, player.y))
        walls_stage_2()
        collision_rect()
        py.display.update()
    
    def stage_1(self):
        event_chair = False
        
        keys = py.key.get_pressed()
        
        if player.colliderect(chairP):
            event_chair = True
            
        if event.type == py.KEYDOWN:
            if keys[py.K_w]:
                player.y -= vel
            elif keys[py.K_s]:
                player.y += vel
            elif keys[py.K_a]:
                player.x -= vel
                right = False
                left = True
            elif keys[py.K_d]:
                player.x += vel
                right = True
                left = False
            elif keys[py.K_f] and event_chair:
                print('next level')
                self.stage = 'stage_2'
            else:
                right = False
                left = False
                walkCount = 0

        if event.type == py.KEYUP:
            if keys[py.K_w]:
                player.y -= vel
            elif keys[py.K_s]:
                player.y += vel
            elif keys[py.K_a]:
                player.x -= vel
                right = False
                left = True
            elif keys[py.K_d]:
                player.x += vel
                right = True
                left = False
            else:
                right = False
                left = False
                walkCount = 0
                
            
        screen.blit(stage1_BG, (0, 0))
        screen.blit(stand, (player.x, player.y))
        screen.blit(chair,(550, 193))
        py.draw.rect(screen, py.SRCALPHA,chairP, 1)
        walls_stage_1()
        collision_rect()

        #Arrumar problema da animação do player!
        

        
py.init()
clock = py.time.Clock()
screen_width, screen_height = 800, 700
screen = py.display.set_mode((screen_width, screen_height))

#general setup
game_stage = GameStages()
chairP = py.Rect(568, 193, 30, 30)
vel = 5
player = py.Rect(207, 129, 40, 64)
health_player = 5


while True:
    clock.tick(27)
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

    if event.type == py.MOUSEBUTTONDOWN:
        Mouse_x, Mouse_y = py.mouse.get_pos()
        print('X:',Mouse_x,'| y:',Mouse_y)
        
    start_time = time.time()     
    game_stage.stage_manager()
    py.display.update()
