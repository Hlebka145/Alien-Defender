import pygame
import sys
import random

pygame.init()
pygame.display.set_caption('Alien Defender')

width, height = 500, 700

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Lucida Sans Unicode', 30)

class Player:
    def __init__(self, x, y, w, h, img_path, hp):
        self.rect = pygame.Rect(x, y, w, h)
        self.img = pygame.transform.scale(pygame.image.load(img_path), (w, h))
        self.hp = hp
        self.speed = 0
    
    def move(self):
        self.rect.x += self.speed
        if self.rect.x <= 0 or self.rect.x >= 440:
            self.rect.x -= self.speed

    def draw(self):
        screen.blit(self.img, self.rect)

class Enemy:
    def __init__(self, x, y, w, h, img_path, hp, money):
        self.rect = pygame.Rect(x, y, w, h)
        self.img_path = img_path
        self.img = pygame.transform.scale(pygame.image.load(img_path), (w, h))
        self.shoot_g = 0
        self.hp = hp
        self.tick = 0
        self.down_tick = 0
        self.move_switch = 1
        self.switch = 0
        self.money = money
        self.group = random.randint(0, 20)

    def move(self):
        if self.tick == 60:
            self.rect.x += (5 * self.move_switch)
            self.down_tick += 1
            self.tick = 0
            self.switch = 1
            self.shoot_g += 1
            if self.shoot_g == 21:
                self.shoot_g = 0
        if self.down_tick == 3 and self.tick == 30:
            self.move_switch *= -1
            self.rect.y += 16
            self.down_tick = 0
        for i in range(0, 20):
            if self.shoot_g == i and self.group == i and self.switch == 1:
                self.shoot()
        
    def shoot(self):
        if self.img_path == 'Easy Code/projects/project4/img/Enemy1.png':
            bullet = Bullet(self.rect.centerx - 4, self.rect.centery, 8, 16, 'Easy Code/projects/project4/img/E1bullet.png', 3, 5, 'e')
        elif self.img_path == 'Easy Code/projects/project4/img/Enemy2.png':
            bullet = Bullet(self.rect.centerx - 4, self.rect.centery, 8, 16, 'Easy Code/projects/project4/img/E2bullet.png', 3, 10, 'e')
        elif self.img_path == 'Easy Code/projects/project4/img/Enemy3.png':
            bullet = Bullet(self.rect.centerx - 4, self.rect.centery, 8, 16, 'Easy Code/projects/project4/img/E3bullet.png', 3, 15, 'e')
        bullets.append(bullet)
        self.switch = 0

    def draw(self):
        screen.blit(self.img, self.rect)

class Boss:
    def __init__(self, x, y, w, h, img_path, hp):
        self.rect = pygame.Rect(x, y, w, h)
        self.img = pygame.transform.scale(pygame.image.load(img_path), (w, h))
        self.hp = hp
        self.tick = 0
        self.down_tick = 9
        self.move_switch = 1

    def move(self):
        if self.tick % 60 == 0 and self.tick >= 60:
            self.rect.x += (15 * self.move_switch)
            self.down_tick += 1
        if self.tick % 60 == 0 and self.tick >= 60 and self.down_tick % 3 == 0 and self.down_tick >= 3:
            self.shoot()
        if self.down_tick == 18 and self.tick % 30 == 0 and self.tick >= 30:
            self.move_switch *= -1
            self.down_tick = 0
            self.tick = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx - 8, self.rect.centery, 16, 32, 'Easy Code/projects/project4/img/Bbullet.png', 3, 20, 'e')
        bullets.append(bullet)
        bullet = Bullet(self.rect.centerx - 58, self.rect.centery, 8, 16, 'Easy Code/projects/project4/img/Bbullet.png', 3, 10, 'e')
        bullets.append(bullet)
        bullet = Bullet(self.rect.centerx + 50, self.rect.centery, 8, 16, 'Easy Code/projects/project4/img/Bbullet.png', 3, 10, 'e')
        bullets.append(bullet)
        self.switch = 0

    def draw(self):
        screen.blit(self.img, self.rect)
    
