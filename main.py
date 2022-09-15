def on_button_pressed_a():
    sprite.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    sprite.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

coin: game.LedSprite = None
sprite: game.LedSprite = None
game.add_score(1)
game.add_life(1)
sprite = game.create_sprite(2, 4)

def on_forever():
    for index in range(999999):
        music.play_melody("G A F B G F B A ", 125)
        music.play_melody("G B C5 G B C5 A F ", 125)
basic.forever(on_forever)

def on_forever2():
    global coin
    coin = game.create_sprite(randint(0, 4), 0)
    for index2 in range(5):
        basic.pause(500)
        coin.change(LedSpriteProperty.Y, 1)
basic.forever(on_forever2)

def on_forever3():
    if coin.is_touching(sprite):
        coin.delete()
        game.add_score(1)
basic.forever(on_forever3)
