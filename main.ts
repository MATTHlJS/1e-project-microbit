input.onButtonPressed(Button.A, function () {
    sprite.move(-1)
})
input.onButtonPressed(Button.B, function () {
    sprite.move(1)
})
let coin: game.LedSprite = null
let sprite: game.LedSprite = null
game.addScore(1)
game.addLife(1)
sprite = game.createSprite(2, 3)
basic.forever(function () {
	
})
basic.forever(function () {
    coin = game.createSprite(randint(0, 4), 0)
    basic.pause(500)
    for (let index = 0; index < 4; index++) {
        basic.pause(500)
        coin.change(LedSpriteProperty.Y, 1)
    }
})
basic.forever(function () {
    if (sprite.isTouching(coin)) {
        coin.delete()
        game.addScore(1)
    }
})
basic.forever(function () {
    if (coin.get(LedSpriteProperty.Y) == 4) {
        game.gameOver()
    }
})