class Bullet:
    def __init__(self, x, y, w, h, img_path, speed, dmg, type):
        self.rect = pygame.Rect(x, y, w, h)
        self.img = pygame.transform.scale(pygame.image.load(img_path), (w, h))
        self.speed = speed
        self.dmg = dmg
        self.type = type
    
    def move(self):
        self.rect.y += self.speed

    def draw(self):
        screen.blit(self.img, self.rect)
    
    def collide(self, obj):
        return self.rect.colliderect(obj.rect)

class Object:
    def __init__(self, x, y, w, h, img_path):
        self.rect = pygame.Rect(x, y, w, h)
        self.img = pygame.transform.scale(pygame.image.load(img_path), (w, h))
    
    def draw(self):
        screen.blit(self.img, self.rect)
    
player = Player(218, 628, 64, 32, 'Easy Code/projects/project4/img/Player.png', 100)
ammo_board = Object(5, 664, 144, 36, 'Easy Code/projects/project4/img/Ammo_board.png')
health_board = Object(351, 664, 144, 36, 'Easy Code/projects/project4/img/Hp_board.png')
boss_health_board = Object(46, 82, 408, 36, 'Easy Code/projects/project4/img/Boss_hp_board.png')
menu = Object(452, 0, 48, 48, 'Easy Code/projects/project4/img/Menu.jpg')
coin = Object(0, 0, 48, 48, 'Easy Code/projects/project4/img/Coin.png')
button1 = Object(370, 185, 96, 48, 'Easy Code/projects/project4/img/Buy.jpg')
button2 = Object(370, 285, 96, 48, 'Easy Code/projects/project4/img/Buy.jpg')
button3 = Object(370, 385, 96, 48, 'Easy Code/projects/project4/img/Buy.jpg')
button4 = Object(200, 595, 96, 48, 'Easy Code/projects/project4/img/Buy.jpg')
ammo_icon = Object(10, 175, 64, 64, 'Easy Code/projects/project4/img/Ammo_icon.png')
dmg_icon = Object(10, 275, 64, 64, 'Easy Code/projects/project4/img/Dmg_icon.png')
reload_icon = Object(10, 375, 64, 64, 'Easy Code/projects/project4/img/Reload_icon.png')
kit_icon = Object(10, 525, 64, 64, 'Easy Code/projects/project4/img/Kit_icon.png')
title = Object(109, 100, 282, 96, 'Easy Code/projects/project4/img/Title.png')
game_over = Object(169, 200, 162, 72, 'Easy Code/projects/project4/img/Game_over.png')
win = Object(199, 200, 102, 72, 'Easy Code/projects/project4/img/Win.png')
health_bar = pygame.Rect(354, 682, 135, 15)
boss_health = pygame.Rect(49, 100, 405, 15)
coins = 0
max_ammo = 8
reload_speed = 45
dmg = 6
coins_counter = font.render(f'{coins}', False, (225, 225, 0))
start_text = font.render('Нажмите SPACE, чтобы начать.', False, (225, 225, 225))
end_text1 = font.render('Нажмите SPACE, чтобы закрыть игру.', False, (225, 225, 225))
end_text2 = font.render('Поздравляем!', False, (225, 225, 225))
end_text3 = font.render('О нет!', False, (225, 225, 225))
pause_text1 = font.render('Игра на паузе.', False, (225, 225, 225))
pause_text2 = font.render('Магазин улучшений:', False, (225, 225, 225))
upgrade_text1 = font.render(f'Магазин патронов: {max_ammo}.', False, (225, 225, 225))
upgrade_text2 = font.render(f'Урон: {dmg}.', False, (225, 225, 225))
upgrade_text3 = font.render(f'Скорость перезарядки: {reload_speed}.', False, (225, 225, 225))
kit_text = font.render(f'Восстановите здоровье полностью!', False, (225, 225, 225))
bullets = []
lvl1_enemies = []
lvl2_enemies = []
lvl3_enemies = []
lvl4_enemies = []
boss = Boss(186, 200, 128, 64, 'Easy Code/projects/project4/img/Boss.png', 5000)
lvl4_enemies.append(boss)
ammo_list = []
ammo = 8
ammo_upgrade = 1
dmg_upgrade = 1
reload_upgrade = 1
upgrade1_price = 20
upgrade2_price = 50
upgrade3_price = 30
kit_price = 20
a = 0
x1 = 0
x2 = 2
x3 = 8
pflag = False
while a != 8:
    a += 1
    x1 += 16
    ammo_list.append(pygame.Rect(x1, 685, 12, 9))

