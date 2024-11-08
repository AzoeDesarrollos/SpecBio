from pygame.sprite import LayeredUpdates
from pygame import event, QUIT, KEYDOWN, K_ESCAPE
from backend.event_handler import EventHandler


class WidgetHandler:
    @classmethod
    def init(cls):
        cls.contents = LayeredUpdates()

    @classmethod
    def add_widget(cls, widget):
        cls.contents.add(widget)

    @classmethod
    def rem_widget(cls, widget):
        if widget in cls.contents.sprites():
            cls.contents.remove(widget)

    @classmethod
    def update(cls):
        for ev in event.get(KEYDOWN):
            if (ev.type == QUIT) or (ev.type == KEYDOWN and ev.key == K_ESCAPE):
                EventHandler.trigger('salir', cls, {'mensaje': 'normal'})

        cls.contents.update()

WidgetHandler.init()