#可用，存在拉伸
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.camera import Camera
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
import os
from datetime import datetime

class CameraApp(App):
    def build(self):
        # Create the album folder
        self.album_folder = "photo_album"
        if not os.path.exists(self.album_folder):
            os.makedirs(self.album_folder)

        # Initialize the camera with index=0 (default to the first available camera device)
        self.camera = Camera(index=0, resolution=(640, 480), play=True)
        self.camera.allow_stretch = True  # Allow the camera to stretch to fit the container
        self.camera.keep_ratio = False    # Disable keeping the aspect ratio

        # Main layout
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.camera)

        # Button layout
        button_layout = BoxLayout(size_hint_y=None, height=50)
        capture_button = Button(text="Capture")
        capture_button.bind(on_press=self.capture)
        album_button = Button(text="Album")
        album_button.bind(on_press=self.show_album)

        button_layout.add_widget(capture_button)
        button_layout.add_widget(album_button)
        layout.add_widget(button_layout)

        return layout

    def capture(self, instance):
        """Capture a photo and save it to the album folder"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        photo_path = os.path.join(self.album_folder, f"photo_{timestamp}.png")
        self.camera.export_to_png(photo_path)
        print(f"Photo saved to: {photo_path}")

    def show_album(self, instance):
        """Display all photos in the album"""
        photos = os.listdir(self.album_folder)
        if not photos:
            # If the album is empty, show a message
            popup = Popup(title="Album", content=Label(text="The album is empty."), size_hint=(0.8, 0.8))
            popup.open()
            return

        # Create a scroll view and grid layout to display photos
        scroll_view = ScrollView()
        grid_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        for photo in photos:
            img = Image(source=os.path.join(self.album_folder, photo), size_hint_y=None, height=400)
            grid_layout.add_widget(img)

        scroll_view.add_widget(grid_layout)
        popup = Popup(title="Album", content=scroll_view, size_hint=(0.8, 0.8))
        popup.open()

if __name__ == '__main__':
    CameraApp().run()