with open('Easy Code/projects/project4/maps/Enemy_map1.txt', 'r') as map:
    row, col = 0, 0
    for line in map.read().split('\n'):
        x = list(line)
        col = 0
        for i in x:
            if i == '1':
                lvl1_enemies.append(Enemy(col * 34 + 6, row * 18 + 50, 32, 16, 'Easy Code/projects/project4/img/Enemy1.png', 6, 1))
            elif i == '2':
                lvl1_enemies.append(Enemy(col * 34 + 6, row * 18 + 50, 32, 16, 'Easy Code/projects/project4/img/Enemy2.png', 12, 2))
            elif i == '3':
                lvl1_enemies.append(Enemy(col * 34 + 6, row * 18 + 50, 32, 16, 'Easy Code/projects/project4/img/Enemy3.png', 24, 4))
            col += 1
        row += 1

with open('Easy Code/projects/project4/maps/Enemy_map2.txt', 'r') as map:
    row, col = 0, 0
    for line in map.read().split('\n'):
        x = list(line)
        col = 0
        for i in x:
            if i == '1':
                lvl2_enemies.append(Enemy(col * 34 + 6, row * 18 + 50, 32, 16, 'Easy Code/projects/project4/img/Enemy1.png', 6, 1))
            elif i == '2':
                lvl2_enemies.append(Enemy(col * 34 + 6, row * 18 + 50, 32, 16, 'Easy Code/projects/project4/img/Enemy2.png', 12, 2))
            elif i == '3':
                lvl2_enemies.append(Enemy(col * 34 + 6, row * 18 + 50, 32, 16, 'Easy Code/projects/project4/img/Enemy3.png', 24, 4))
            col += 1
        row += 1

with open('Easy Code/projects/project4/maps/Enemy_map3.txt', 'r') as map:
    row, col = 0, 0
    for line in map.read().split('\n'):
        x = list(line)
        col = 0
        for i in x:
            if i == '1':
                lvl3_enemies.append(Enemy(col * 34 + 6, row * 18 + 50, 32, 16, 'Easy Code/projects/project4/img/Enemy1.png', 6, 1))
            elif i == '2':
                lvl3_enemies.append(Enemy(col * 34 + 6, row * 18 + 50, 32, 16, 'Easy Code/projects/project4/img/Enemy2.png', 12, 2))
            elif i == '3':
                lvl3_enemies.append(Enemy(col * 34 + 6, row * 18 + 50, 32, 16, 'Easy Code/projects/project4/img/Enemy3.png', 24, 4))
            col += 1
        row += 1

game_state = 0
level = 0
level_text = font.render(f'Level: {level}', False, (225, 225, 225))
tick = 0
tick1 = 0
tick2 = 0

