import arcade

LARGURA = 800
ALTURA = 600

class Jogo(arcade.Window):
    def __init__(self):
        super().__init__(LARGURA, ALTURA, "SpriteList - Arcade")

        # Cria uma SpriteList
        self.sprites = arcade.SpriteList()

        # Adiciona 1000 sprites
        for i in range(1000):
            sprite = arcade.Sprite("assets/images/player_car.png")

            sprite.center_x = (i % 40) * 20
            sprite.center_y = (i // 40) * 20

            self.sprites.append(sprite)

    def on_draw(self):
        self.clear()

        # O Arcade desenha a SpriteList de forma otimizada
        self.sprites.draw()


jogo = Jogo()
arcade.run()