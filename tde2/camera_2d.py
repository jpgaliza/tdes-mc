import arcade

class ExemploCamera(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Exemplo 2D")

        self.cam_mundo = arcade.Camera2D()
        self.cam_gui = arcade.Camera2D()

    def on_draw(self):
        self.clear()

        # Elemento do mundo
        self.cam_mundo.use()
        arcade.draw_circle_filled(
            400, 300, 40,
            arcade.color.BLUE
        )

        # Interface fixa
        self.cam_gui.use()
        arcade.draw_text(
            "Pontuação: 100",
            20, 560,
            arcade.color.WHITE,
            16
        )

arcade.run()
