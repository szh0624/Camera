from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Line, Color
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.utils import platform
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.behaviors import ButtonBehavior
from datetime import datetime
import os

class CameraGrid(FloatLayout):
    def __init__(self, **kwargs):
        super(CameraGrid, self).__init__(**kwargs)
        self.bind(size=self.update_grid)
        
    def update_grid(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(1, 1, 1, 0.5)  # White color with 50% opacity
            # Vertical lines
            Line(points=[self.width/3, 0, self.width/3, self.height], width=1, dash_length=10, dash_offset=5)
            Line(points=[self.width*2/3, 0, self.width*2/3, self.height], width=1, dash_length=10, dash_offset=5)
            # Horizontal lines
            Line(points=[0, self.height/3, self.width, self.height/3], width=1, dash_length=10, dash_offset=5)
            Line(points=[0, self.height*2/3, self.width, self.height*2/3], width=1, dash_length=10, dash_offset=5)

class CameraApp(App):
    def build(self):
        # Set window size for mobile
        if platform == 'android':
            Window.size = (360, 640)
        
        # Main layout
        self.root = BoxLayout(orientation='vertical')
        
        # Camera preview with grid
        self.camera_grid = CameraGrid()
        self.camera = Camera(resolution=(640, 480), play=True)
        self.camera_grid.add_widget(self.camera)
        self.root.add_widget(self.camera_grid)
        
        # Bottom buttons
        button_layout = BoxLayout(size_hint_y=None, height=50)
        
        # Capture button
        self.capture_btn = Button(text='Capture', size_hint_x=0.5)
        self.capture_btn.bind(on_press=self.capture)
        button_layout.add_widget(self.capture_btn)
        
        # Gallery button
        self.gallery_btn = Button(text='Gallery', size_hint_x=0.5)
        self.gallery_btn.bind(on_press=self.show_gallery)
        button_layout.add_widget(self.gallery_btn)
        
        self.root.add_widget(button_layout)
        
        # Create photos directory if not exists
        if not os.path.exists('camera_photos'):
            os.makedirs('camera_photos')
            
        return self.root
    
    def capture(self, instance):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        photo_path = f'camera_photos/photo_{timestamp}.png'
        self.camera.export_to_png(photo_path)
        
    def show_gallery(self, instance):
        # Create gallery popup
        content = BoxLayout(orientation='vertical')
        scroll = ScrollView()
        gallery = GridLayout(cols=3, size_hint_y=None)
        gallery.bind(minimum_height=gallery.setter('height'))
        
        # Load photos
        if os.path.exists('camera_photos'):
            for photo in sorted(os.listdir('camera_photos'), reverse=True):
                if photo.endswith('.png'):
                    img = ButtonImage(source=f'camera_photos/{photo}')
                    gallery.add_widget(img)
        
        scroll.add_widget(gallery)
        content.add_widget(scroll)
        
        # Close button
        close_btn = Button(text='Close', size_hint_y=None, height=50)
        content.add_widget(close_btn)
        
        popup = Popup(title='Gallery', content=content, size_hint=(0.9, 0.9))
        close_btn.bind(on_press=popup.dismiss)
        popup.open()

class ButtonImage(ButtonBehavior, Image):
    pass

if __name__ == '__main__':
    CameraApp().run()
