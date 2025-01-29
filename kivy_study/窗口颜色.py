from kivy.app import App
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.clearcolor =get_color_from_hex("#FFFFFF")
Apps=App()
Apps.title="YFTHKKD App"
Apps.run()