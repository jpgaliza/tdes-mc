import arcade
LARGURA = 800
ALTURA = 500
class Jogo(arcade.Window):
    def __init__(self):
        super().__init__(LARGURA, ALTURA, "Primitivas e Transformações")

        self.x = 200
        self.y = 250
        self.angulo = 0

    def on_draw(self):
        self.clear()
      
        arcade.draw_circle_filled(
            150, 350, 50,
            arcade.color.BLUE
        )
        arcade.draw_rect_filled(
            arcade.XYWH(self.x, self.y, 150, 80),
            arcade.color.GREEN,
            tilt_angle=self.angulo
        )

    def on_update(self, delta_time):
        self.x += 100 * delta_time
        self.angulo += 100 * delta_time

        if self.x > LARGURA + 75:
            self.x = -75


jogo = Jogo()
arcade.run()
