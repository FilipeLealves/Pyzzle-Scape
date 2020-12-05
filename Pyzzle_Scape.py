import pygame as py
from pygame import mixer, time, freetype
import os, sys, time, random

py.mixer.init()
py.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

#----------Sounds----------#
if getattr(sys, 'frozen', False):
    wd = sys._MEIPASS
else:
    wd = ''

#image = loadImage(os.path.join(wd,'folder',"file_name.jpg"))

pop = py.mixer.Sound(os.path.join(wd,'data','pop.wav'))
spark = py.mixer.Sound(os.path.join(wd,'data','power_spark.wav'))
sucked = py.mixer.Sound(os.path.join(wd,'data','getting-sucked.ogg'))
typing = py.mixer.Sound(os.path.join(wd,'data','keyboard-typing.ogg'))
click = py.mixer.Sound(os.path.join(wd,'data','click.ogg'))
mouse = py.mixer.Sound(os.path.join(wd,'data','motion_mouse.ogg'))
appear = py.mixer.Sound(os.path.join(wd,'data','appear.ogg'))
chest = py.mixer.Sound(os.path.join(wd,'data','chest.ogg'))
death_player = py.mixer.Sound(os.path.join(wd,'data','hurt.ogg'))
handle = py.mixer.Sound(os.path.join(wd,'data','handle.ogg'))
ring = py.mixer.Sound(os.path.join(wd,'data','phone-ringing.ogg'))
request = py.mixer.Sound(os.path.join(wd,'data','request.ogg'))
argue = py.mixer.Sound(os.path.join(wd,'data','argue.ogg'))
click_switch = py.mixer.Sound(os.path.join(wd,'data','click_switch.ogg'))
dial = py.mixer.Sound(os.path.join(wd,'data','dial.ogg'))

py.mixer.music.load(os.path.join(wd,'data','stage_2.ogg'))
py.mixer.music.set_volume(0.4)
py.mixer.music.play(-1)

#-------Load Images--------#
load = py.image.load

walkRight = [load(os.path.join(wd,'data','R1.png')),load(os.path.join(wd,'data','R2.png')),load(os.path.join(wd,'data','R3.png')),load(os.path.join(wd,'data','R4.png')),load(os.path.join(wd,'data','R5.png')),load(os.path.join(wd,'data','R6.png')),load(os.path.join(wd,'data','R7.png')),load(os.path.join(wd,'data','R8.png')),load(os.path.join(wd,'data','R9.png'))]
walkLeft = [load(os.path.join(wd,'data','L1.png')),load(os.path.join(wd,'data','L2.png')),load(os.path.join(wd,'data','L3.png')),load(os.path.join(wd,'data','L4.png')),load(os.path.join(wd,'data','L5.png')),load(os.path.join(wd,'data','L6.png')),load(os.path.join(wd,'data','L7.png')),load(os.path.join(wd,'data','L8.png')),load(os.path.join(wd,'data','L9.png'))]
walkUp = [load(os.path.join(wd,'data','U1.png')),load(os.path.join(wd,'data','U2.png')),load(os.path.join(wd,'data','U3.png')),load(os.path.join(wd,'data','U4.png')),load(os.path.join(wd,'data','U5.png')),load(os.path.join(wd,'data','U6.png')),load(os.path.join(wd,'data','U7.png')),load(os.path.join(wd,'data','U8.png')),load(os.path.join(wd,'data','U9.png'))]
walkDown = [load(os.path.join(wd,'data','D1.png')),load(os.path.join(wd,'data','D2.png')),load(os.path.join(wd,'data','D3.png')),load(os.path.join(wd,'data','D1.png')),load(os.path.join(wd,'data','D2.png')),load(os.path.join(wd,'data','D3.png')),load(os.path.join(wd,'data','D1.png')),load(os.path.join(wd,'data','D2.png')),load(os.path.join(wd,'data','D3.png'))]
Stand = [load(os.path.join(wd,'data','S1.png')),load(os.path.join(wd,'data','S2.png')),load(os.path.join(wd,'data','S3.png')),load(os.path.join(wd,'data','S4.png')),load(os.path.join(wd,'data','S5.png')),load(os.path.join(wd,'data','S6.png')),load(os.path.join(wd,'data','S6.png')),load(os.path.join(wd,'data','S7.png')),load(os.path.join(wd,'data','S7.png'))]
fullBlack = [load(os.path.join(wd,'data','full_black-0.png')),load(os.path.join(wd,'data','full_black-1.png')),load(os.path.join(wd,'data','full_black-2.png')),load(os.path.join(wd,'data','full_black-3.png')),load(os.path.join(wd,'data','full_black-4.png')),load(os.path.join(wd,'data','full_black-5.png')),load(os.path.join(wd,'data','full_black-6.png')),load(os.path.join(wd,'data','full_black-7.png')),load(os.path.join(wd,'data','full_black-8.png'))]
sugado = [load(os.path.join(wd,'data','sugado1.png')),load(os.path.join(wd,'data','sugado2.png')),load(os.path.join(wd,'data','sugado3.png')),load(os.path.join(wd,'data','sugado4.png')),load(os.path.join(wd,'data','sugado5.png')),load(os.path.join(wd,'data','sugado6.png')),load(os.path.join(wd,'data','sugado7.png')),load(os.path.join(wd,'data','sugado8.png')),load(os.path.join(wd,'data','sugado9.png')),load(os.path.join(wd,'data','sugado10.png'))]
player_back = load(os.path.join(wd,'data','U1.png'))
stage_1_on = load(os.path.join(wd,'data','stage_1_on.png'))
stage_1_off = load(os.path.join(wd,'data','stage_1_off.png'))
stage_2 = load(os.path.join(wd,'data','stage_2.png'))
stage_google = load(os.path.join(wd,'data','stage_2_1.png'))
stage_baidu = load(os.path.join(wd,'data','baidu_BG.png'))
stage_lol = load(os.path.join(wd,'data','lol_BG-1-1.png'))
stage_pygame = load(os.path.join(wd,'data','pycharm_bg-1.png'))
stand = load(os.path.join(wd,'data','stand.png'))
start = load(os.path.join(wd,'data','start-2.png'))
stage2_BG = load(os.path.join(wd,'data','main_lobby_1.png'))
chair = load(os.path.join(wd,'data','chair.png'))
jogar_img = load(os.path.join(wd,'data','jogar.png'))
comandos_img = load(os.path.join(wd,'data','comandos_img.png'))
comandos_start = load(os.path.join(wd,'data','comandos.png'))
sair_img = load(os.path.join(wd,'data','sair_img.png'))
voltar_img = load(os.path.join(wd,'data','voltar.png'))
eraser_blue = load(os.path.join(wd,'data','blue.png'))
hide_up = load(os.path.join(wd,'data','hide_up.png'))
door_img = load(os.path.join(wd,'data','door1.png'))
google_dirty = load(os.path.join(wd,'data','google_dirty.png'))
baidu_dirty = load(os.path.join(wd,'data','baidu_dirty.png'))
lol_dirty = load(os.path.join(wd,'data','lol_dirty.png'))
py_dirty = load(os.path.join(wd,'data','py_dirty.png'))
heart_1 = load(os.path.join(wd,'data','heart-1.png'))
heart_2 = load(os.path.join(wd,'data','heart-2.png'))
heart_3 = load(os.path.join(wd,'data','heart-3.png'))
heart_4 = load(os.path.join(wd,'data','heart-4.png'))
set_icon = load(os.path.join(wd,'data','set_icon.png'))
set_boss_talk = load(os.path.join(wd,'data','screen_boss.png'))
set_self_talk = load(os.path.join(wd,'data','screen_self.png'))
#------------Times---------------#
current_time = py.time.get_ticks()

game_font = py.freetype.Font('data/game_font.ttf', 13)
game_font_16 = py.freetype.Font('data/game_font.ttf', 16)
game_font_18 = py.freetype.Font('data/game_font.ttf', 18)
game_font_20 = py.freetype.Font('data/game_font.ttf', 20)
py.display.set_icon(set_icon)
py.display.set_caption('Pyzzle Scape')

time_a1 = 0

def walls_stage_1():
    pos = (127, 168, 1, 365), (127, 125, 520, 1),(490, 150, 200, 1),(127,532,550,1),(675,250,1,280), (646,169,1,80),(646,248,50,1),(116,436,44,80)
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
    pos = (514,9,1,175),(528,44,250,1),(528,200,150,1),(516,240,160,1),(516,290,1,160),(447,447,66,1),(443,448,1,65),(720,425,100,1),(720,425,1,100),(562,545,1,100),(562,545,200,1),(388,500,55,1),(388,446,1,50),(388,446,70,1),(461,100,1,345),(461,100,50,1),(235,128,1,600),(235,128,130,1),(365,133,1,40),(290,174,1,500),(290,174,60,1),(135,50,1,430),(150,3,1,30),(80,484,40,1),(80,4,1,450),(1,644,1000,1)
                                                                                                                     #----------------------Inferior direito-------------------------#                                                                           #----------------------------Second Part-------------------------------------#                                                        #--Floor--#
    for i in range(len(pos)):
        wall = py.Rect(pos[i])
        py.draw.rect(screen, (124,252,0), (wall))

        collision_tolerance = 10
        if player_1.colliderect(wall):
            if abs(wall.top - player_1.bottom) < collision_tolerance:
                player_1.y -= 5
            if abs(wall.bottom - player_1.top) < collision_tolerance:
                player_1.y += 5
            if abs(wall.right - player_1.left) < collision_tolerance:
                player_1.x += 5
            if abs(wall.left - player_1.right) < collision_tolerance:
                player_1.x -= 5

def walls_stage_3():
    pos = (0,680,1000,1),(469,575,1000,1),(80,498,260,1),(411,382,300,1),(0,250,355,1),(430,143,150,1),(633,103,400,1)                                                                
    for i in range(len(pos)):
        wall = py.Rect(pos[i])
        py.draw.rect(screen, (124,252,0), (wall))

        collision_tolerance = 15
        if player_lv1.colliderect(wall):
            if abs(wall.top - player_lv1.bottom) < collision_tolerance:
                player_lv1.y -= 11
            if abs(wall.bottom - player_lv1.top) < collision_tolerance:
                player_lv1.y += 11
            if abs(wall.right - player_lv1.left) < collision_tolerance:
                player_lv1.x += 11
            if abs(wall.left - player_lv1.right) < collision_tolerance:
                player_lv1.x -= 11

def walls_stage_4():
    pos = (0,677,800,1),(303,557,280,1),(620,461,500,1),(0,231,195,1),(239,121,370,1),(715,121,300,1)                                                  
    for i in range(len(pos)):
        wall = py.Rect(pos[i])
        py.draw.rect(screen, (124,252,0), (wall))

        collision_tolerance = 15
        if player_lv1.colliderect(wall):
            if abs(wall.top - player_lv1.bottom) < collision_tolerance:
                player_lv1.y -= 11
            if abs(wall.bottom - player_lv1.top) < collision_tolerance:
                player_lv1.y += 11
            if abs(wall.right - player_lv1.left) < collision_tolerance:
                player_lv1.x += 11
            if abs(wall.left - player_lv1.right) < collision_tolerance:
                player_lv1.x -= 11
            
def walls_stage_5():
    pos = (0,650,800,1),(0,475,636,1),(636,323,1,185),(636,323,47,1),(683,280,1,43),(636,280,47,1),(636,107,1,173),(532,107,94,1),(532,107,1,50),(472,166,60,1),(472,112,1,55),(384,107,88,1),(384,107,1,55),(320,166,60,1),(322,107,1,60),(232,107,85,1),(232,107,1,30),(233,137,85,1),(384,137,85,1),(532,137,65,1),(597,137,1,302),(0,439,597,1),(160,289,363,1),(129,271,391,1),(410,271,1,165),(458,271,1,165),(131,0,1,108),(66,108,80,1),(65,135,102,1),(168,0,1,135),(0,570,40,1)                          
    for i in range(len(pos)):
        wall = py.Rect(pos[i])
        py.draw.rect(screen, (124,252,0), (wall))

        collision_tolerance = 15
        if player_lv1.colliderect(wall):
            if abs(wall.top - player_lv1.bottom) < collision_tolerance:
                player_lv1.y -= 11
            if abs(wall.bottom - player_lv1.top) < collision_tolerance:
                player_lv1.y += 11
            if abs(wall.right - player_lv1.left) < collision_tolerance:
                player_lv1.x += 11
            if abs(wall.left - player_lv1.right) < collision_tolerance:
                player_lv1.x -= 11

def walls_stage_6():
    pos = (53,215,40,1),(53,215,1,115),(163,215,700,1),(93,100,1,90),(165,100,1,90),(30,333,1,123),(10,457,1,150),(755,215,1,180),(777,390,1,150)
                                                                                                                     #----------------------Inferior direito-------------------------#                                                                           #----------------------------Second Part-------------------------------------#                                                        #--Floor--#
    for i in range(len(pos)):
        wall = py.Rect(pos[i])
        py.draw.rect(screen, (124,252,0), (wall))

        collision_tolerance = 10
        if player_1.colliderect(wall):
            if abs(wall.top - player_1.bottom) < collision_tolerance:
                player_1.y -= 8
            if abs(wall.bottom - player_1.top) < collision_tolerance:
                player_1.y += 8
            if abs(wall.right - player_1.left) < collision_tolerance:
                player_1.x += 8
            if abs(wall.left - player_1.right) < collision_tolerance:
                player_1.x -= 8
    
def collision_rect_st1():
    # collision with screen borders
    if player.right >= screen_width:
        player.x -= 5
    if player.bottom >= screen_height:
        player.y -= 5
    if player.left <= 0:
        player.x += 5
    if player.top <= 0:
        player.y += 5
