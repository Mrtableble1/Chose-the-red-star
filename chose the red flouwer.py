import pgzrun
import random


HEIGHT = 800
WIDTH = 1000

TITLE = "Chose the red flouwer"

actors = []
total = 5
clvl = 1


garbage = ["blue","orange","green","purple"]

animations = []

gameover = False
gamefinished = False


def draw():
    screen.blit("cool_earth",(0,0))
    if gameover :
        screen.draw.text("NOOOO THE STAR REACHED THE EARTH",(500,400))
    elif gamefinished:
        screen.draw.text("YOU SAVED THE WORLD!",(500,400))
        
    else :
        for actor in actors:
            actor.draw()
        screen.draw.text("LEVEL "+str(clvl),(10,750))


def next_level():
    global clvl,gamefinished
    stop_animations()
    clvl = clvl + 1
    if clvl > total:
        gamefinished = True
    else:
        screenactors()



def on_mouse_down(pos):
    for actor in actors:
        if actor.collidepoint(pos):
            if actor.image == "red":
                next_level()
            else:
                game_over()


def game_over():
    global gameover
    gameover = True

def update():
    pass

def stop_animations():
    global animations
    for animation in animations:
        if animation.running:
            animation.stop()

def screenactors():
    global actors ,animations
    #selecting actors
    actors.clear()
    images = ["red"]
    for i in range(clvl):
        images.append(random.choice(garbage))

    #creating actors
    for image in images:
        red = Actor(image)
        actors.append(red)
    #positioning the actors

    nog = clvl+2
    size = WIDTH/nog
    number = 1
    random.shuffle(actors)
    for actor in actors:
        actor.pos = size*number,0
        number+=1

    #animating the actors

    for actor in actors:
        actor.anchor = ("center","bottom")
        animation = animate(actor,duration = 4, on_finished = game_over,y = 800)
        animations.append(animation)

        



        






screenactors()
pgzrun.go()