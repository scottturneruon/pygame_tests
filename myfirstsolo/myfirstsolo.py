import random

bee = Actor ('bee')
bee.pos = 50,50

player = Actor ('panic')
player.pos = 750, 750

HEIGHT = 800
WIDTH = 800

def draw():
    screen.clear()
    bee.draw()
    player.draw()

def update():
    player_update()
    bee_update()
    if bee.colliderect(player):
        player_hurt()

def player_update():
    if keyboard.right:
        player.pos = (player.x+5, player.y)
    if keyboard.left:
        player.pos = (player.x-5, player.y)
    if keyboard.up:
        player.pos = (player.x, player.y-5)
    if keyboard.down:
        player.pos = (player.x, player.y+5)
    if player.y>HEIGHT+25:
        player.y=25
    if player.y< 25:
        player.y = HEIGHT-50
    if player.x>WIDTH+25:
        player.x=25
    if player.x< 25:
        player.x = WIDTH-50

def bee_update():
    bee.pos= (bee.x + random.randint(-25,25), bee.y + random.randint(-25,25))
    if bee.y>HEIGHT+25:
        bee.y=25
    if bee.y< 25:
        bee.y = HEIGHT-50
    if bee.x>WIDTH+25:
        bee.x=25
    if bee.x< 25:
        bee.x = WIDTH-50

def player_hurt():
    player.image='ohno'
    sounds.sneeze.play()
    clock.schedule_unique(player_normal, 1)

def player_normal():
    player.image='panic'