def collision_rect_st2():
    # collision with screen borders
    if player_1.right >= screen_width:
        player_1.x -= 5
    if player_1.bottom >= screen_height:
        player_1.y -= 5
    if player_1.left <= 0:
        player_1.x += 5
    if player_1.top <= 0:
        player_1.y += 5
def collision_rect_st3():
    # collision with screen borders
    if player_1.right >= screen_width:
        player_1.x -= 8
    if player_1.bottom >= screen_height:
        player_1.y -= 8
    if player_1.left <= 0:
        player_1.x += 8
    if player_1.top <= 0:
        player_1.y += 8
def collision_rect_lv1():
    # collision with screen borders
    if player_lv1.right >= screen_width:
        player_lv1.x -= 11
    if player_lv1.bottom >= screen_height:
        player_lv1.y -= 11
    if player_lv1.left <= 0:
        player_lv1.x += 11
    if player_lv1.top <= 0:
        player_lv1.y += 11
    
    #py.draw.rect(screen, (255,0,0),player, 1) #rect visible edge
    py.draw.rect(screen, py.SRCALPHA,player, 1) #rect invisible
 
class enemy(object):
    enemy_r = load(os.path.join(wd,'data','enemy_c.png'))
    enemy_l = py.transform.flip(enemy_r, True, False)
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.vel = 3.5

    def draw(self, screen):
        self.move()
        #py.draw.rect(screen, (255,0,0), dino_rect, 2)

    def move(self):
        if self.vel > 0:
            if dino_rect.x < self.path[1] + self.vel:
                dino_rect.x += self.vel
                screen.blit(self.enemy_r, (dino_rect.x - 5, dino_rect.y - 10))
            else:
                self.vel = self.vel * -1
                dino_rect.x += self.vel
        else:
            if dino_rect.x > self.path[0] - self.vel:
                dino_rect.x += self.vel
                screen.blit(self.enemy_l, (dino_rect.x - 5, dino_rect.y - 10))
            else:
                self.vel = self.vel * -1
                dino_rect.x += self.vel  

class enemy2(object):
    enemy_r = load(os.path.join(wd,'data','enemy_c.png'))
    enemy_l = py.transform.flip(enemy_r, True, False)
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.vel = 3.2

    def draw(self, screen):
        self.move()
        
        #py.draw.rect(screen, (255,0,0), dino_rect_2, 2)

    def move(self):
        if self.vel > 0:
            if dino_rect_2.x < self.path[1] + self.vel:
                dino_rect_2.x += self.vel
                screen.blit(self.enemy_r, (dino_rect_2.x - 5, dino_rect_2.y - 10))
            else:
                self.vel = self.vel * -1
                dino_rect_2.x += self.vel
        else:
            if dino_rect_2.x > self.path[0] - self.vel:
                dino_rect_2.x += self.vel
                screen.blit(self.enemy_l, (dino_rect_2.x - 5, dino_rect_2.y - 10))
            else:
                self.vel = self.vel * -1
                dino_rect_2.x += self.vel 

class enemy3(object):
    enemy_r = load(os.path.join(wd,'data','enemy_c.png'))
    enemy_l = py.transform.flip(enemy_r, True, False)
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.vel = 3.8

    def draw(self, screen):
        self.move()
        #py.draw.rect(screen, (255,0,0), dino_rect_3, 2)

    def move(self):
        if self.vel > 0:
            if dino_rect_3.x < self.path[1] + self.vel:
                dino_rect_3.x += self.vel
                screen.blit(self.enemy_r, (dino_rect_3.x - 5, dino_rect_3.y - 10))
            else:
                self.vel = self.vel * -1
                dino_rect_3.x += self.vel
        else:
            if dino_rect_3.x > self.path[0] - self.vel:
                dino_rect_3.x += self.vel
                screen.blit(self.enemy_l, (dino_rect_3.x - 5, dino_rect_3.y - 10))
            else:
                self.vel = self.vel * -1
                dino_rect_3.x += self.vel

class enemy4(object):
    enemy_r = load(os.path.join(wd,'data','enemy_c.png'))
    enemy_l = py.transform.flip(enemy_r, True, False)

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.vel = 4
        

    def draw(self, screen):
        self.move()
        #py.draw.rect(screen, (255,0,0), dino_rect_4, 2)

    def move(self):
        if self.vel > 0:
            if dino_rect_4.x < self.path[1] + self.vel:
                dino_rect_4.x += self.vel
                screen.blit(self.enemy_r, (dino_rect_4.x - 5, dino_rect_4.y - 10))
            else:
                self.vel = self.vel * -1
                dino_rect_4.x += self.vel
                
        else:
            if dino_rect_4.x > self.path[0] - self.vel:
                dino_rect_4.x += self.vel
                screen.blit(self.enemy_l, (dino_rect_4.x - 5, dino_rect_4.y - 10))

            else:
                self.vel = self.vel * -1
                dino_rect_4.x += self.vel
                
class virus1(object):
    virus_img_right = load(os.path.join(wd,'data','virus_3.png'))
    virus_img_left = py.transform.flip(virus_img_right, True, False)
    def __init__(self, x, end):
        self.x = x
        self.path = [x, end]
        self.vel = 5

    def draw(self, screen):
        self.move()
        #py.draw.rect(screen, (255,0,0), virus_1, 2)

    def move(self):
        if self.vel > 0:
            if virus_1.x < self.path[1] + self.vel:
                virus_1.x += self.vel
                screen.blit(self.virus_img_left, (virus_1.x, virus_1.y - 15))
            else:
                self.vel = self.vel * -1
                virus_1.x += self.vel
                virus_1.y -= 110
                
        else:
            if virus_1.x > self.path[0] - self.vel: 
                virus_1.x += self.vel
                screen.blit(self.virus_img_right, (virus_1.x, virus_1.y - 15))
            else:
                self.vel = self.vel * -1
                virus_1.x += self.vel
                virus_1.y += 110

class virus2(object):
    virus_img_right = load(os.path.join(wd,'data','virus_4.png'))
    virus_img_left = py.transform.flip(virus_img_right, True, True)
    def __init__(self, x, y, end):
        self.x = x
        self.y = y
        self.path = [y, end]
        self.vel = 3

    def draw(self, screen):
        self.move()
        #py.draw.rect(screen, (255,0,0), virus_2, 2)

    def move(self):
        if self.vel > 0:
            if virus_2.y < self.path[1] + self.vel:
                virus_2.y += self.vel
                screen.blit(self.virus_img_left, (virus_2.x - 5, virus_2.y - 10))
            else:
                self.vel = self.vel * -1
                virus_2.y += self.vel
                
        else:
            if virus_2.y > self.path[0] - self.vel: 
                virus_2.y += self.vel
                screen.blit(self.virus_img_right, (virus_2.x - 5, virus_2.y - 10))
            else:
                self.vel = self.vel * -1
                virus_2.y += self.vel           

class virus3(object):
    virus_img_right = load(os.path.join(wd,'data','virus-1.png'))
    virus_img_left = py.transform.flip(virus_img_right, True, False)
    def __init__(self, x, y, end):
        self.x = x
        self.y = y
        self.path = [x, end]
        self.path_2 = [y, end]
        self.vel = 5

    def draw(self, screen):
        self.move()
        #py.draw.rect(screen, (255,0,0), virus_3, 2)

    def move(self):
        if self.vel > 0:
            if virus_3.x < self.path[1] + self.vel:
                virus_3.x += self.vel
                screen.blit(self.virus_img_right, (virus_3.x, virus_3.y))
            else:
                self.vel = self.vel * -1
                virus_3.x += self.vel
                
        else:
            if virus_3.y > self.path[0] - self.vel: 
                virus_3.y += self.vel
                screen.blit(self.virus_img_left, (virus_3.x, virus_3.y))
            else:
                self.vel = self.vel * -1
                virus_3.x, virus_3.y = 3 , 168

class virus4(object):
    virus_img_right = load(os.path.join(wd,'data','virus_2.png'))
    virus_img_left = py.transform.flip(virus_img_right, True, False)
    def __init__(self, x, end):
        self.x = x
        self.path = [x, end]
        self.vel = 8.5

    def draw(self, screen):
        self.move()
        #py.draw.rect(screen, (255,0,0), virus_4, 2)

    def move(self):
        if self.vel > 0:
            if virus_4.x < self.path[1] + self.vel:
                virus_4.x += self.vel
                screen.blit(self.virus_img_left, (virus_4.x, virus_4.y))
            else:
                self.vel = self.vel * -1
                virus_4.x += self.vel
                
        else:
            if virus_4.x > self.path[0] - self.vel: 
                virus_4.x += self.vel
                screen.blit(self.virus_img_right, (virus_4.x, virus_4.y))
            else:
                self.vel = self.vel * -1
                virus_4.x += self.vel

class plataformV2(object):
    platform = load(os.path.join(wd,'data','baidu_plataform.png'))
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.vel = 3

    def draw(self, screen):
        self.move()
        screen.blit(self.platform, (plataform_lv2.x, plataform_lv2.y - 20))
        #py.draw.rect(screen, (255,0,0), plataform_lv2, 2)

    def move(self):
        if self.vel > 0:
            if plataform_lv2.x < self.path[1] + self.vel:
                plataform_lv2.x += self.vel
            else:
                self.vel = self.vel * -1
                plataform_lv2.x += self.vel
        else:
            if plataform_lv2.x > self.path[0] - self.vel:
                plataform_lv2.x += self.vel
            else:
                self.vel = self.vel * -1
                plataform_lv2.x += self.vel
class plat1(object):
    plat_img = load(os.path.join(wd,'data','plataform-lol-4.png'))
    def __init__(self, y, end):
        self.y = y
        self.path = [y, end]
        self.vel = 3

    def draw(self, screen):
        self.move()
        #py.draw.rect(screen, (255,0,0), plat_1, 1)

    def move(self):
        if self.vel > 0:
            if plat_1.y < self.path[1] + self.vel:
                plat_1.y += self.vel
                screen.blit(self.plat_img, (plat_1.x, plat_1.y - 20))
            else:
                self.vel = self.vel * -1
                plat_1.y += self.vel

            if player_lv1.colliderect(plat_1):
                if abs(plat_1.top - player_lv1.bottom) < 15:
                    player_lv1.y -= 8
                
        else:
            if plat_1.y > self.path[0] - self.vel: 
                plat_1.y += self.vel
                screen.blit(self.plat_img, (plat_1.x, plat_1.y - 20))
            else:
                self.vel = self.vel * -1
                plat_1.y += self.vel

            if player_lv1.colliderect(plat_1):
                if abs(plat_1.top - player_lv1.bottom) < 15:
                    player_lv1.y -= 14
                if abs(plat_1.bottom - player_lv1.top) < 5:
                    player_lv1.y = 524

class plat2(object):
    plat_img = load(os.path.join(wd,'data','plataform-lol-4.png'))
    def __init__(self, y, end):
        self.y = y
        self.path = [y, end]
        self.vel = 3

    def draw(self, screen):
        self.move()
        #py.draw.rect(screen, (255,0,0), plat_2, 1)

    def move(self):
        if self.vel > 0:
            if plat_1.y < self.path[1] + self.vel:
                plat_2.y += self.vel
                screen.blit(self.plat_img, (plat_2.x, plat_2.y - 20))
            else:
                self.vel = self.vel * -1
                plat_2.y += self.vel

            if player_lv1.colliderect(plat_2):
                if abs(plat_2.top - player_lv1.bottom) < 15:
                    player_lv1.y -= 8
                
        else:
            if plat_2.y > self.path[0] - self.vel: 
                plat_2.y += self.vel
                screen.blit(self.plat_img, (plat_2.x, plat_2.y - 20))
            else:
                self.vel = self.vel * -1
                plat_2.y += self.vel

            if player_lv1.colliderect(plat_2):
                if abs(plat_2.top - player_lv1.bottom) < 15:
                    player_lv1.y -= 14
                if abs(plat_2.bottom - player_lv1.top) < 15:
                    player_lv1.y = 200

class plat3(object):
    plat_img = load(os.path.join(wd,'data','plat_3.png'))
    def __init__(self, y, end):
        self.y = y
        self.path = [y, end]
        self.vel = 3

    def draw(self, screen):
        self.move()
        #py.draw.rect(screen, (255,0,0), plat_3, 1)

    def move(self):
        if self.vel > 0:
            if plat_3.y < self.path[1] + self.vel:
                plat_3.y += self.vel
                screen.blit(self.plat_img, (plat_3.x, plat_3.y - 20))
            else:
                self.vel = self.vel * -1
                plat_3.y += self.vel

            if player_lv1.colliderect(plat_3):
                if abs(plat_3.top - player_lv1.bottom) < 15:
                    player_lv1.y -= 8
                
        else:
            if plat_3.y > self.path[0] - self.vel: 
                plat_3.y += self.vel
                screen.blit(self.plat_img, (plat_3.x, plat_3.y - 20))
            else:
                self.vel = self.vel * -1
                plat_3.y += self.vel

            if player_lv1.colliderect(plat_3):
                if abs(plat_3.top - player_lv1.bottom) < 15:
                    player_lv1.y -= 14
