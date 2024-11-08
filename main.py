from frontend import Renderer, WidgetHandler
from backend.event_handler import EventHandler

while True:
    WidgetHandler.update()
    EventHandler.process()
    Renderer.update()