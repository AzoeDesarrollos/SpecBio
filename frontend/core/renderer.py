from pygame import display, SCALED
from pygame.sprite import LayeredUpdates


class Renderer:
    @classmethod
    def init(cls):
        display.set_caption('SpecBio')
        display.set_mode((400, 400), SCALED)
        cls.contents = LayeredUpdates()

    @classmethod
    def update(cls):
        fondo = display.get_surface()
        cls.contents.draw(fondo)


Renderer.init()