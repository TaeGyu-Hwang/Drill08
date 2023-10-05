from pico2d import *
import random

# Game object class here
class Grass: # 클래스 이름은 대문자로 시작하는 명사..
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball1:
    def __init__(self):
        self.hx, self.hy = random.randint(50, 750), 599
        self.frame = random.randint(0, 7)
        self.image = load_image('ball21x21.png')

    def update(self):
        if self.hy > 0:  # 바닥에 닿지 않았다면
            self.frame = (self.frame + 1) % 8
            self.hy -= 5
        else:
            self.hy = 0  # 바닥에 닿으면 높이를 0으로 설정

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.hx, self.hy)

class Ball2:
    def __init__(self):
        self.hx, self.hy = random.randint(50, 750), 599
        self.frame = random.randint(0, 7)
        self.image = load_image('ball41x41.png')

    def update(self):
        if self.hy > 0:  # 바닥에 닿지 않았다면
            self.frame = (self.frame + 1) % 8
            self.hy -= 5
        else:
            self.hy = 0  # 바닥에 닿으면 높이를 0으로 설정

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.hx, self.hy)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



def reset_world():
    global running
    global grass
    global team
    global world
    global ball1
    global ball2

    running = True
    world = []

    grass = Grass() # 클래스를 이용해 객체를 찍어냄.
    world.append(grass)

    team = [Boy() for i in range(11)]
    world += team

    ball1 = [Ball1() for b in range(20)]
    world += ball1
    ball2 = [Ball2() for b in range(20)]
    world += ball2


# initialization code


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

def update_world():
    for o in world:
        o.update()


open_canvas()
reset_world()

# game main loop code
while running:
    handle_events()
    update_world() # 객체들의 상호작용 결과 업데이트
    render_world()
    delay(0.05)


# finalization code

close_canvas()