#--------------Level 4 -----------------#
class Lazer1(object):
    def __init__(self, end):
        self.x = lazer1_rect.x
        self.path = [lazer1_rect.x, end]
        self.vel = 30
        self.next_pos1 = 0
        self.next_pos2 = 0

    def draw(self, screen):
        self.move()
        #py.draw.rect(screen, (255,0,0), lazer1_rect)

    def move(self):
        global health_player
        lazer = load(os.path.join(wd,'data','lazer.png'))
        screen.blit(lazer, (lazer1_rect.x, lazer1_rect.y))
        a1 = 45; a2 = 88; a3 = 131; a4 = 174; a5 = 217
        a6 = 260; a7 = 303; a8 = 346; a9 = 389; a10 = 432
        a11 = 475; a12 = 518; a13 = 561; a14 = 604; a15 = 647
        a16 = 690; a17 = 733; a18 = 776; a19 = 819
        rand_num = random.randint(236, 600)
        if self.next_pos1 > 900:
            self.next_pos1 = 0
            self.next_pos2 = 0
        if self.vel > 0:
            if lazer1_rect.x < self.path[1] + self.vel:
                lazer1_rect.x += self.vel
                self.next_pos1 += 1

                 #----------------DIREITA---------------#
                if self.next_pos1 > a1 and self.next_pos1 < a2:
                    if self.next_pos1 >= a1 and self.next_pos1 < a1+2:
                        lazer1_rect.y = rand_num        
                if self.next_pos1 > a2 and self.next_pos1 < a3:
                    if self.next_pos1 >= a2 and self.next_pos1 < a2+2:
                        lazer1_rect.y = rand_num
                if self.next_pos1 > a3 and self.next_pos1 < a4:
                    if self.next_pos1 >= a3 and self.next_pos1 < a3+2:
                        lazer1_rect.y = rand_num
                if self.next_pos1 > a4 and self.next_pos1 < a5:
                    if self.next_pos1 >= a4 and self.next_pos1 < a4+2:
                        lazer1_rect.y = rand_num
                if self.next_pos1 > a5 and self.next_pos1 < a6:
                    if self.next_pos1 >= a5 and self.next_pos1 < a5+2:
                        lazer1_rect.y = rand_num
                if self.next_pos1 > a6 and self.next_pos1 < a7:
                    if self.next_pos1 >= a6 and self.next_pos1 < a6+2:
                        lazer1_rect.y = rand_num
                if self.next_pos1 > a7 and self.next_pos1 < a8:
                    if self.next_pos1 >= a7 and self.next_pos1 < a7+2:
                        lazer1_rect.y = rand_num
                if self.next_pos1 > a8 and self.next_pos1 < a9:
                    if self.next_pos1 >= a8 and self.next_pos1 < a8+2:
                        lazer1_rect.y = rand_num
                if self.next_pos1 > a9 and self.next_pos1 < a10:
                    if self.next_pos1 >= a9 and self.next_pos1 < a9+2:
                        lazer1_rect.y = rand_num                       
                if self.next_pos1 > a10 and self.next_pos1 < a11:
                    if self.next_pos1 >= a10 and self.next_pos1 < a10+2:
                        lazer1_rect.y = rand_num                       
                if self.next_pos1 > a11 and self.next_pos1 < a12:
                    if self.next_pos1 >= a11 and self.next_pos1 < a11+2:
                        lazer1_rect.y = rand_num                        
                if self.next_pos1 > a12 and self.next_pos1 < a13:
                    if self.next_pos1 >= a11 and self.next_pos1 < a12+2:
                        lazer1_rect.y = rand_num                        
                if self.next_pos1 > a13 and self.next_pos1 < a14:
                    if self.next_pos1 >= a13 and self.next_pos1 < a13+2:
                        lazer1_rect.y = rand_num                       
                if self.next_pos1 > a14 and self.next_pos1 < a15:
                    if self.next_pos1 >= a14 and self.next_pos1 < a14+2:
                        lazer1_rect.y = rand_num                        
                if self.next_pos1 > a15 and self.next_pos1 < a16:
                    if self.next_pos1 >= a15 and self.next_pos1 < a15+2:
                        lazer1_rect.y = rand_num                        
                if self.next_pos1 > a16 and self.next_pos1 < a17:
                    if self.next_pos1 >= a16 and self.next_pos1 < a16+2:
                        lazer1_rect.y = rand_num                       
                if self.next_pos1 > a17 and self.next_pos1 < a18:
                    if self.next_pos1 >= a17 and self.next_pos1 < a17+2:
                        lazer1_rect.y = rand_num                       
                if self.next_pos1 > a18 and self.next_pos1 < a19:
                    if self.next_pos1 >= a18 and self.next_pos1 < a18+2:
                        lazer1_rect.y = rand_num                
                if self.next_pos1 > a19 and self.next_pos1 < 864:
                    if self.next_pos1 >= a19 and self.next_pos1 < a19+2:
                        lazer1_rect.y = rand_num
                    
            else:
                self.vel = self.vel * -1
                lazer1_rect.x += self.vel
                
                
        else:
            if lazer1_rect.x > self.path[0] - self.vel: 
                lazer1_rect.x += self.vel
                self.next_pos2 += 1
                #----------------ESQUERDA---------------#
                if self.next_pos2 > a1 and self.next_pos2 < a2:
                    if self.next_pos2 >= a1 and self.next_pos2 < a1+2:
                        lazer1_rect.y = rand_num  
                if self.next_pos2 > a2 and self.next_pos2 < a3:
                    if self.next_pos2 >= a2 and self.next_pos2 < a2+2:
                        lazer1_rect.y = rand_num
                if self.next_pos2 > a3 and self.next_pos2 < a4:
                    if self.next_pos2 >= a3 and self.next_pos2 < a3+2:
                        lazer1_rect.y = rand_num
                if self.next_pos2 > a4 and self.next_pos2 < a5:
                    if self.next_pos2 >= a4 and self.next_pos2 < a4+2:
                        lazer1_rect.y = rand_num
                if self.next_pos2 > a5 and self.next_pos2 < a6:
                    if self.next_pos2 >= a5 and self.next_pos2 < a5+2:
                        lazer1_rect.y = rand_num
                if self.next_pos2 > a6 and self.next_pos2 < a7:
                    if self.next_pos2 >= a6 and self.next_pos2 < a6+2:
                        lazer1_rect.y = rand_num
                if self.next_pos2 > a7 and self.next_pos2 < a8:
                    if self.next_pos2 >= a7 and self.next_pos2 < a7+2:
                        lazer1_rect.y = rand_num
                if self.next_pos2 > a8 and self.next_pos2 < a9:
                    if self.next_pos2 >= a8 and self.next_pos2 < a8+2:
                        lazer1_rect.y = rand_num
                if self.next_pos2 > a9 and self.next_pos2 < a10:
                    if self.next_pos2 >= a9 and self.next_pos2 < a9+2:
                        lazer1_rect.y = rand_num
                if self.next_pos2 > a10 and self.next_pos2 < a11:
                    if self.next_pos2 >= a10 and self.next_pos2 < a10+2:
                        lazer1_rect.y = rand_num                    
                if self.next_pos2 > a11 and self.next_pos2 < a12:
                    if self.next_pos2 >= a11 and self.next_pos2 < a11+2:
                        lazer1_rect.y = rand_num                        
                if self.next_pos2 > a12 and self.next_pos2 < a13:
                    if self.next_pos2 >= a11 and self.next_pos2 < a12+2:
                        lazer1_rect.y = rand_num                        
                if self.next_pos2 > a13 and self.next_pos2 < a14:
                    if self.next_pos2 >= a13 and self.next_pos2 < a13+2:
                        lazer1_rect.y = rand_num                        
                if self.next_pos2 > a14 and self.next_pos2 < a15:
                    if self.next_pos2 >= a14 and self.next_pos2 < a14+2:
                        lazer1_rect.y = rand_num                        
                if self.next_pos2 > a15 and self.next_pos2 < a16:
                    if self.next_pos2 >= a15 and self.next_pos2 < a15+2:
                        lazer1_rect.y = rand_num                       
                if self.next_pos2 > a16 and self.next_pos2 < a17:
                    if self.next_pos2 >= a16 and self.next_pos2 < a16+2:
                        lazer1_rect.y = rand_num                      
                if self.next_pos2 > a17 and self.next_pos2 < a18:
                    if self.next_pos2 >= a17 and self.next_pos2 < a17+2:
                        lazer1_rect.y = rand_num                       
                if self.next_pos2 > a18 and self.next_pos2 < a19:
                    if self.next_pos2 >= a18 and self.next_pos2 < a18+2:
                        lazer1_rect.y = rand_num                    
                if self.next_pos2 > a19 and self.next_pos2 < 864:
                    if self.next_pos2 >= a19 and self.next_pos2 < a19+2:
                        lazer1_rect.y = rand_num
  
                   
            else:
                self.vel = self.vel * -1
                lazer1_rect.x += self.vel

        if player_1.colliderect(lazer1_rect):
            death_player.play()
            health_player += 1
            if abs(player_1.top - lazer1_rect.bottom) < 15:
                player_1.y += 10
            if abs(player_1.bottom - lazer1_rect.top) < 15:
                player_1.y -= 10
            if abs(player_1.left - lazer1_rect.right) < 15:
                player_1.y += 30
            if abs(player_1.right - lazer1_rect.left) < 15:
                player_1.y -= 30

################################################################################################
class Lazer2(object):
    def __init__(self, end):
        self.x = lazer1_rect_2.x
        self.path = [lazer1_rect_2.x, end]
        self.vel = 30
        self.next_pos1 = 0
        self.next_pos2 = 0

    def draw(self, screen):
        global time__
        time__ += 1
        if time__ > 54:
            self.move()
        #py.draw.rect(screen, (255,0,0), lazer1_rect_2,1)

    def move(self):
        global health_player
        lazer = load(os.path.join(wd,'data','lazer.png'))
        screen.blit(lazer, (lazer1_rect_2.x, lazer1_rect_2.y))
        a1 = 45; a2 = 88; a3 = 131; a4 = 174; a5 = 217
        a6 = 260; a7 = 303; a8 = 346; a9 = 389; a10 = 432
        a11 = 475; a12 = 518; a13 = 561; a14 = 604; a15 = 647
        a16 = 690; a17 = 733; a18 = 776; a19 = 819
        rand_num = random.randint(220, 550)
        if self.next_pos1 > 900:
            self.next_pos1 = 0
            self.next_pos2 = 0
        if self.vel > 0:
            if lazer1_rect_2.x < self.path[1] + self.vel:
                lazer1_rect_2.x += self.vel
                self.next_pos1 += 1

                 #----------------DIREITA---------------#
                if self.next_pos1 > a1 and self.next_pos1 < a2:
                    if self.next_pos1 >= a1 and self.next_pos1 < a1+2:
                        lazer1_rect_2.y = rand_num        
                if self.next_pos1 > a2 and self.next_pos1 < a3:
                    if self.next_pos1 >= a2 and self.next_pos1 < a2+2:
                        lazer1_rect_2.y = rand_num
                if self.next_pos1 > a3 and self.next_pos1 < a4:
                    if self.next_pos1 >= a3 and self.next_pos1 < a3+2:
                        lazer1_rect_2.y = rand_num
                if self.next_pos1 > a4 and self.next_pos1 < a5:
                    if self.next_pos1 >= a4 and self.next_pos1 < a4+2:
                        lazer1_rect_2.y = rand_num
                if self.next_pos1 > a5 and self.next_pos1 < a6:
                    if self.next_pos1 >= a5 and self.next_pos1 < a5+2:
                        lazer1_rect_2.y = rand_num
                if self.next_pos1 > a6 and self.next_pos1 < a7:
                    if self.next_pos1 >= a6 and self.next_pos1 < a6+2:
                        lazer1_rect_2.y = rand_num
                if self.next_pos1 > a7 and self.next_pos1 < a8:
                    if self.next_pos1 >= a7 and self.next_pos1 < a7+2:
                        lazer1_rect_2.y = rand_num
                if self.next_pos1 > a8 and self.next_pos1 < a9:
                    if self.next_pos1 >= a8 and self.next_pos1 < a8+2:
                        lazer1_rect_2.y = rand_num
                if self.next_pos1 > a9 and self.next_pos1 < a10:
                    if self.next_pos1 >= a9 and self.next_pos1 < a9+2:
                        lazer1_rect_2.y = rand_num                       
                if self.next_pos1 > a10 and self.next_pos1 < a11:
                    if self.next_pos1 >= a10 and self.next_pos1 < a10+2:
                        lazer1_rect_2.y = rand_num                       
                if self.next_pos1 > a11 and self.next_pos1 < a12:
                    if self.next_pos1 >= a11 and self.next_pos1 < a11+2:
                        lazer1_rect_2.y = rand_num                        
                if self.next_pos1 > a12 and self.next_pos1 < a13:
                    if self.next_pos1 >= a11 and self.next_pos1 < a12+2:
                        lazer1_rect_2.y = rand_num                        
                if self.next_pos1 > a13 and self.next_pos1 < a14:
                    if self.next_pos1 >= a13 and self.next_pos1 < a13+2:
                        lazer1_rect_2.y = rand_num                       
                if self.next_pos1 > a14 and self.next_pos1 < a15:
                    if self.next_pos1 >= a14 and self.next_pos1 < a14+2:
                        lazer1_rect_2.y = rand_num                        
                if self.next_pos1 > a15 and self.next_pos1 < a16:
                    if self.next_pos1 >= a15 and self.next_pos1 < a15+2:
                        lazer1_rect_2.y = rand_num                        
                if self.next_pos1 > a16 and self.next_pos1 < a17:
                    if self.next_pos1 >= a16 and self.next_pos1 < a16+2:
                        lazer1_rect_2.y = rand_num                       
                if self.next_pos1 > a17 and self.next_pos1 < a18:
                    if self.next_pos1 >= a17 and self.next_pos1 < a17+2:
                        lazer1_rect_2.y = rand_num                       
                if self.next_pos1 > a18 and self.next_pos1 < a19:
                    if self.next_pos1 >= a18 and self.next_pos1 < a18+2:
                        lazer1_rect_2.y = rand_num                
                if self.next_pos1 > a19 and self.next_pos1 < 864:
                    if self.next_pos1 >= a19 and self.next_pos1 < a19+2:
                        lazer1_rect_2.y = rand_num
                    
            else:
                self.vel = self.vel * -1
                lazer1_rect_2.x += self.vel
                
                
        else:
            if lazer1_rect_2.x > self.path[0] - self.vel: 
                lazer1_rect_2.x += self.vel
                self.next_pos2 += 1
                #----------------ESQUERDA---------------#
                if self.next_pos2 > a1 and self.next_pos2 < a2:
                    if self.next_pos2 >= a1 and self.next_pos2 < a1+2:
                        lazer1_rect_2.y = rand_num  
                if self.next_pos2 > a2 and self.next_pos2 < a3:
                    if self.next_pos2 >= a2 and self.next_pos2 < a2+2:
                        lazer1_rect_2.y = rand_num
                if self.next_pos2 > a3 and self.next_pos2 < a4:
                    if self.next_pos2 >= a3 and self.next_pos2 < a3+2:
                        lazer1_rect_2.y = rand_num
                if self.next_pos2 > a4 and self.next_pos2 < a5:
                    if self.next_pos2 >= a4 and self.next_pos2 < a4+2:
                        lazer1_rect_2.y = rand_num
                if self.next_pos2 > a5 and self.next_pos2 < a6:
                    if self.next_pos2 >= a5 and self.next_pos2 < a5+2:
                        lazer1_rect_2.y = rand_num
                if self.next_pos2 > a6 and self.next_pos2 < a7:
                    if self.next_pos2 >= a6 and self.next_pos2 < a6+2:
                        lazer1_rect_2.y = rand_num
                if self.next_pos2 > a7 and self.next_pos2 < a8:
                    if self.next_pos2 >= a7 and self.next_pos2 < a7+2:
                        lazer1_rect_2.y = rand_num
                if self.next_pos2 > a8 and self.next_pos2 < a9:
                    if self.next_pos2 >= a8 and self.next_pos2 < a8+2:
                        lazer1_rect_2.y = rand_num
                if self.next_pos2 > a9 and self.next_pos2 < a10:
                    if self.next_pos2 >= a9 and self.next_pos2 < a9+2:
                        lazer1_rect_2.y = rand_num
                if self.next_pos2 > a10 and self.next_pos2 < a11:
                    if self.next_pos2 >= a10 and self.next_pos2 < a10+2:
                        lazer1_rect_2.y = rand_num                    
                if self.next_pos2 > a11 and self.next_pos2 < a12:
                    if self.next_pos2 >= a11 and self.next_pos2 < a11+2:
                        lazer1_rect_2.y = rand_num                        
                if self.next_pos2 > a12 and self.next_pos2 < a13:
                    if self.next_pos2 >= a11 and self.next_pos2 < a12+2:
                        lazer1_rect_2.y = rand_num                        
                if self.next_pos2 > a13 and self.next_pos2 < a14:
                    if self.next_pos2 >= a13 and self.next_pos2 < a13+2:
                        lazer1_rect_2.y = rand_num                        
                if self.next_pos2 > a14 and self.next_pos2 < a15:
                    if self.next_pos2 >= a14 and self.next_pos2 < a14+2:
                        lazer1_rect_2.y = rand_num                        
                if self.next_pos2 > a15 and self.next_pos2 < a16:
                    if self.next_pos2 >= a15 and self.next_pos2 < a15+2:
                        lazer1_rect_2.y = rand_num                       
                if self.next_pos2 > a16 and self.next_pos2 < a17:
                    if self.next_pos2 >= a16 and self.next_pos2 < a16+2:
                        lazer1_rect_2.y = rand_num                      
                if self.next_pos2 > a17 and self.next_pos2 < a18:
                    if self.next_pos2 >= a17 and self.next_pos2 < a17+2:
                        lazer1_rect_2.y = rand_num                       
                if self.next_pos2 > a18 and self.next_pos2 < a19:
                    if self.next_pos2 >= a18 and self.next_pos2 < a18+2:
                        lazer1_rect_2.y = rand_num                    
                if self.next_pos2 > a19 and self.next_pos2 < 864:
                    if self.next_pos2 >= a19 and self.next_pos2 < a19+2:
                        lazer1_rect_2.y = rand_num
  
                   
            else:
                self.vel = self.vel * -1
                lazer1_rect_2.x += self.vel
                lazer1_rect_2.y = 300

        if player_1.colliderect(lazer1_rect_2):
            death_player.play()
            health_player += 1
            if abs(player_1.top - lazer1_rect_2.bottom) < 15:
                player_1.y += 10
            if abs(player_1.bottom - lazer1_rect_2.top) < 15:
                player_1.y -= 10
            if abs(player_1.left - lazer1_rect_2.right) < 15:
                player_1.y += 30
            if abs(player_1.top - lazer1_rect_2.bottom) < 15:
                player_1.y -= 30
            