while True:
    screen.fill((0, 0, 0))
    if game_state == 0:
        level_text = font.render(f'Level: {level}', False, (225, 225, 225))
        if level == 0:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_SPACE:
                        level = 1
            screen.blit(start_text, (100, 350))
            title.draw()
        elif level == 1 or level == 2 or level == 3 or level == 4:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_SPACE:
                        game_state = 1
                        ammo = 0
                        ammo_list = []
                        x1 = 0
                        x2 = 2
                        x3 = 8
            player.draw()
            ammo_board.draw()
            menu.draw()
            coin.draw()
            pygame.draw.rect(screen, (225, 0, 20), health_bar)
            health_board.draw()
            screen.blit(coins_counter, (58, 15))
            screen.blit(start_text, (100, 350))
            screen.blit(level_text, (215, 15))
        if level == 1:
            for enemy in lvl1_enemies:
                enemy.draw()
        elif level == 2:
            for enemy in lvl2_enemies:
                enemy.draw()
        elif level == 3:
            for enemy in lvl3_enemies:
                enemy.draw()
        elif level == 4:
            for enemy in lvl4_enemies:
                enemy.draw()
    elif game_state == 1:
        coins_counter = font.render(f'{coins}', False, (225, 225, 0))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT or e.key == pygame.K_a:
                    player.speed = -3
                elif e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                    player.speed = 3
                elif e.key == pygame.K_SPACE:
                    if ammo > 0:
                        for a in ammo_list:
                            if ammo_upgrade == 1:
                                if a.x == x1:
                                    ammo_list.remove(a)
                                    x1 -= 16
                            elif ammo_upgrade == 2:
                                if a.x == x2:
                                    ammo_list.remove(a)
                                    x2 -= 12
                            elif ammo_upgrade == 3:
                                if a.x == x3:
                                    ammo_list.remove(a)
                                    x3 -= 9
                        bullet = Bullet(player.rect.centerx - 4, player.rect.centery, 8, 16, 'Easy Code/projects/project4/img/Pbullet.png', -3, dmg, 'p')
                        bullets.append(bullet)
                        ammo -= 1
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT or e.key == pygame.K_a or e.key == pygame.K_d:
                    player.speed = 0
            elif e.type == pygame.MOUSEBUTTONDOWN:
                x, y = e.pos
                if menu.rect.x < x < menu.rect.right and menu.rect.y < y < menu.rect.bottom:
                    game_state = 2

        if level == 1:
            for bullet in bullets:
                bullet.move()
                bullet.draw()
                
            for bullet in bullets:
                if bullet.rect.y <= 0 or bullet.rect.y >= 700:
                    bullets.remove(bullet)
                    break
                
            for enemy in lvl1_enemies:
                enemy.tick += 1
                enemy.move()
                enemy.draw()
                if enemy.rect.bottom >= player.rect.top:
                    game_state = 3
                
            for enemy in lvl1_enemies:
                flag = False
                for bullet in bullets:
                    if bullet.collide(enemy) and bullet.type == 'p':
                        bullets.remove(bullet)
                        flag = True
                        break
                if flag:
                    enemy.hp -= bullet.dmg
                    if enemy.hp <= 0:
                        lvl1_enemies.remove(enemy)
                        coins += enemy.money
                        break
            
            for bullet in bullets:
                if bullet.collide(player) and bullet.type == 'e':
                    tick1 = 0
                    pflag = True
                    player.img = pygame.transform.scale(pygame.image.load('Easy Code/projects/project4/img/Player_inverted.png'), (64, 32))
                    player.hp -= bullet.dmg
                    health_bar.width -= (1.35 * bullet.dmg)
                    health_bar.x += (1.35 * bullet.dmg)
                    bullets.remove(bullet)
                    break

            if lvl1_enemies == []:
                tick = 0
                bullets = []
                level = 2
                game_state = 0
                player.rect.x = 218
                player.speed = 0
                ammo = 0
                ammo_list = []
                x1 = 0
                x2 = 2
                x3 = 8
    
        if level == 2:
            for bullet in bullets:
                    bullet.move()
                    bullet.draw()
                
            for bullet in bullets:
                if bullet.rect.y <= 0:
                    bullets.remove(bullet)
                    break
                
            for enemy in lvl2_enemies:
                enemy.tick += 1
                enemy.move()
                enemy.draw()
                if enemy.rect.bottom >= player.rect.top:
                    game_state = 3
            
            for enemy in lvl2_enemies:
                flag = False
                for bullet in bullets:
                    if bullet.collide(enemy) and bullet.type == 'p':
                        bullets.remove(bullet)
                        flag = True
                        break
                if flag:
                    enemy.hp -= bullet.dmg
                    if enemy.hp <= 0:
                        lvl2_enemies.remove(enemy)
                        coins += enemy.money
                        break

            for bullet in bullets:
                if bullet.collide(player) and bullet.type == 'e':
                    tick1 = 0
                    pflag = True
                    player.img = pygame.transform.scale(pygame.image.load('Easy Code/projects/project4/img/Player_inverted.png'), (64, 32))
                    player.hp -= bullet.dmg
                    health_bar.width -= (1.35 * bullet.dmg)
                    health_bar.x += (1.35 * bullet.dmg)
                    bullets.remove(bullet)
                    break
            
            if lvl2_enemies == []:
                tick = 0
                bullets = []
                level = 3
                game_state = 0
                player.rect.x = 218
                player.speed = 0
                ammo = 0
                ammo_list = []
                x1 = 0
                x2 = 2
                x3 = 8
        
        if level == 3:
            for bullet in bullets:
                    bullet.move()
                    bullet.draw()
                
            for bullet in bullets:
                if bullet.rect.y <= 0:
                    bullets.remove(bullet)
                    break
                
            for enemy in lvl3_enemies:
                enemy.tick += 1
                enemy.move()
                enemy.draw()
                if enemy.rect.bottom >= player.rect.top:
                    game_state = 3
            
            for enemy in lvl3_enemies:
                flag = False
                for bullet in bullets:
                    if bullet.collide(enemy) and bullet.type == 'p':
                        bullets.remove(bullet)
                        flag = True
                        break
                if flag:
                    enemy.hp -= bullet.dmg
                    if enemy.hp <= 0:
                        lvl3_enemies.remove(enemy)
                        coins += enemy.money
                        break

            for bullet in bullets:
                if bullet.collide(player) and bullet.type == 'e':
                    tick1 = 0
                    pflag = True
                    player.img = pygame.transform.scale(pygame.image.load('Easy Code/projects/project4/img/Player_inverted.png'), (64, 32))
                    player.hp -= bullet.dmg
                    health_bar.width -= (1.35 * bullet.dmg)
                    health_bar.x += (1.35 * bullet.dmg)
                    bullets.remove(bullet)
                    break
            
            if lvl3_enemies == []:
                tick = 0
                bullets = []
                level = 4
                game_state = 0
                player.rect.x = 218
                player.speed = 0
                ammo = 0
                ammo_list = []
                x1 = 0
                x2 = 2
                x3 = 8

        if level == 4:
            for bullet in bullets:
                    bullet.move()
                    bullet.draw()
                
            for bullet in bullets:
                if bullet.rect.y <= 0:
                    bullets.remove(bullet)
                    break
                
            for enemy in lvl4_enemies:
                enemy.tick += 1
                enemy.move()
                enemy.draw()
                if enemy.rect.bottom >= player.rect.top:
                    game_state = 3
            
            for enemy in lvl4_enemies:
                flag = False
                for bullet in bullets:
                    if bullet.collide(enemy) and bullet.type == 'p':
                        bullets.remove(bullet)
                        flag = True
                        break
                if flag:
                    if enemy == boss:
                        boss_health = pygame.Rect(500 - (50 + 0.081 * boss.hp), 100, 0.081 * boss.hp, 15)
                        coins += 1
                    enemy.hp -= bullet.dmg
                    if enemy.hp <= 0:
                        lvl4_enemies.remove(enemy)
                        if enemy != boss:
                            coins += enemy.money
                        break

            for bullet in bullets:
                if bullet.collide(player) and bullet.type == 'e':
                    tick1 = 0
                    pflag = True
                    player.img = pygame.transform.scale(pygame.image.load('Easy Code/projects/project4/img/Player_inverted.png'), (64, 32))
                    player.hp -= bullet.dmg
                    health_bar.width -= (1.35 * bullet.dmg)
                    health_bar.x += (1.35 * bullet.dmg)
                    bullets.remove(bullet)
                    break
            
            if tick2 == 480 and boss in lvl4_enemies:
                i = 0
                while i != 5:
                    group = random.randint(1,3)
                    if group == 1:
                        lvl4_enemies.append(Enemy(boss.rect.centerx - 80 + i*32, boss.rect.bottom + 16, 32, 16, 'Easy Code/projects/project4/img/Enemy1.png', 6, 1))
                    elif group == 2:
                        lvl4_enemies.append(Enemy(boss.rect.centerx - 80 + i*32, boss.rect.bottom + 16, 32, 16, 'Easy Code/projects/project4/img/Enemy2.png', 12, 2))
                    elif group == 3:
                        lvl4_enemies.append(Enemy(boss.rect.centerx - 80 + i*32, boss.rect.bottom + 16, 32, 16, 'Easy Code/projects/project4/img/Enemy3.png', 24, 4))
                    i += 1
                tick2 = 0
            
            pygame.draw.rect(screen, (225, 0, 20), boss_health)
            boss_health_board.draw()
            tick2 += 1

            if lvl4_enemies == []:
                game_state = 4

        player.move()
        player.draw()
        ammo_board.draw()
        menu.draw()
        coin.draw()
        pygame.draw.rect(screen, (225, 0, 20), health_bar)
        health_board.draw()
        screen.blit(coins_counter, (58, 15))
        screen.blit(level_text, (215, 15))

        for bullet in ammo_list:
            pygame.draw.rect(screen, (225, 225, 0), bullet)

        if health_bar.w <= 0:
            game_state = 3

        tick += 1
        if pflag == True:
            tick1 += 1
        if tick1 == 15 and pflag == True:
            tick1 = 0
            pflag = False
            player.img = pygame.transform.scale(pygame.image.load('Easy Code/projects/project4/img/Player.png'), (64, 32))
        if tick == reload_speed:
            tick = 0
            if ammo < max_ammo:
                ammo += 1
                if ammo_upgrade == 1:
                    x1 += 16
                    ammo_list.append(pygame.Rect(x1, 685, 12, 9))
                elif ammo_upgrade == 2:
                    x2 += 12
                    ammo_list.append(pygame.Rect(x2, 685, 9, 9))
                elif ammo_upgrade == 3:
                    x3 += 9
                    ammo_list.append(pygame.Rect(x3, 685, 6, 9))

    elif game_state == 2:
        coins_counter = font.render(f'{coins}', False, (225, 225, 0))
        upgrade_text1 = font.render(f'Магазин патронов: {max_ammo}', False, (225, 225, 225))
        upgrade_text2 = font.render(f'Урон: {dmg}', False, (225, 225, 225))
        upgrade_text3 = font.render(f'Скорость перезарядки: {reload_speed}', False, (225, 225, 225))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                x, y = e.pos
                if menu.rect.x < x < menu.rect.right and menu.rect.y < y < menu.rect.bottom:
                    game_state = 1
                elif button1.rect.x < x < button1.rect.right and button1.rect.y < y < button1.rect.bottom and coins >= upgrade1_price and ammo_upgrade < 3:
                    if ammo_upgrade == 1:
                        coins -= upgrade1_price
                        upgrade1_price = 40
                        max_ammo = 11
                        ammo = 0
                        ammo_list = []
                    elif ammo_upgrade == 2:
                        coins -= upgrade1_price
                        max_ammo = 14
                        ammo = 0
                        ammo_list = []
                    ammo_upgrade += 1
                elif button2.rect.x < x < button2.rect.right and button2.rect.y < y < button2.rect.bottom and coins >= upgrade2_price and dmg_upgrade < 3:
                    if dmg_upgrade == 1:
                        coins -= upgrade2_price
                        upgrade2_price = 100
                        dmg = 12
                    elif dmg_upgrade == 2:
                        coins -= upgrade2_price
                        dmg = 24
                    dmg_upgrade += 1
                elif button3.rect.x < x < button3.rect.right and button3.rect.y < y < button3.rect.bottom and coins >= upgrade3_price and reload_upgrade < 3:
                    if reload_upgrade == 1:
                        coins -= upgrade3_price
                        upgrade3_price = 50
                        reload_speed = 35
                        tick = 0
                    elif reload_upgrade == 2:
                        coins -= upgrade3_price
                        reload_speed = 25
                        tick = 0
                    reload_upgrade += 1
                elif button4.rect.x < x < button4.rect.right and button4.rect.y < y < button4.rect.bottom and coins >= kit_price and health_bar.w != 135:
                    health_bar.w = 135
                    health_bar.x = 354
                    coins -= kit_price
        
        if coins >= upgrade1_price and ammo_upgrade != 3:
            button1.img = pygame.transform.scale(pygame.image.load('Easy Code/projects/project4/img/Buy.jpg'), (96, 48))
        elif ammo_upgrade == 3:
            button1.img = pygame.transform.scale(pygame.image.load('Easy Code/projects/project4/img/Max.jpg'), (96, 48))
        else:
            button1.img = pygame.transform.scale(pygame.image.load('Easy Code/projects/project4/img/No_buy.jpg'), (96, 48))
                
        if coins >= upgrade2_price and dmg_upgrade != 3:
            button2.img = pygame.transform.scale(pygame.image.load('Easy Code/projects/project4/img/Buy.jpg'), (96, 48))
        elif dmg_upgrade == 3:
            button2.img = pygame.transform.scale(pygame.image.load('Easy Code/projects/project4/img/Max.jpg'), (96, 48))
        else:
            button2.img = pygame.transform.scale(pygame.image.load('Easy Code/projects/project4/img/No_buy.jpg'), (96, 48))
                
        if coins >= upgrade3_price and reload_upgrade != 3:
            button3.img = pygame.transform.scale(pygame.image.load('Easy Code/projects/project4/img/Buy.jpg'), (96, 48))
        elif reload_upgrade == 3:
            button3.img = pygame.transform.scale(pygame.image.load('Easy Code/projects/project4/img/Max.jpg'), (96, 48))
        else:
            button3.img = pygame.transform.scale(pygame.image.load('Easy Code/projects/project4/img/No_buy.jpg'), (96, 48))
        
        if coins >= kit_price and health_bar.w != 135:
            button4.img = pygame.transform.scale(pygame.image.load('Easy Code/projects/project4/img/Buy.jpg'), (96, 48))
        else:
            button4.img = pygame.transform.scale(pygame.image.load('Easy Code/projects/project4/img/No_buy.jpg'), (96, 48))
    
        menu.draw()
        coin.draw()
        pygame.draw.rect(screen, (20, 20, 20), pygame.Rect(5, 165, 490, 90))
        pygame.draw.rect(screen, (20, 20, 20), pygame.Rect(5, 265, 490, 90))
        pygame.draw.rect(screen, (20, 20, 20), pygame.Rect(5, 365, 490, 90))
        pygame.draw.rect(screen, (20, 20, 20), pygame.Rect(5, 515, 490, 155))
        button1.draw()
        button2.draw()
        button3.draw()
        button4.draw()
        ammo_icon.draw()
        dmg_icon.draw()
        reload_icon.draw()
        kit_icon.draw()
        screen.blit(coins_counter, (58, 15))
        screen.blit(pause_text1, (180, 15))
        screen.blit(pause_text2, (150, 75))
        screen.blit(upgrade_text1, (88, 200))
        screen.blit(upgrade_text2, (88, 300))
        screen.blit(upgrade_text3, (88, 400))
        screen.blit(kit_text, (88, 550))
        screen.blit(font.render(f'{ammo_upgrade}/3', False, (225, 225, 225)), (405, 165))
        screen.blit(font.render(f'{dmg_upgrade}/3', False, (225, 225, 225)), (405, 265))
        screen.blit(font.render(f'{reload_upgrade}/3', False, (225, 225, 225)), (405, 365))
        if ammo_upgrade != 3:
            screen.blit(font.render(f'{upgrade1_price} C', False, (225, 225, 0)), (400, 237))
        if dmg_upgrade != 3:
            screen.blit(font.render(f'{upgrade2_price} C', False, (225, 225, 0)), (400, 337))
        if reload_upgrade != 3:
            screen.blit(font.render(f'{upgrade3_price} C', False, (225, 225, 0)), (400, 437))
        screen.blit(font.render(f'{kit_price} C', False, (225, 225, 0)), (230, 647))
    
    elif game_state == 3:
        screen.blit(end_text1, (60, 350))
        screen.blit(end_text3, (210, 50))
        game_over.draw()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    sys.exit()
    
    elif game_state == 4:
        screen.blit(end_text1, (60, 350))
        screen.blit(end_text2, (180, 50))
        win.draw()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    sys.exit()
        
    pygame.display.update()
    clock.tick(60)
