def on_a_pressed():
    PrincessRose.say(sentence)
    PrincessBlue.say(nouns)
    PrincessSun.say(verbs)
    PrincessViolet.say(pronouns)
    pause(5000)
    PrincessRose.start_effect(effects.fire, 5000)
    PrincessBlue.start_effect(effects.fire, 5000)
    PrincessSun.start_effect(effects.fire, 5000)
    PrincessViolet.start_effect(effects.fire, 5000)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

pronouns = ""
verbs = ""
nouns = ""
sentence = ""
PrincessViolet: Sprite = None
PrincessSun: Sprite = None
PrincessBlue: Sprite = None
PrincessRose: Sprite = None
scene.set_background_color(1)
PrincessRose = sprites.create(img("""
        . . . . . f f 4 4 f f . . . . . 
            . . . . f 5 4 5 5 4 5 f . . . . 
            . . . f e 4 5 5 5 5 4 e f . . . 
            . . f b 3 e 4 4 4 4 e 3 b f . . 
            . . f 3 3 3 3 3 3 3 3 3 3 f . . 
            . f 3 3 e b 3 e e 3 b e 3 3 f . 
            . f 3 3 f f e e e e f f 3 3 f . 
            . f b b f b f e e f b f b b f . 
            . f b b e 1 f 4 4 f 1 e b b f . 
            f f b b f 4 4 4 4 4 4 f b b f f 
            f b b f f f e e e e f f f b b f 
            . f e e f b d d d d b f e e f . 
            . . e 4 c d d d d d d c 4 e . . 
            . . e f b d b d b d b b f e . . 
            . . . f f 1 d 1 d 1 d f f . . . 
            . . . . . f f b b f f . . . . .
    """),
    SpriteKind.player)
PrincessBlue = sprites.create(img("""
        . . . . . . 5 . 5 . . . . . . . 
            . . . . . f 5 5 5 f f . . . . . 
            . . . . f 1 5 2 5 1 6 f . . . . 
            . . . f 1 6 6 6 6 6 1 6 f . . . 
            . . . f 6 6 f f f f 6 1 f . . . 
            . . . f 6 f f d d f f 6 f . . . 
            . . f 6 f d f d d f d f 6 f . . 
            . . f 6 f d 3 d d 3 d f 6 f . . 
            . . f 6 6 f d d d d f 6 6 f . . 
            . f 6 6 f 3 f f f f 3 f 6 6 f . 
            . . f f d 3 5 3 3 5 3 d f f . . 
            . . f d d f 3 5 5 3 f d d f . . 
            . . . f f 3 3 3 3 3 3 f f . . . 
            . . . f 3 3 5 3 3 5 3 3 f . . . 
            . . . f f f f f f f f f f . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
PrincessSun = sprites.create(img("""
        . . . . . f 2 f 2 . . . . . 
            . . . f f 4 4 4 4 4 f . . . 
            . . f 5 5 4 5 4 5 4 5 f . . 
            . f 5 5 5 5 5 5 5 5 5 5 f . 
            . f 5 5 5 d b b d 5 5 5 f . 
            f 5 5 5 b 4 4 4 4 b 5 5 5 f 
            f 5 5 c c 4 4 4 4 c c 5 5 f 
            f b b f b f 4 4 f b f b b f 
            f b b 4 1 f d d f 1 4 b b f 
            . f b f d d d d d d f b f . 
            . f e f e 4 4 4 4 e f e f . 
            . e 4 f 6 9 9 9 9 6 f 4 e . 
            . 4 d c 9 9 9 9 9 9 c d 4 . 
            . 4 f d 5 d 5 d 5 d d f 4 . 
            . . f f 5 d 5 d 5 5 f f . . 
            . . . . f f d d f f . . . .
    """),
    SpriteKind.player)
PrincessViolet = sprites.create(img("""
        . . . . . f f 4 4 f f . . . . . 
            . . . . f 5 4 5 5 4 5 f . . . . 
            . . . f e 4 5 5 5 5 4 e f . . . 
            . . f b a e 4 4 4 4 e a b f . . 
            . . f a a a a a a a a a a f . . 
            . f a a e b a e e a b e a a f . 
            . f a a f f e e e e f f a a f . 
            . f b b f b f e e f b f b b f . 
            . f b b e 1 f 4 4 f 1 e b b f . 
            f f b b f 4 4 4 4 4 4 f b b f f 
            f b b f f f e e e e f f f b b f 
            . f e e f b a a a a b f e e f . 
            . . e 4 c a a a a a a c 4 e . . 
            . . e f b a b a b a b b f e . . 
            . . . f f 1 d 1 d 1 d f f . . . 
            . . . . . f f b b f f . . . . .
    """),
    SpriteKind.player)
PrincessRose.set_position(80, 35)
PrincessBlue.set_position(100, 85)
PrincessSun.set_position(40, 60)
PrincessViolet.set_position(50, 100)
sentence = "The castle is cold in the winter, which is why we build fires!"
nouns = "" + sentence.substr(4, 6) + sentence.substr(25, 7) + sentence.substr(55, 5)
verbs = "" + sentence.substr(11, 3) + sentence.substr(50, 5)
pronouns = sentence.substr(47, 2)