class slideWindow(object):
    window = load(os.path.join(wd,'data','window_up.png'))
    def __init__(self, y, end):
        self.y = y
        self.path = [y, end]
        self.vel = 1
    def draw(self, screen):
        self.move()
        screen.blit(self.window, (window_rect.x,window_rect.y))
        #py.draw.rect(screen, (255,0,0), window, 1)

    def move(self):
        if window_slide_up_ok:
            if self.vel > 0:
                if window_rect.y < self.path[1] + self.vel:
                    window_rect.y -= self.vel
                    if window_rect.y < 0:
                        self.vel = 0
                else:
                    self.vel = self.vel * -1
                    window_rect.y += self.vel
                    
            else:
                if window_rect.y > self.path[0] - self.vel: 
                    window_rect.y += self.vel
                else:
                    self.vel = self.vel * -1
                    window_rect.y += self.vel

class gradeUp(object):
    def __init__(self, end):
        self.y = grade_rect.y
        self.path = [grade_rect.y, end]
        self.vel = 1
        self.img = load(os.path.join(wd,'data','grade.png'))
    def draw(self, screen):
        self.move()
        screen.blit(self.img, (grade_rect.x,grade_rect.y))
        #py.draw.rect(screen, (255,0,0), window, 1)
    def move(self):
        if can_open_grade:
            if self.vel > 0:
                if grade_rect.y < self.path[1] + self.vel:
                    grade_rect.y -= self.vel
                    if grade_rect.y < 0:
                        self.vel = 0
                else:
                    self.vel = self.vel * -1
                    grade_rect.y += self.vel
                    
            else:
                if grade_rect.y > self.path[0] - self.vel: 
                    grade_rect.y += self.vel
                else:
                    self.vel = self.vel * -1
                    grade_rect.y += self.vel

class door1(object):
    def __init__(self, y, end):
        self.y = y
        self.path = [y, end]
        self.vel = 2
        self.active_door = 0
        self.pos = 443, 366

    def draw(self, screen):
        self.move()
        #py.draw.rect(screen,(255,0,0), door_rect_1,1)

    def move(self):
        alavanca_img_1 = load(os.path.join(wd,'data','alavanca-1.png'))
        alavanca_img_2 = load(os.path.join(wd,'data','alavanca-2.png'))
        screen.blit(door_img, (door_rect_1.x - 1, door_rect_1.y - 5))
        keys = py.key.get_pressed()
        if player_lv1.colliderect(alavanca1):
            if keys[py.K_e]:
                self.active_door += 1
        if self.active_door == 0:
            screen.blit(alavanca_img_1, (443,366))
        elif self.active_door == 1:
            screen.blit(alavanca_img_2, (443,366))
            handle.play()
            self.active_door += 1
        else:
            screen.blit(alavanca_img_2, (443,366))

        if self.active_door > 0:        
            if self.vel > 0:
                if door_rect_1.y < self.path[1] + self.vel:
                    door_rect_1.y -= self.vel
                    if door_rect_1.y < 0:
                        self.vel = 0
                else:
                    self.vel = self.vel * -1
                    door_rect_1.y -= self.vel
            else:
                if door_rect_1.y > self.path[0] - self.vel: 
                    door_rect_1.y -= self.vel

                else:
                    self.vel = self.vel * -1
                    door_rect_1.y -= self.vel

        if player_lv1.colliderect(door_rect_1):
                if abs(door_rect_1.right - player_lv1.left) < 15:
                    player_lv1.x += 11

class door2(object):
    door_2_img = load(os.path.join(wd,'data','door2.png'))
    def __init__(self, y, end):
        self.y = y
        self.path = [y, end]
        self.vel = 3
        self.active_door = 0
        self.pos = 443, 366

    def draw(self, screen):
        self.move()

    def move(self):
        alavanca_img_1 = load(os.path.join(wd,'data','alavanca-1.png'))
        alavanca_img_2 = load(os.path.join(wd,'data','alavanca-2.png'))
        alavanca_img_flip_1 = py.transform.flip(alavanca_img_1, True, False)
        alavanca_img_flip_2 = py.transform.flip(alavanca_img_2, True, False)

        screen.blit(self.door_2_img, (door_rect_2.x, door_rect_2.y - 20))
        keys = py.key.get_pressed()
        if player_lv1.colliderect(alavanca2):
            if keys[py.K_e]:
                self.active_door += 1
        if self.active_door == 0:
            screen.blit(alavanca_img_flip_1, (400,366))
        elif self.active_door == 1:
            handle.play()
            self.active_door += 1
        else:
            screen.blit(alavanca_img_flip_2, (400,366))
        if self.active_door > 0:        
            if self.vel > 0:
                if door_rect_2.y < self.path[1] + self.vel:
                    door_rect_2.y += self.vel

                else:
                    self.vel = self.vel * -1
                    door_rect_2.y += self.vel

                if player_lv1.colliderect(door_rect_2):
                    if abs(door_rect_2.top - player_lv1.bottom) < 15:
                        player_lv1.y -= 8
                
            else:
                if door_rect_2.y > self.path[0] - self.vel: 
                    door_rect_2.y += self.vel
                else:
                    self.vel = self.vel * -1
                    door_rect_2.y += self.vel

                if player_lv1.colliderect(door_rect_2):
                    if abs(door_rect_2.top - player_lv1.bottom) < 15:
                        player_lv1.y -= 14                    

class minion1(object):
    minion_red_left = load(os.path.join(wd,'data','minion_blue.png'))
    minion_red_right = py.transform.flip(minion_red_left, True, False)
    def __init__(self, x, end):
        self.x = x
        self.path = [x, end]
        self.vel = 8.5

    def draw(self, screen):
        self.move()
        #py.draw.rect(screen, (255,0,0), minion_1, 2)

    def move(self):
        if self.vel > 0:
            if minion_1.x < self.path[1] + self.vel:
                minion_1.x += self.vel
                screen.blit(self.minion_red_right, (minion_1.x, minion_1.y))
            else:
                self.vel = self.vel * -1
                minion_1.x += self.vel
                
        else:
            if minion_1.x > self.path[0] - self.vel: 
                minion_1.x = 170
            else:
                self.vel = self.vel * -1
                minion_1.x += self.vel

        if player_lv1.colliderect(minion_1):
            health_player += 1
            death_player.play()
            if abs(minion_1.right - player_lv1.left) < 15:
                player_lv1.y -= 11
                player_lv1.x, player_lv1.y = 635, 579
            if abs(minion_1.bottom - player_lv1.top) < 15:
                player_lv1.y -= 11
                player_lv1.x, player_lv1.y = 635, 579
            if abs(minion_1.left - player_lv1.right) < 15:
                player_lv1.y -= 11
                player_lv1.x, player_lv1.y = 635, 579

