def on_on_created(sprite):
    mySprite3.x = randint(0, 100)
sprites.on_created(SpriteKind.enemy, on_on_created)

def on_up_pressed():
    mySprite.vy += -1
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_on_created2(sprite):
    mySprite2.x = randint(0, 100)
sprites.on_created(SpriteKind.food, on_on_created2)

def on_left_pressed():
    mySprite.vx += -1
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    mySprite.vx += 1
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    mySprite.vy += 1
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

mySprite3: Sprite = None
mySprite2: Sprite = None
mySprite: Sprite = None
scene.set_background_color(9)
game.splash("Motion Project Game")
mySprite = sprites.create(img("""
        ......ffff..............
            ....fff22fff............
            ...fff2222fff...........
            ..fffeeeeeefff..........
            ..ffe222222eef..........
            ..fe2ffffff2ef..........
            ..ffffeeeeffff......ccc.
            .ffefbf44fbfeff....cddc.
            .ffefbf44fbfeff...cddc..
            .fee4dddddd4eef.ccddc...
            fdfeeddddd4eeffecddc....
            fbffee4444ee4fddccc.....
            fbf4f222222f1edde.......
            fcf.f222222f44ee........
            .ff.f445544f............
            ....ffffffff............
            .....ff..ff.............
            ........................
            ........................
            ........................
            ........................
            ........................
            ........................
            ........................
    """),
    SpriteKind.player)
mySprite.x += -1 * 1
mySprite.x = 75
mySprite.y = 75
mySprite2 = sprites.create(assets.image("""
    Tree
"""), SpriteKind.food)
mySprite3 = sprites.create(assets.image("""
    Snake
"""), SpriteKind.enemy)