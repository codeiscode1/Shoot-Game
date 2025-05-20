import pgzhelper as p
import pgzero
import pgzrun


WIDTH = 500
HEIGHT = 500
TITLE = "Shoot The Ball!!!"


gun = p.Actor("gun")
bullet = p.Actor("bullet")
target = p.Actor("star")

gun.x = 50
gun.y = 250
target.x = 450

bullet_active = False
hit_timer = 0
score = 0
score_add = False

def handle_collision():
    global bullet_active
    global score
    global score_add
    global hit_timer
    hit_timer = 30
    bullet_active = False
    bullet.left = gun.right
    sounds.eep.play()


def draw():
    global hit_timer
    global score
    global score_add
    screen.draw.filled_rect(Rect((0,0),(500,500)),'blue')
    gun.draw()
    target.draw()
    if bullet_active:
        bullet.draw()
    if hit_timer > 0:
        screen.draw.text(
            f"Hit!!Score:{int(score)}!", (0, 0), fontsize=100, color="green"
        )


def update():
    global bullet_active
    global score_add
    global hit_timer
    global score
    if score < 10:
        target.y+=5
    if score < 20 and score > 10:
        target.y+=10
    if score < 30 and score >20:
        target.y += 20
    if target.y > HEIGHT:
        target.y = 0
    if bullet_active:
        bullet.x += 20
    if target.colliderect(bullet):
        handle_collision()
        score_add = True
    if hit_timer > 0:
        hit_timer -= 1
    if score_add:
        score += 1
        score_add = False



def on_mouse_down():
    global bullet_active
    bullet.left = gun.right
    bullet.y = gun.y
    bullet_active = True

pgzrun.go()
