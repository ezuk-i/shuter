from pygame import *
from random import randint
finish = False

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()



window = display.set_mode((700, 500))
display.set_caption("Шутер")
background = transform.scale(image.load("galaxy.jpg"),(700, 500))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_size, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_size, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        kp = key.get_pressed()
        if kp[K_UP]:
            self.rect.y = self.rect.y - self.speed
        if kp[K_DOWN]:
            self.rect.y = self.rect.y + self.speed
        if kp[K_RIGHT]:
            self.rect.x = self.rect.x + self.speed
        if kp[K_LEFT]:
            self.rect.x = self.rect.x - self.speed

    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.centery, 100, 15, 20)
        bullets.add(bullet)


class Enemy(GameSprite):
    def update(self):
        self.rect.y = self.rect.y + self.speed
        if self.rect.y > 500:
            self.rect.y = 1
            self.rect.x = randint(1, 700)

class Bullet(GameSprite):
    def update(self):
        self.rect.y = self.rect.y - self.speed
        if self.rect.y < 1:
            self.kill()


player1 = Player("rocket.png", 300, 440, 30, 30, 40)
bullets = sprite.Group()
monsters = sprite.Group()
for i in range(8):
    monster = Enemy("ufo.png", randint(80, 620), -40, 5, 50, 40)
    monsters.add(monster)


finish = False

game = True
while game:

    kp = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
        if kp[K_SPACE]:
            player1.fire()
    if finish != True:

        window.blit(background,(0,0))

        if sprite.groupcollide(monsters, bullets, True, True):
            monster = Enemy("ufo.png",randint(0,550),100,3,65,65)
            monsters.add(monster)


        player1.update()
        monsters.update()
        bullets.update()

        player1.reset()
        monsters.draw(window)
        bullets.draw(window)

        display.update()

    time.delay(30)























































