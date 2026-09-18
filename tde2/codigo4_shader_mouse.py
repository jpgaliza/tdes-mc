import arcade
from array import array

LARGURA = 800
ALTURA = 600

VERTEX_SHADER = """
#version 330
in vec2 posicao;
void main() {
    gl_Position = vec4(posicao, 0.0, 1.0);
}
"""

FRAGMENT_SHADER = """
#version 330
uniform float t;
uniform vec2 tela;
uniform vec2 mouse;
out vec4 corFinal;

void main() {
    vec2 uv = gl_FragCoord.xy / tela;
    vec2 mouseNorm = mouse / tela;

    float dist = distance(uv, mouseNorm);
    float onda = sin(dist * 20.0 - t * 3.0) * 0.5 + 0.5;

    vec3 base = vec3(uv.x, uv.y, 0.5);
    vec3 cor = base * onda;

    corFinal = vec4(cor, 1.0);
}
"""

class JanelaShader(arcade.Window):
    def __init__(self):
        super().__init__(LARGURA, ALTURA, "Shader Interativo com Mouse")

        self.shader = self.ctx.program(
            vertex_shader=VERTEX_SHADER,
            fragment_shader=FRAGMENT_SHADER,
        )

        pontos = array('f', [
            -1.0, -1.0,
             1.0, -1.0,
            -1.0,  1.0,
             1.0,  1.0,
        ])
        buffer_pontos = self.ctx.buffer(data=pontos)

        self.tela_shader = self.ctx.geometry(
            [arcade.gl.BufferDescription(buffer_pontos, '2f', ['posicao'])],
            mode=self.ctx.TRIANGLE_STRIP,
        )

        self.relogio = 0
        self.mouse_x = LARGURA / 2
        self.mouse_y = ALTURA / 2

    def on_draw(self):
        self.clear()
        self.shader['t'] = self.relogio
        self.shader['tela'] = (LARGURA, ALTURA)
        self.shader['mouse'] = (self.mouse_x, self.mouse_y)
        self.tela_shader.render(self.shader)

    def on_update(self, delta_time):
        self.relogio += delta_time

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_x = x
        self.mouse_y = y


jogoShader = JanelaShader()
arcade.run()
