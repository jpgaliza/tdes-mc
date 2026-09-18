import random
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Demonstração de Draw Call Batching com SpriteList"
NUM_SPRITES = 5000


class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.AMAZON)

        # 1. Criação do SpriteList
        # O SpriteList gerencia os buffers na VRAM da GPU
        self.coins_list = arcade.SpriteList()

        # 2. Popula o SpriteList
        for _ in range(NUM_SPRITES):
            # Usando uma textura embutida do Arcade para facilitar o teste
            coin = arcade.Sprite(":resources:images/items/gold_1.png", scale=0.3)
            
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            
            # Adiciona ao SpriteList (isso atualiza o buffer na GPU)
            self.coins_list.append(coin)

    def on_draw(self):
        # Limpa a tela
        self.clear()

        # 3. O 'magic' do Arcade / OpenGL:
        # Apenas 1 DRAW CALL é enviado para a GPU renderizar os 5.000 sprites de uma vez!
        self.coins_list.draw()

    def on_update(self, delta_time):
        # Mover os elementos altera a VRAM via instanced attribute buffers
        for coin in self.coins_list:
            coin.center_y -= 1
            if coin.top < 0:
                coin.bottom = SCREEN_HEIGHT


if __name__ == "__main__":
    window = GameWindow()
    arcade.run()