class fireball(object):
    global current_time, health_player

    minion_red = load(os.path.join(wd,'data','minion_red.png'))
    fire_ball_img = load(os.path.join(wd,'data','fire_ball.png'))
    def __init__(self, x, end):
        self.x = x
        self.path = [x, end]
        self.vel = 5
        self.can_fire = 0
        self.minion_death = 0
        self.time_pos_1s = 0
        self.time_pos_2s = 0
        self.time_pos_3s = 0
        self.time_pos_4s = 0
        self.time_pos_5s = 0
        self.time_1s = 0
        self.time_2s = 0
        self.time_3s = 0
        self.time_4s = 0
        self.time_5s = 0

    def draw(self, screen):
        self.move()
        screen.blit(self.minion_red, (minion_2.x, minion_2.y - 15))
        #py.draw.rect(screen, (255,0,0), bug_fix, 2)
        

    def move(self):
        global health_player
        if player_lv1.colliderect(bug_fix):
            bug_fix.y = 1000
            self.can_fire += 1
            self.time_1s = current_time + 1000
            self.time_2s = current_time + 2000
            self.time_3s = current_time + 3000
            self.time_4s = current_time + 4000
            self.time_5s = current_time + 5000
        if player_lv1.colliderect(minion_2):
            if abs(minion_2.top - player_lv1.bottom) < 15:
                self.time_pos_1s = current_time + 1000
                self.time_pos_2s = current_time + 2400
                self.time_pos_3s = current_time + 4000
                self.can_fire += 1
                print('minion morre')
                pop.play()
                self.minion_death += 1
                minion_2.x, minion_2.y = 317, 382
                player_lv1.y -= 11
            if abs(minion_2.bottom - player_lv1.top) < 15:
                print('Voce morreu')
                death_player.play()
                player_lv1.y += 11
                health_player += 1
                if self.minion_death == 0:
                    player_lv1.x, player_lv1.y =10, 500
                elif self.minion_death == 1:
                    player_lv1.x, player_lv1.y = 180, 210
            if abs(minion_2.right - player_lv1.left) < 15:
                print('Voce morreu')
                death_player.play()
                player_lv1.x += 11
                health_player += 1
                if self.minion_death == 0:
                    player_lv1.x, player_lv1.y =10, 500
                elif self.minion_death == 1:
                    player_lv1.x, player_lv1.y = 180, 210
            if abs(minion_2.left - player_lv1.right) < 15:
                print('Voce morreu')
                death_player.play()
                player_lv1.x -= 11
                health_player += 1
                if self.minion_death == 0:
                    player_lv1.x, player_lv1.y =10, 500
                elif self.minion_death == 1:
                    player_lv1.x, player_lv1.y = 180, 210
        if self.minion_death >= 2:
            minion_2.x, minion_2.y = 1000, 1000


        if self.can_fire == 1 :
            if current_time >= self.time_1s:
                if self.vel > 0:
                    if fire_ball_1.x < self.path[1] + self.vel:
                        fire_ball_1.x -= self.vel
                        screen.blit(self.fire_ball_img, (fire_ball_1.x, fire_ball_1.y))
            if current_time >= self.time_2s:
                if self.vel > 0:
                    if fire_ball_2.x < self.path[1] + self.vel:
                        fire_ball_2.x -= self.vel
                        screen.blit(self.fire_ball_img, (fire_ball_2.x, fire_ball_2.y))

            if current_time >= self.time_3s:
                if self.vel > 0:
                    if fire_ball_3.x < self.path[1] + self.vel:
                        fire_ball_3.x -= self.vel
                        screen.blit(self.fire_ball_img, (fire_ball_3.x, fire_ball_3.y))
            if current_time >= self.time_4s:
                if self.vel > 0:
                    if fire_ball_4.x < self.path[1] + self.vel:
                        fire_ball_4.x -= self.vel
                        screen.blit(self.fire_ball_img, (fire_ball_4.x, fire_ball_4.y))                       
            if current_time >= self.time_5s:
                if self.vel > 0:
                    if fire_ball_5.x < self.path[1] + self.vel:
                        fire_ball_5.x -= self.vel
                        screen.blit(self.fire_ball_img, (fire_ball_5.x, fire_ball_5.y))
            
            if fire_ball_1.x < 0:
                fire_ball_1.x = -200
            if fire_ball_2.x < 0:
                fire_ball_2.x = 563
            if fire_ball_3.x < 0:
                fire_ball_3.x = 563
            if fire_ball_4.x < 0:
                fire_ball_4.x = 563
            if fire_ball_5.x < 0:
                fire_ball_5.x = 563

        if self.can_fire == 2:
            if current_time >= self.time_pos_1s:
                if self.vel > 0:
                    if fire_ball_6.x < self.path[1] + self.vel:
                        fire_ball_6.x -= self.vel
                        screen.blit(self.fire_ball_img, (fire_ball_6.x, fire_ball_6.y))
            if current_time >= self.time_pos_2s:
                if self.vel > 0:
                    if fire_ball_7.x < self.path[1] + self.vel:
                        fire_ball_7.x -= self.vel
                        screen.blit(self.fire_ball_img, (fire_ball_7.x, fire_ball_7.y))
            if current_time >= self.time_pos_3s:
                if self.vel > 0:
                    if fire_ball_8.x < self.path[1] + self.vel:
                        fire_ball_8.x -= self.vel
                        screen.blit(self.fire_ball_img, (fire_ball_8.x, fire_ball_8.y))
            

            if fire_ball_6.x < 0:
                fire_ball_6.x = 300
            if fire_ball_7.x < 0:
                fire_ball_7.x = 300
            if fire_ball_8.x < 0:
                fire_ball_8.x = 300

            fire_ball_1.x = -100            
            fire_ball_2.x = -100            
            fire_ball_3.x = -100         
            fire_ball_4.x = -100
            fire_ball_5.x = -100

        if self.can_fire == 3:
           
            
            fire_ball_6.x = -100
            fire_ball_7.x = -100
            fire_ball_8.x = -100
            fire_ball_9.x = -100
            fire_ball_10.x = -100

        if player_lv1.colliderect(fire_ball_1):
            player_lv1.x, player_lv1.y = 10, 500
            death_player.play()
            health_player += 1
        if player_lv1.colliderect(fire_ball_2):
            player_lv1.x, player_lv1.y = 10, 500
            death_player.play()
            health_player += 1
        if player_lv1.colliderect(fire_ball_3):
            player_lv1.x, player_lv1.y = 10, 500
            death_player.play()
            health_player += 1
        if player_lv1.colliderect(fire_ball_4):
            player_lv1.x, player_lv1.y = 10, 500
            death_player.play()
            health_player += 1
        if player_lv1.colliderect(fire_ball_5):
            player_lv1.x, player_lv1.y = 10, 500
            death_player.play()
            health_player += 1
        if player_lv1.colliderect(fire_ball_6):
            player_lv1.x, player_lv1.y = 180, 210
            death_player.play()
            health_player += 1
        if player_lv1.colliderect(fire_ball_7):
            player_lv1.x, player_lv1.y = 180, 210
            death_player.play()
            health_player += 1
        if player_lv1.colliderect(fire_ball_8):
            player_lv1.x, player_lv1.y = 180, 210
            death_player.play()
            health_player += 1
        if player_lv1.colliderect(fire_ball_9):
            player_lv1.x, player_lv1.y = 180, 210
            death_player.play()
            health_player += 1
        if player_lv1.colliderect(fire_ball_10):
            player_lv1.x, player_lv1.y = 180, 210
            death_player.play()
            health_player += 1
        

class serra(object):
    serra_img = [load(os.path.join(wd,'data','serra-1.png')),load(os.path.join(wd,'data','serra-2.png')),load(os.path.join(wd,'data','serra-3.png'))]

    def __init__(self, x, end):
        self.x = x
        self.path = [x, end]
        self.vel = 3
        self.count = 0

    def draw(self, screen):
        self.move()
        #py.draw.rect(screen, (255,0,0), serra_rect, 2)

    def move(self):
        if self.count + 1 >= 27:
            self.count = 0

        if self.vel > 0:
            if serra_rect.x < self.path[1] + self.vel:
                serra_rect.x += self.vel
                screen.blit(self.serra_img[self.count//9], (serra_rect.x - 18, serra_rect.y))
                self.count += 1
            else:
                self.vel = self.vel * -1
                serra_rect.x += self.vel
                
        else:
            if serra_rect.x > self.path[0] - self.vel: 
                serra_rect.x += self.vel
                screen.blit(self.serra_img[self.count//9], (serra_rect.x - 18, serra_rect.y))
                self.count += 1
            else:
                self.vel = self.vel * -1
                serra_rect.x += self.vel

        if player_lv1.colliderect(serra_rect):
            death_player.play()
            health_player += 1
            if abs(serra_rect.right - player_lv1.left) < 15:
                player_lv1.y -= 11
                player_lv1.x, player_lv1.y = 642, 212
            if abs(serra_rect.bottom - player_lv1.top) < 15:
                player_lv1.y -= 11
                player_lv1.x, player_lv1.y = 642, 212
            if abs(serra_rect.left - player_lv1.right) < 15:
                player_lv1.y -= 11
                player_lv1.x, player_lv1.y = 642, 212
            if abs(serra_rect.top - player_lv1.bottom) < 15:
                player_lv1.y -= 11
                player_lv1.x, player_lv1.y = 642, 212
class timing():
    def __init__(self):
        self.dois_segundos = 0
        self.sec()
    def sec(self):
        self.dois_segundos = current_time + 2000
        print(f'2 sec{self.dois_segundos} | corrente:{current_time}')

class GameStages():
    def __init__(self):
        self.stage = 'intro'
        self.unblock_1 = False
        self.unblock_2 = False
        self.unblock_3 = False
        self.hit = 0
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.count = 0

    def stage_manager(self):
        if self.stage == 'intro':
            self.intro()
        if self.stage == 'comandos':
            self.comandos()
        if self.stage == 'stage_1':
            self.stage_1()
        if self.stage == 'stage_2':
            self.stage_2()
        if self.stage == 'level_1':
            self.level_1()
        if self.stage == 'level_2':
            self.level_2() 
        if self.stage == 'level_3':
            self.level_3()
        if self.stage == 'level_4':
            self.level_4()
        
    def intro(self):
        screen.blit(start ,(0, 0))
        #-----------Jogar------------#
        if event.type == py.MOUSEMOTION:
            m_x, m_y = py.mouse.get_pos()
            m_rect = py.Rect(m_x, m_y, 50, 50)
            if m_rect.colliderect(jogar):
                screen.blit(jogar_img, (203, 298))

        if event.type == py.MOUSEBUTTONDOWN:
            m_x, m_y = py.mouse.get_pos()
            m_rect = py.Rect(m_x, m_y, 10, 10)
            
            if m_rect.colliderect(jogar):
                click.play()
                time.sleep(0.2)
                print('JOGAR')
                self.stage = 'stage_1'
        
        #-----------Controles---------#
        if event.type == py.MOUSEMOTION:
            m_x, m_y = py.mouse.get_pos()
            m_rect = py.Rect(m_x, m_y, 10, 10)
            if m_rect.colliderect(comandos):
                screen.blit(comandos_img, (203, 431))

        if event.type == py.MOUSEBUTTONDOWN: 
            m_x, m_y = py.mouse.get_pos()
            m_rect = py.Rect(m_x, m_y, 10, 10)
            if m_rect.colliderect(comandos):
                click.play()
                time.sleep(0.2)
                print('COMANDOS')
                self.stage = 'comandos'

        #-------------Sair-----------#
        if event.type == py.MOUSEMOTION:
            m_x, m_y = py.mouse.get_pos()
            m_rect = py.Rect(m_x, m_y, 10, 10)
            if m_rect.colliderect(sair):
                screen.blit(sair_img, (203, 564))

        if event.type == py.MOUSEBUTTONDOWN: 
            m_x, m_y = py.mouse.get_pos()
            m_rect = py.Rect(m_x, m_y, 10, 10)
            if m_rect.colliderect(sair):
                click.play()
                time.sleep(0.2)
                print('SAIR')
                py.quit()

        py.display.update()

    def comandos(self):
        screen.blit(comandos_start, (0,0))
        if event.type == py.MOUSEMOTION:
            m_x, m_y = py.mouse.get_pos()
            m_rect = py.Rect(m_x, m_y, 10, 10)
            if m_rect.colliderect(voltar):
                screen.blit(voltar_img, (28,24))

        if event.type == py.MOUSEBUTTONDOWN:
            m_x, m_y = py.mouse.get_pos()
            m_rect = py.Rect(m_x, m_y, 10, 10)
            if m_rect.colliderect(voltar):
                click.play()
                time.sleep(0.5)
                print('VOLTAR')
                self.stage = 'intro'

    def anim_p_lv1(self):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if self.left:
            screen.blit(walkLeft[self.walkCount//3], (player_lv1.x, player_lv1.y))
            self.walkCount += 1
        elif self.right:
            screen.blit(walkRight[self.walkCount//3], (player_lv1.x, player_lv1.y))
            self.walkCount += 1
        else:
            screen.blit(Stand[self.walkCount//3], (player_lv1.x, player_lv1.y))
            self.walkCount += 1
        
        py.display.update()

    def anim_p_normal_st2(self):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if self.left:
            screen.blit(walkLeft[self.walkCount//3], (player_1.x, player_1.y))
            self.walkCount += 1
        elif self.right:
            screen.blit(walkRight[self.walkCount//3], (player_1.x, player_1.y))
            self.walkCount += 1
        elif self.up:
            screen.blit(walkUp[self.walkCount//3], (player_1.x, player_1.y))
            self.walkCount += 1
        elif self.down:
            screen.blit(walkDown[self.walkCount//3], (player_1.x, player_1.y))
            self.walkCount += 1
        else:
            screen.blit(Stand[self.walkCount//3], (player_1.x, player_1.y))
            self.walkCount += 1
        

    def anim_p_normal_st1(self):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if self.left:
            screen.blit(walkLeft[self.walkCount//3], (player.x, player.y))
            self.walkCount += 1
        elif self.right:
            screen.blit(walkRight[self.walkCount//3], (player.x, player.y))
            self.walkCount += 1
        elif self.up:
            screen.blit(walkUp[self.walkCount//3], (player.x, player.y))
            self.walkCount += 1
        elif self.down:
            screen.blit(walkDown[self.walkCount//3], (player.x, player.y))
            self.walkCount += 1
        else:
            screen.blit(Stand[self.walkCount//3], (player.x, player.y))
            self.walkCount += 1
        if player.colliderect(chairP):
            screen.blit(player_back, (player.x, player.y))
            screen.blit(chair,(550, 193))

    def level_4(self):
        exclamation = load(os.path.join(wd,'data','exclamation.png'))
        left_p_img = load(os.path.join(wd,'data','L1.png'))
        global liberar, health_player, reset_to_0, next_level,time_a3,time_a4, time_fight ,grade_rect, can_open_grade, del_player, time_a1, time_a2, window_slide_up, window_slide_up_ok
        time_a1 += 1
        if time_a1 > 1 and time_a1 < 3:
            player_1.x, player_1.y = 500, 400
        
        keys = py.key.get_pressed()
        if not window_slide_up_ok:
            if keys[py.K_w]:
                player_1.y -= vel + 3
                self.left = False
                self.right = False
                self.up = True
                self.down = False
            elif keys[py.K_s]:
                player_1.y += vel + 3
                self.left = False
                self.right = False
                self.up = False
                self.down = True
            elif keys[py.K_a]:
                player_1.x -= vel + 3
                self.left = True
                self.right = False
                self.up = False
                self.down = False
            elif keys[py.K_d]:
                player_1.x += vel + 3
                self.left = False
                self.right = True
                self.up = False
                self.down = False
            else:
                self.left = False
                self.right = False
                self.up = False
                self.down = False

        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if player_1.colliderect(red_buttom):
            window_slide_up = True
        
        collision_rect_st3()
        walls_stage_6()
        screen.blit(stage_pygame, (0,0))
        v1.draw(screen)
        g1.draw(screen)

        if not del_player:
            self.anim_p_normal_st2()

        screen.blit(hide_up, (0,-1))
        
        keys = py.key.get_pressed()
        if keys[py.K_e] and window_slide_up:
            window_slide_up_ok = True

        screen_b_x = 68
        screen_b_y = 360
        screen_boss = load(os.path.join(wd,'data','screen_boss_2.png'))

        font_x, font_y = 154,436

        if player_1.colliderect(grade_rect):
                if abs(player_1.top - grade_rect.bottom) < 15:
                    player_1.y += 8

        #--------Boss talking-------------#
        if window_slide_up_ok:
            time_a2 += 1
            if time_a2 > 10 and time_a2 < 101:
                del_player = True
                screen.blit(left_p_img, (player_1.x, player_1.y))
            if time_a2 > 100 and time_a2 < 130:
                player_1.y += vel
                screen.blit(walkDown[self.walkCount//3], (player_1.x, player_1.y))
                self.walkCount += 1
                del_player = True
            if time_a2 > 130 and time_a2 < 170:
                player_1.x -= vel
                screen.blit(walkLeft[self.walkCount//3], (player_1.x, player_1.y))
                self.walkCount += 1
            if time_a2 > 170 and time_a2 < 190:
                screen.blit(walkUp[self.walkCount//3], (player_1.x, player_1.y))
                self.walkCount += 1
                player_1.y -= vel
            if time_a2 > 190:
                screen.blit(walkUp[self.walkCount//3], (player_1.x, player_1.y))
                screen.blit(screen_boss, (screen_b_x, screen_b_y))
            #----------First Part-----------#
            if time_a2 > 200 and time_a2 < 680:
                game_font_16.render_to(screen, (font_x, font_y), '                  Chefe?? Mas porque... o que esta acontecendo?', (0,0,156))
            if time_a2 > 254 and time_a2 < 680:
                game_font_16.render_to(screen, (font_x, font_y + 35), 'Apenas me livrando de pessoas que não preciso mais!', (0,0,0))
            if time_a2 > 360 and time_a2 < 680:
                game_font_16.render_to(screen, (font_x - 50, font_y + 70), 'Como assim não precisa mais? Faço tudo por aquela empresa!', (0,0,156))
            if time_a2 > 440 and time_a2 < 680:
                game_font_16.render_to(screen, (font_x - 50, font_y + 105), 'Por isso mesmo! Meu chefe vai me substituir e por você...', (0,0,0))
            if time_a2 > 520 and time_a2 < 680:
                game_font_16.render_to(screen, (font_x - 50, font_y + 140), 'Como ele ousa fazer isso comigo ? ?', (0,0,0))
            if time_a2 > 600 and time_a2 < 680:
                game_font_16.render_to(screen, (font_x - 50, font_y + 175), 'Não fique triste Marcelo, são apenas negócios...', (0,0,0))
            #----------Second Part-----------#
            if time_a2 > 680 and time_a2 < 1160:
                game_font_16.render_to(screen, (font_x, font_y), 'Agora eu entendi tudo ! Por causa desse maldito código.', (0,0,156))
            if time_a2 > 760 and time_a2 < 1160:
                game_font_16.render_to(screen, (font_x, font_y + 35), 'Nossa, palmas para voce por adivinhar.', (0,0,0))
            if time_a2 > 787 and time_a2 < 1160:
                game_font_16.render_to(screen, (542, font_y + 35), 'HAHAHAHAHA.', (0,0,0))
            if time_a2 > 840 and time_a2 < 1160:
                game_font_16.render_to(screen, (font_x - 50, font_y + 70), '                    Voce vai pagar por tudo isso, Abre essa porta agora', (0,0,156))
            if time_a2 > 920 and time_a2 < 1160:
                game_font_16.render_to(screen, (font_x - 50, font_y + 105), 'Claro que vou abrir, so primeiro deixe me apertar este botão.', (0,0,0))
            if time_a2 > 1000 and time_a2 < 1160:
                game_font_16.render_to(screen, (font_x - 50, font_y + 140), 'HAHAHAHAHAHAHA espero que sobreviva...', (0,0,0))
            if time_a2 > 1027 and time_a2 < 1160:
                game_font_16.render_to(screen, (512, font_y + 140), 'MENTIRA!', (0,0,0))
            if time_a2 > 1054 and time_a2 < 1160:
                game_font_16.render_to(screen, (603, font_y + 140), 'MORRA!', (0,0,0))
            if time_a2 > 1134 and time_a2 < 1160:
                game_font_16.render_to(screen, (font_x - 50, font_y + 175), 'Você é um completo maluco! Me tira daqui de dentro agora!', (0,0,156))
            if time_a2 > 1160:
                del_player = False
                window_slide_up_ok = False
                time_fight = True
        
        #-----------------TIME FIGHT------------------#
        screen_boss_start_fight = load(os.path.join(wd,'data','screen_boss_4.png'))
        if time_fight:
            time_a3 += 1
            if time_a3 > 0 and time_a3 < 160:
                screen.blit(screen_boss_start_fight, (335,5))
            if time_a3 > 10 and time_a3 < 160:
                game_font_20.render_to(screen, (343, 35), 'QUE', (0,0,0))
            if time_a3 > 40 and time_a3 < 160:
                game_font_20.render_to(screen, (394, 35), 'OS', (0,0,0))
            if time_a3 > 80 and time_a3 < 160:
                game_font_20.render_to(screen, (430, 35), 'JOGOS', (0,0,0))
            if time_a3 > 120 and time_a3 < 160:
                game_font_20.render_to(screen, (510, 35), 'COMECEM', (255,0,0))
            if time_a3 > 165:
                game_font_20.render_to(screen, (195, 83), f'MORTES: {health_player}', (255,255,255))
                if time_a3 > 160 and time_a3 < 1850:
                    game_font_20.render_to(screen, (624, 82), 'TEMPO: {:.0f}'.format(time_a4//13.5), (255,255,255))
                    l1.draw(screen)
                if time_a3 > 165 and time_a3 < 167:
                    next_level += 1
                time_a4 -= 0.5
                game_font_20.render_to(screen, (424, 76), f'NÍVEL: {str(next_level)}', (255,255,255))
            if time_a3 > 1850:
                game_font_20.render_to(screen, (624, 82), 'TEMPO: {:.0f}'.format(time_a4//13.5), (255,255,255))
            if time_a3 > 2040 and time_a3 < 2042:
                time_a4 = 864
            if time_a4 < 1:
                time_a4 += 0.5
            if time_a3 > 1900:
                if time_a3 > 1900 and time_a3 < 1902:
                    next_level += 1
                    reset_to_0 = True
                if time_a3 > 1902 and time_a4 < 1904:
                    reset_to_0 = False
                if time_a3 > 1930 and time_a3 < 2035:
                    screen.blit(screen_boss_start_fight, (335,5))
                    if time_a3 > 1940 and time_a3 < 1970:
                        game_font_20.render_to(screen, (350, 30), 'Vamos aumentar a', (0,0,0))
                    if time_a3 > 2000 and time_a3 < 2030:
                        game_font_20.render_to(screen, (350, 40), 'potência dessa vez!', (0,0,0))
                if time_a3 > 2040 and time_a3 < 3940:
                    l2.draw(screen)
                    l1.draw(screen)
                if time_a3 > 3940:
                    screen.blit(screen_boss_start_fight, (335,5))
                if time_a3 > 3940 and time_a3 < 4000:
                    game_font_20.render_to(screen, (343, 40), 'Agora você vai ver!', (0,0,0))
                if time_a3 > 4000 and time_a3 < 4040:
                    game_font_20.render_to(screen, (343, 40), 'POTENCIA MÁXIMA', (0,0,0))
                    can_open_grade = True
                if time_a3 > 4040 and time_a3 < 4080:
                    game_font_20.render_to(screen, (343, 40), 'Ops, botão errado.', (0,0,0))
                if time_a3 > 4080:
                    game_font_20.render_to(screen, (343, 40), 'Podemos conversar... ?', (0,0,0))

            
            
                
            
                    
                
        
    def level_3(self):
        global jumpCount, isJumping
        lol_eraser = load(os.path.join(wd,'data','lol_eraser.png'))
        can_jump = False
        if player_lv1.colliderect(jump_on_1_2):
            can_jump = True
        if player_lv1.colliderect(jump_on_2_2):
            can_jump = True
        if player_lv1.colliderect(jump_on_3_2):
            can_jump = True
        if player_lv1.colliderect(jump_on_4_2):
            can_jump = True
        if player_lv1.colliderect(jump_on_5_2):
            can_jump = True
        if player_lv1.colliderect(jump_on_6_2):
            can_jump = True
        if player_lv1.colliderect(jump_on_7_2):
            can_jump = True
        if player_lv1.colliderect(jump_on_8_2):
            can_jump = True
        if player_lv1.colliderect(jump_on_9_2):
            can_jump = True
        if player_lv1.colliderect(jump_on_10_2):
            can_jump = True
        if player_lv1.colliderect(jump_on_11_2):
            can_jump = True

        event_chest_LV3 = False
        if player_lv1.colliderect(chest_LV3):
            event_chest_LV3 = True

        keys = py.key.get_pressed()
        if keys[py.K_a]:
            player_lv1.x -= vel + 3
            self.left = True
            self.right = False
        elif keys[py.K_d]:
            player_lv1.x += vel + 3
            self.left = False
            self.right = True
        else:
            self.right = False
            self.left = False
            
        if not(isJumping):
            player_lv1.y += 11
            if can_jump:
                if keys[py.K_SPACE]:
                    isJumping = True
                    self.left = False
                    self.right = False
        else:
            if jumpCount >= -1:
                player_lv1.y -= (jumpCount ** 2) * 0.3 * 1
                jumpCount -= 1
            else:
                jumpCount = 8.5
                isJumping = False

        if keys[py.K_e] and event_chest_LV3:
            chest.play()
            time.sleep(2.5)
            self.unblock_3 = True
            LV_3.x, LV_3.y = 1000, 1000
            player_1.x, player_1.y = 388, 29

            jump_on_1_2.x, jump_on_1_2.y = 1000, 1000
            jump_on_2_2.x, jump_on_2_2.y = 1000, 1000
            jump_on_3_2.x, jump_on_3_2.y = 1000, 1000
            jump_on_4_2.x, jump_on_4_2.y = 1000, 1000
            jump_on_5_2.x, jump_on_5_2.y = 1000, 1000
            jump_on_6_2.x, jump_on_6_2.y = 1000, 1000
            jump_on_7_2.x, jump_on_7_2.y = 1000, 1000
            jump_on_8_2.x, jump_on_8_2.y = 1000, 1000
            jump_on_9_2.x, jump_on_9_2.y = 1000, 1000
            jump_on_10_2.x, jump_on_10_2.y = 1000, 1000
            jump_on_11_2.x, jump_on_11_2.y = 1000, 1000

            self.stage = 'stage_2'
        
        screen.fill((0, 0, 0))
        collision_rect_lv1()
        walls_stage_5()
        screen.blit(stage_lol,(0, 0))
        
        p1.draw(screen)
        p2.draw(screen)
        p3.draw(screen)
        s1.draw(screen)
        m1.draw(screen)
        f1.draw(screen)
        d1.draw(screen)
        d2.draw(screen)
        
        screen.blit(lol_eraser, (0,422,393,86))

        game_font_18.render_to(screen, (18,639), f'MORTES: {health_player}', (0,0,0))
        
        self.anim_p_lv1()

        
            
    def level_2(self):
        global jumpCount, isJumping, health_player

        can_jump = False

        if player_lv1.colliderect(jump_on_1_1):
            can_jump = True
        if player_lv1.colliderect(jump_on_2_1):
            can_jump = True
        if player_lv1.colliderect(jump_on_3_1):
            can_jump = True
        if player_lv1.colliderect(jump_on_4_1):
            can_jump = True
        if player_lv1.colliderect(jump_on_5_1):
            can_jump = True
        if player_lv1.colliderect(jump_on_6_1):
            can_jump = True
        if player_lv1.colliderect(jump_on_7_1):
            can_jump = True

        event_chest_LV2 = False
        if player_lv1.colliderect(chest_LV2):
            event_chest_LV2 = True

        keys = py.key.get_pressed()
        if keys[py.K_a]:
            player_lv1.x -= vel + 3
            self.left = True
            self.right = False
        elif keys[py.K_d]:
            player_lv1.x += vel + 3
            self.left = False
            self.right = True
        else:
            self.right = False
            self.left = False
            
        if not(isJumping):
            player_lv1.y += 11
            if can_jump:
                if keys[py.K_SPACE]:
                    isJumping = True
                    self.left = False
                    self.right = False
        else:
            if jumpCount >= -1:
                player_lv1.y -= (jumpCount ** 2) * 0.3 * 1
                jumpCount -= 1
            else:
                jumpCount = 11
                isJumping = False

        if keys[py.K_e] and event_chest_LV2:
            chest.play()
            time.sleep(2.5)
            self.unblock_2 = True
            LV_2.x, LV_2.y = 1000, 1000
            player_1.x, player_1.y = 542, 305

            jump_on_1_1.x, jump_on_1_1.y = 1000,1000
            jump_on_2_1.x, jump_on_2_1.y = 1000,1000
            jump_on_3_1.x, jump_on_3_1.y = 1000,1000
            jump_on_4_1.x, jump_on_4_1.y = 1000,1000
            jump_on_5_1.x, jump_on_5_1.y = 1000,1000
            jump_on_6_1.x, jump_on_6_1.y = 1000,1000
            jump_on_7_1.x, jump_on_7_1.y = 1000,1000

            self.stage = 'stage_2'
            
        
        if player_lv1.colliderect(plataform_lv2):
            if abs(plataform_lv2.top - player_lv1.bottom) < 15:
                player_lv1.y -= 11
            


        screen.fill((0, 0, 0))
        collision_rect_lv1()
        walls_stage_4() 
        #py.draw.rect(screen, (255,0,0), plataform_lv2, 1)
        screen.blit(stage_baidu,(0, 0))
        plataformm.draw(screen)
        v1.draw(screen)
        v2.draw(screen)
        v3.draw(screen)
        v4.draw(screen)
        self.anim_p_lv1()

        if player_lv1.colliderect(virus_1):
            if abs(virus_1.top - player_lv1.bottom) < 15:
                print('Vírus morre')
                pop.play()
                virus_1.y = 1000
                player_lv1.y -= 11
            if abs(virus_1.bottom - player_lv1.top) < 15:
                print('Voce morreu')
                death_player.play()
                player_lv1.y += 11
                player_lv1.x, player_lv1.y = 413,605
                health_player += 1
            if abs(virus_1.right - player_lv1.left) < 15:
                print('Voce morreu')
                death_player.play()
                player_lv1.x += 11
                player_lv1.x, player_lv1.y = 413,605
                health_player += 1
            if abs(virus_1.left - player_lv1.right) < 15:
                print('Voce morreu')
                death_player.play()
                player_lv1.x -= 11
                player_lv1.x, player_lv1.y = 413,605
                health_player += 1

        if player_lv1.colliderect(virus_2):
            if abs(virus_2.top - player_lv1.bottom) < 15:
                print('Vírus morre')
                pop.play()
                virus_2.x = 1000
                player_lv1.y -= 11
            if abs(virus_2.bottom - player_lv1.top) < 15:
                print('Voce morreu')
                death_player.play()
                player_lv1.y += 11
                player_lv1.x, player_lv1.y = 413,605
                health_player += 1
            if abs(virus_2.right - player_lv1.left) < 15:
                print('Voce morreu')
                death_player.play()
                player_lv1.x += 11
                player_lv1.x, player_lv1.y = 413,605
                health_player += 1
            if abs(virus_2.left - player_lv1.right) < 15:
                print('Voce morreu')
                death_player.play()
                player_lv1.x -= 11
                player_lv1.x, player_lv1.y = 413,605
                health_player += 1

        if player_lv1.colliderect(virus_3):
            if abs(virus_3.top - player_lv1.bottom) < 15:
                print('Vírus morre')
                pop.play()
                virus_3.y = 100000
                virus_3.x = 100000
                player_lv1.y -= 11
            if abs(virus_3.bottom - player_lv1.top) < 15:
                print('Voce morreu')
                death_player.play()
                player_lv1.y += 11
                player_lv1.x, player_lv1.y = 413,605
                health_player += 1
            if abs(virus_3.right - player_lv1.left) < 15:
                print('Voce morreu')
                death_player.play()
                player_lv1.x += 11
                player_lv1.x, player_lv1.y = 413,605
                health_player += 1
            if abs(virus_3.left - player_lv1.right) < 15:
                print('Voce morreu')
                death_player.play()
                player_lv1.x -= 11
                player_lv1.x, player_lv1.y = 413,605
                health_player += 1
                health_player += 1
        if player_lv1.colliderect(virus_4):
            if abs(virus_4.top - player_lv1.bottom) < 15:
                print('Vírus morre')
                pop.play()
                virus_4.y = 1000
                virus_4.x = 1000
                player_lv1.y -= 11
            if abs(virus_4.bottom - player_lv1.top) < 15:
                print('Voce morreu')
                death_player.play()
                player_lv1.y += 11
                player_lv1.x, player_lv1.y = 413,605
                health_player += 1
            if abs(virus_4.right - player_lv1.left) < 15:
                print('Voce morreu')
                death_player.play()
                player_lv1.x += 11
                player_lv1.x, player_lv1.y = 413,605
                health_player += 1
            if abs(virus_4.left - player_lv1.right) < 15:
                print('Voce morreu')
                death_player.play()
                player_lv1.x -= 11
                player_lv1.x, player_lv1.y = 413,605
                health_player += 1

        game_font_18.render_to(screen, (400,10), f'MORTES: {health_player}', (0,0,0))   

    def level_1(self):
        global jumpCount, isJumping, health_player

        can_jump = False

        if player_lv1.colliderect(jump_on_1):
            can_jump = True
        if player_lv1.colliderect(jump_on_2):
            can_jump = True
        if player_lv1.colliderect(jump_on_3):
            can_jump = True
        if player_lv1.colliderect(jump_on_4):
            can_jump = True
        if player_lv1.colliderect(jump_on_5):
            can_jump = True
        if player_lv1.colliderect(jump_on_6):
            can_jump = True
        if player_lv1.colliderect(jump_on_7):
            can_jump = True
        

        event_chest_LV1 = False
        if player_lv1.colliderect(chest_LV1):
            event_chest_LV1 = True

        keys = py.key.get_pressed()
        if keys[py.K_a]:
            player_lv1.x -= vel + 3
            self.left = True
            self.right = False
        elif keys[py.K_d]:
            player_lv1.x += vel + 3
            self.left = False
            self.right = True
        else:
            self.right = False
            self.left = False
        if not(isJumping):
            player_lv1.y += 11
            if can_jump:
                if keys[py.K_SPACE]:
                    isJumping = True
                    self.right = False
                    self.left = False
        else:
            if jumpCount >= -1:
                player_lv1.y -= (jumpCount ** 2) * 0.3 * 1
                jumpCount -= 1
            else:
                jumpCount = 10
                isJumping = False
        if keys[py.K_e] and event_chest_LV1:
            self.unblock_1 = True
            player_1.x, player_1.y = 715,103
            chest.play()
            time.sleep(2.5)
            chest.stop()

            jump_on_1.x, jump_on_1.y = 1000,1000
            jump_on_2.x, jump_on_2.y = 1000,1000
            jump_on_3.x, jump_on_3.y = 1000,1000
            jump_on_4.x, jump_on_4.y = 1000,1000
            jump_on_5.x, jump_on_5.y = 1000,1000
            jump_on_6.x, jump_on_6.y = 1000,1000
            jump_on_7.x, jump_on_7.y = 1000,1000

            self.stage = 'stage_2'

        screen.fill((0, 0, 0))
        collision_rect_lv1()
        walls_stage_3()        
        screen.blit(stage_google,(0, 0))
        dino.draw(screen)
        dino_2.draw(screen)
        dino_3.draw(screen)
        dino_4.draw(screen)

        self.anim_p_lv1()
        #screen.blit(stand, (player_lv1.x, player_lv1.y))

        

        if player_lv1.colliderect(dino_rect):
            if abs(dino_rect.top - player_lv1.bottom) < 15:
                print('Dino morre')
                pop.play()
                dino_rect.y = 1000
            if abs(dino_rect.bottom - player_lv1.top) < 15:
                print('1 hit')
                death_player.play()
                health_player += 1
                player_lv1.x, player_lv1.y = 413,605
            if abs(dino_rect.right - player_lv1.left) < 15:
                print('1 hit')
                death_player.play()
                health_player += 1
                player_lv1.x, player_lv1.y = 413,605
            if abs(dino_rect.left - player_lv1.right) < 15:
                print('1 hit')
                death_player.play()
                health_player += 1
                player_lv1.x, player_lv1.y = 413,605
                

        if player_lv1.colliderect(dino_rect_2):
            if abs(dino_rect_2.top - player_lv1.bottom) < 15:
                print('Dino morre')
                pop.play()
                dino_rect_2.y = 1000
            if abs(dino_rect_2.bottom - player_lv1.top) < 15:
                print('1 hit')
                death_player.play()
                health_player += 1
                player_lv1.x, player_lv1.y = 413,605
                
            if abs(dino_rect_2.right - player_lv1.left) < 15:
                print('1 hit')
                death_player.play()
                health_player += 1
                player_lv1.x, player_lv1.y = 413,605
                
            if abs(dino_rect_2.left - player_lv1.right) < 15:
                print('1 hit')
                death_player.play()
                health_player += 1
                player_lv1.x, player_lv1.y = 413,605
                

        if player_lv1.colliderect(dino_rect_3):
            if abs(dino_rect_3.top - player_lv1.bottom) < 15:
                print('Dino morre')
                pop.play()
                dino_rect_3.y = 1000
            if abs(dino_rect_3.bottom - player_lv1.top) < 15:
                print('1 hit')
                death_player.play()
                health_player += 1
                player_lv1.x, player_lv1.y = 413,605
                
            if abs(dino_rect_3.right - player_lv1.left) < 15:
                print('1 hit')
                death_player.play()
                health_player += 1
                player_lv1.x, player_lv1.y = 413,605
                
            if abs(dino_rect_3.left - player_lv1.right) < 15:
                print('1 hit')
                death_player.play()
                health_player += 1
                player_lv1.x, player_lv1.y = 413,605
                

        if player_lv1.colliderect(dino_rect_4):
            if abs(dino_rect_4.top - player_lv1.bottom) < 15:
                print('Dino morre')
                pop.play()
                dino_rect_4.y = 1000
            if abs(dino_rect_2.bottom - player_lv1.top) < 15:
                print('1 hit')
                death_player.play()
                health_player += 1
                player_lv1.x, player_lv1.y = 413,605
                
            if abs(dino_rect_4.right - player_lv1.left) < 15:
                print('1 hit')
                death_player.play()
                health_player += 1
                player_lv1.x, player_lv1.y = 413,605
                
            if abs(dino_rect_4.left - player_lv1.right) < 15:
                print('1 hit')
                death_player.play()
                health_player += 1
                player_lv1.x, player_lv1.y = 413,605
                
        game_font_18.render_to(screen, (15,60), f'MORTES: {health_player}', (0,0,0))
        py.display.update()

    def stage_2(self):
        global time_s5, ok, teste_go1


        event_lv1 = False
        event_lv2 = False
        event_lv3 = False
        event_lv4 = False


        if player_1.colliderect(LV_1):
            event_lv1 = True

        if player_1.colliderect(LV_2):
            event_lv2 = True
        
        if player_1.colliderect(LV_3):
            event_lv3 = True

        if player_1.colliderect(LV_4):
            event_lv4 = True
        
        if player_1.colliderect(block_1):
            if abs(block_1.top - player_1.bottom) < 10:
                player_1.y -= 5
        if player_1.colliderect(block_2):
            if abs(block_2.top - player_1.bottom) < 20:
                player_1.y -= 5
            if abs(block_2.right - player_1.left) < 10:
                player_1.x += 5 
        if player_1.colliderect(block_3):
            if abs(block_3.top - player_1.bottom) < 10:
                player_1.y -= 5  
            


        keys = py.key.get_pressed()
        if keys[py.K_w]:
            player_1.y -= vel
            self.left = False
            self.right = False
            self.up = True
            self.down = False
        elif keys[py.K_s]:
            player_1.y += vel
            self.left = False
            self.right = False
            self.up = False
            self.down = True
        elif keys[py.K_a]:
            player_1.x -= vel
            self.left = True
            self.right = False
            self.up = False
            self.down = False
        elif keys[py.K_d]:
            player_1.x += vel
            self.left = False
            self.right = True
            self.up = False
            self.down = False
        else:
            self.left = False
            self.right = False
            self.up = False
            self.down = False

        if keys[py.K_e] and event_lv1:
            print('Level 1')
            self.stage = 'level_1'
            appear.play()
        if keys[py.K_e] and event_lv2:
            print('Level 2')
            self.stage = 'level_2'
            appear.play()
            player_lv1.x, player_lv1.y = 427, 609
        if keys[py.K_e] and event_lv3:
            player_lv1.x, player_lv1.y = 10, 510
            print('Level 3')
            self.stage = 'level_3'
            appear.play()
        if keys[py.K_e] and event_lv4:
            player_lv1.x, player_lv1.y = 10, 510
            print('Level 4')
            self.stage = 'level_4'
            appear.play()
                    
        screen.fill((0, 0, 0))
        walls_stage_2()
        collision_rect_st2()
        screen.blit(stage_2,(0, 0))

        if self.unblock_1:
            LV_1.x, LV_1.y = 1000,1000
            block_1.x, block_1.y = 1000,1000
            screen.blit(eraser_blue, (699, 200))
            screen.blit(google_dirty, (727, 121))
        
        if self.unblock_2:
            block_2.x, block_2.y = 1000, 1000
            screen.blit(eraser_blue, (429, 537))
            screen.blit(baidu_dirty, (546, 320))

        if self.unblock_3:
            LV_3.x, LV_3.y = 1000,1000
            block_3.x, block_3.y = 1000,1000
            screen.blit(eraser_blue, (140, 117))
            screen.blit(lol_dirty, (394, 35))

        self.anim_p_normal_st2()

    def stage_1(self):
        global next_phrase, reset1, call_end, call_end2, anwser_now, can_go_chair, can_anwser_phone, time_s, time_s1, teste_go, light_on, go_on, dont_move, stop_anim, time_s2, call_boss, call_finished
        event_chair = False
 
        
        walls_stage_1()
        collision_rect_st1()

        if self.count + 1 >= 27:
            self.count = 0
        

        if can_go_chair > 0:
            anwser_now = False
            if player.colliderect(chairP):
                event_chair = True

        keys = py.key.get_pressed()
        if not dont_move:
            if keys[py.K_w]:
                player.y -= vel
                self.left = False
                self.right = False
                self.up = True
                self.down = False
            elif keys[py.K_s]:
                player.y += vel
                self.left = False
                self.right = False
                self.up = False
                self.down = True
            elif keys[py.K_a]:
                player.x -= vel
                self.left = True
                self.right = False
                self.up = False
                self.down = False
            elif keys[py.K_d]:
                player.x += vel
                self.left = False
                self.right = True
                self.up = False
                self.down = False
            else:
                self.left = False
                self.right = False
                self.up = False
                self.down = False

        if light_on:
            if player.colliderect(start_ring):
                if abs(player.right - start_ring.left) < 15:
                    can_anwser_phone += 1
                    player.x -= 5
                    start_ring.y = 3000
                    ring.play(-1)
                    
                
        if can_anwser_phone > 0:
            if player.colliderect(answer_phone):
                anwser_now = True
        
        if keys[py.K_e] and anwser_now:
            call_boss = True
        
        if player.colliderect(switch_light):
            if keys[py.K_e]:
                light_on = True
                click_switch.play()
                time.sleep(0.1)

        screen.blit(stage_1_off, (0,0))

        #--------------Texts-------------------#
        #-----Lights off-------#
        if not light_on:
            if not reset1:
                if time_s > 1 and time_s < 3:
                    next_phrase += 1
                if time_s > 100 and time_s < 102:
                     next_phrase += 1
                if time_s > 200 and time_s < 202:
                     next_phrase += 1
                if time_s > 300 and time_s < 302:
                     next_phrase += 1
                

                if time_s > 55 and next_phrase == 1:
                    screen.blit(set_self_talk, (player.x - 150 ,player.y - 100))
                    game_font_16.render_to(screen, (player.x - 60, player.y - 80), 'Que escuridao...', (0,0,0))
                if time_s > 150 and next_phrase == 2:
                    screen.blit(set_self_talk, (player.x - 150 ,player.y - 100))
                    game_font_16.render_to(screen, (player.x - 135, player.y - 80), 'Preciso achar o interruptor !', (0,0,0))
                if time_s > 250 and next_phrase == 3:
                    screen.blit(set_self_talk, (player.x - 150 ,player.y - 100))
                    game_font_16.render_to(screen, (player.x - 137, player.y - 80), 'Acho que fica do lado da porta', (0,0,0))
                if time_s > 350 and next_phrase == 4:
                    screen.blit(set_self_talk, (player.x - 150 ,player.y - 100))
                    game_font_16.render_to(screen, (player.x - 100, player.y - 80), 'Essa tecla [ E ] funciona ?', (0,0,0))
                if time_s > 400:
                    reset1 = True
           
                if time_s > 2000:
                    light_on = True
            #---------Call Phone-------#
        global after_light_on, time_s2, time_s3, next_phrase_1, n1, n2, time_s4
        if light_on:
            screen.blit(stage_1_on, (0,0))
            after_light_on = True

        if call_end2:
            argue.play(-1)

        if call_end:
            dial.play(-1)

        g_font_call_x = 96
        g_font_call_y = 94

        

        if after_light_on:
            time_s3 += 1
            if time_s3 > 1 and time_s3 < 3:
                next_phrase_1 += 1
            if time_s3 > 50 and time_s3 < 52:
                next_phrase_1 += 1
            if time_s3 > 160 and time_s3 < 162:
                next_phrase_1 += 1
                screen.blit(set_self_talk, (player.x - 150 ,player.y - 100))
            if time_s3 > 5 and next_phrase_1 == 1:
                screen.blit(set_self_talk, (player.x - 150 ,player.y - 100))
                game_font_16.render_to(screen, (player.x - 60, player.y - 80), 'Bem melhor agora!', (0,0,0))
            if time_s3 > 100 and next_phrase_1 == 2:
                screen.blit(set_self_talk, (player.x - 150 ,player.y - 100))
                game_font_16.render_to(screen, (player.x - 146, player.y - 80), 'Tenho que olhar essa papelada', (0,0,0))    
            if time_s3 > 200 and next_phrase_1 == 3 and can_anwser_phone:
                
                game_font_16.render_to(screen, (player.x - 110, player.y - 80), 'Melhor eu atender agora !', (0,0,0))
            if  time_s3 > 400:
                screen.blit(chair,(550, 193))
                next_phrase_1 += 1
                after_light_on = False
            if time_s3 > 500 and n2:
                screen.blit(set_self_talk, (player.x - 150 ,player.y - 100))
                game_font_16.render_to(screen, (player.x - 105, player.y - 80), 'Vamos lá resolver então...', (0,0,0))
                time_s4 += 1
                if time_s4 > 100:
                    screen.blit(stage_1_on, (0,0))
                
                    
        print(n2)
        
        if call_boss:
            screen.blit(stage_1_on, (0,0))
            answer_phone.x = 1000
            dont_move = True
            time_s2 += 1
            ring.stop()
            can_go_chair += 1
            screen.blit(set_boss_talk, (20,60))
            if time_s2 > 1:
                call_end2 = True
            if time_s2 > 2:
                call_end2 = False
                game_font.render_to(screen, (g_font_call_x, g_font_call_y), '[CHEFE] : Entao, preciso que resolva um codigo para mim', (0,0,0))
            if time_s2 > 80:       
                game_font.render_to(screen, (g_font_call_x, g_font_call_y + 20), '[CHEFE] : Ninguem aqui na empresa consegue resolver', (0,0,0))
            if time_s2 > 150:                  
                game_font.render_to(screen, (g_font_call_x, g_font_call_y + 40), '[CHEFE] : Preciso que voce faca isso agora ! certo ? ', (0,0,0))
            if time_s2 > 220:                  
                game_font.render_to(screen, (g_font_call_x, g_font_call_y + 65), '                 Tudo bem chefe, pode deixar que eu resolvo : [EU]', (0,0,156))
            if time_s2 > 290:
                game_font.render_to(screen, (g_font_call_x, g_font_call_y + 90), '[CHEFE] : Muito bem entao, ja mandei para seu e-mail', (0,0,0))
            if time_s2 > 360:
                game_font.render_to(screen, (g_font_call_x, g_font_call_y + 115), '                                                            O que esse codigo faz ??: [EU]', (0,0,156))
            if time_s2 > 390:
                argue.stop()
                game_font.render_to(screen, (g_font_call_x, g_font_call_y + 140), '                    [LIGACAO ENCERRADA]', (255,0,0))
                call_end = True
                if time_s2 > 391:
                    call_end = False
            if time_s2 > 450:
                dont_move = False
                dial.stop()
                screen.blit(stage_1_on, (0,0))
                call_boss = False
                n2 = True

        screen.blit(chair,(550, 193))
        time_s += 1
        
        if time_s >= 13.5:
            teste_go = False

        if teste_go:
            screen.blit(fullBlack[self.count//3], (-550, -550))
            self.count += 2

        if player.colliderect(chairP) and event_chair:
            if keys[py.K_e]:
                go_on = True
                dont_move = True

        self.anim_p_normal_st1()
        if self.count >= 27:
            stop_anim = False

        if go_on:
            time_s1 += 1
            if time_s1 > 1 and time_s1 < 3:
                typing.play()
            if time_s1 > 120 and time_s1 < 122:
                typing.stop()
                spark.play()
            if time_s1 > 160 and time_s1 < 162:
                spark.stop()
                sucked.play()
            if time_s1 > 273:
                    player.x = 1000
                    if stop_anim:
                        screen.blit(sugado[self.count//3], (563, 138))
                    screen.blit(chair,(550, 193))
                    self.count += 1
            if time_s1 > 300 and time_s1 < 302:
                sucked.stop()
                print('Next stage')
                self.stage = 'stage_2'
                appear.play()
        

        py.display.flip()

          
        

        #Arrumar problema da animação do player!
        

        
py.init()
clock = py.time.Clock()
screen_width, screen_height = 800, 700
screen = py.display.set_mode((screen_width, screen_height))
t = timing()
#general setup
game_stage = GameStages()

chairP = py.Rect(568, 193, 30, 30)

#-----------Stage 2---------------#
LV_1 = py.Rect(728,122,30,30)
block_1 = py.Rect(691,215,90,5)
chest_LV1 = py.Rect(671,52,30,40)

LV_2 = py.Rect(551, 324, 30, 30)
block_2 = py.Rect(434, 557, 80, 60)
chest_LV2 = py.Rect(743,80,30,40)

LV_3 = py.Rect(394, 36, 40, 40)
block_3 = py.Rect(146, 134, 60,40)
chest_LV3 = py.Rect(90,65,30,40)

LV_4 = py.Rect(162,553,40,40)


player = py.Rect(230, 129, 35, 60)
player_1 = py.Rect(553,110,35,60)
player_lv1 = py.Rect(413,605,35,60)

vel = 5
#------------Level 1--------------#
#------------Enemies--------------#
dino = enemy(80, 436, 64, 64, 300)      #(X, Y, W, H, End)
dino_rect = py.Rect(80, 440, 50, 10)    #(X, Y, W, H)

dino_2 = enemy2(480, 508, 64, 64, 720)
dino_rect_2 = py.Rect(480, 519, 50, 10)

dino_3 = enemy3(412, 308, 64, 64, 650)
dino_rect_3 = py.Rect(412, 328, 50, 10)

dino_4 = enemy4(2, 180, 64, 64, 300)
dino_rect_4 = py.Rect(2, 193, 50, 10)
#---------Can Jump Level 1---------#
jump_on_1 = py.Rect(0,666,800,1)
jump_on_2 = py.Rect(468,553,800,1)
jump_on_3 = py.Rect(79,476,254,1)
jump_on_4 = py.Rect(407,359,294,1)
jump_on_5 = py.Rect(0,229,347,1)
jump_on_6 = py.Rect(426,124,153,1)
jump_on_7 = py.Rect(629,84,170,1)
#------------Level 2--------------#
#------------Enemies--------------#
plataformm = plataformV2(100, 345, 64, 64, 420)
plataform_lv2 = py.Rect(112, 345, 300, 1)

v1 = virus1(6, 600)
virus_1 = py.Rect(6, 616 ,50 , 10)

v2 = virus2(639, 14, 400)
virus_2 = py.Rect(639, 30, 50, 10)

v3 = virus3(3, 168, 150)
virus_3 = py.Rect(3, 168, 50, 10)

v4 = virus4(200, 620)
virus_4 = py.Rect(200, 215, 100, 100)
#---------Can Jump Level 2---------#
jump_on_1_1 = py.Rect(0,650,800,1)
jump_on_2_1 = py.Rect(303,530,290,1)
jump_on_3_1 = py.Rect(620,436,300,1)
jump_on_4_1 = py.Rect(127,316,582,1)
jump_on_5_1 = py.Rect(0,201,201,1)
jump_on_6_1 = py.Rect(239,92,370,1)
jump_on_7_1 = py.Rect(713,93,170,1)
#------------Level 3--------------#
#------------Enemies--------------#
p1 = plat1(332,600)
plat_1 = py.Rect(692,332,101,1)

p2 = plat2(10, 600)
plat_2 = py.Rect(692,10,101,1)

p3 = plat3(270, 400)
plat_3 = py.Rect(527,270,85,1)

s1 = serra(236, 450)
serra_rect = py.Rect(236,238,10,13)

m1 = minion1(170, 580)
minion_1 = py.Rect(170,20,40,60)

minion_2 = py.Rect(590, 580, 40,60)
f1 = fireball(563, 800)

fire_ball_1 = py.Rect(563,596,10,10)
fire_ball_2 = py.Rect(563,596,10,10)
fire_ball_3 = py.Rect(563,596,10,10)
fire_ball_4 = py.Rect(563,596,10,10)
fire_ball_5 = py.Rect(563,596,10,10)

fire_ball_6 = py.Rect(300,400,10,10)
fire_ball_7 = py.Rect(300,400,10,10)
fire_ball_8 = py.Rect(300,400,10,10)
fire_ball_9 = py.Rect(300,400,10,10)
fire_ball_10 = py.Rect(300,400,10,10)

alavanca1 = py.Rect(463,366,30,50)
door_rect_1 = py.Rect(130,95,41,167)
d1 = door1(130, 300)

alavanca2 = py.Rect(377,366,30,50)
door_rect_2 = py.Rect(1,446,65,1)
d2 = door2(100,440)

bug_fix = py.Rect(60,526,10,10)
#---------Can Jump Level 3---------#
jump_on_1_2 = py.Rect(0,620,800,1)
jump_on_2_2 = py.Rect(0,50,60,1)
jump_on_3_2 = py.Rect(620,0,300,700)
jump_on_4_2 = py.Rect(637,273,100,1)
jump_on_5_2 = py.Rect(232,86,400,1)
jump_on_6_2 = py.Rect(323,148,210,1)
jump_on_7_2 = py.Rect(130,242,395,1)
jump_on_8_2 = py.Rect(530,248,100,170)
jump_on_9_2 = py.Rect(464,403,200,1)
jump_on_10_2 = py.Rect(0,422,600,1)
jump_on_11_2 = py.Rect(0,84,128,1)
#------------Phone---------------#
start_ring = py.Rect(480,192,1,700)
answer_phone = py.Rect(166,509,5,5)

anwser_now = False
can_go_chair = 0
can_anwser_phone = 0

light_on = False
switch_light = py.Rect(300,140,10,10)

teste_go = True
teste_go1 = True
go_on = False
time_s = 0
time_s1 = 0
time_s2 = 0
time_s3 = 0
time_s4 = 0
time_s5 = 0

next_phrase = 0
next_phrase_1 = 0
after_light_on = False
n1 = 0
n2 = False
ok = True


time_s2 = 0
reset1 = False
call_boss = False
call_finished = False
call_end = False
call_end2 = False

dont_move = False
stop_anim = True
#------------Level 4--------------#
red_buttom = py.Rect(649,234,10,10)
window_rect = py.Rect(384,156,157,70)

grade_rect = py.Rect(93,159,79,55)

window_slide_up = False
window_slide_up_ok = False
can_open_grade = False
liberar = False

v1 = slideWindow(158,500)
g1 = gradeUp(500)

del_player = False

time_a2 = 0
#------------Time fight----------#
time_fight = False
time_a3 = 0
time_a4 = 864
time__ = 0

lazer1_rect = py.Rect(-500,500,300,30)
lazer1_rect_2 = py.Rect(-500,500,300,30)
l1 = Lazer1(800)
l2 = Lazer2(800)

next_level = 0
reset_to_0 = False

#------------Config--------------#
health_player = 0

isJumping = False
jumpCount = 10

left = False
right = False
walkCount = 0

#----------Tela de Menu----------#
jogar = py.Rect(204,298,398,105)
comandos = py.Rect(204,431,398,105)
sair = py.Rect(204,564,398,105)
voltar = py.Rect(28,24,200,77)


while True:
    clock.tick(27)
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

    if event.type == py.MOUSEBUTTONDOWN:
        Mouse_x, Mouse_y = py.mouse.get_pos()
        print('X:',Mouse_x,'| y:',Mouse_y)


    current_time = py.time.get_ticks()     
    game_stage.stage_manager()
    py.display.update()
