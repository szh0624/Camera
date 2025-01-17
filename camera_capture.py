from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
import os


class CameraApp(App):
    def build(self):
        # Create a vertical layout
        layout = BoxLayout(orientation='vertical')

        # Create a Camera widget with default camera (index=0)
        self.camera = Camera(index=0, resolution=(640, 480), play=True)
        layout.add_widget(self.camera)

        # Create a horizontal layout for buttons
        button_layout = BoxLayout(size_hint=(1, 0.1))
        layout.add_widget(button_layout)

        # Create a "Capture" button
        capture_button = Button(text="Capture")
        capture_button.bind(on_press=self.capture)
        button_layout.add_widget(capture_button)

        # Create an "Album" button
        album_button = Button(text="Album")
        album_button.bind(on_press=self.show_album)
        button_layout.add_widget(album_button)

        # Create a folder for storing photos
        self.photo_folder = "camera_photos"
        if not os.path.exists(self.photo_folder):
            os.makedirs(self.photo_folder)

        return layout

    def capture(self, instance):
        """Capture the current camera frame and save it to the photo folder."""
        # Get the current frame from the camera
        texture = self.camera.texture

        if texture:
            # Save the texture as an image file
            photo_path = os.path.join(self.photo_folder, f"photo_{len(os.listdir(self.photo_folder)) + 1}.png")
            texture.save(photo_path, flipped=False)
            print(f"Photo saved to {photo_path}")

    def show_album(self, instance):
        """Open a popup to display the photos in the album."""
        # Create a popup to display the photos
        popup = Popup(title="Album", size_hint=(0.9, 0.9))

        # Create a scrollable grid layout for the photos
        scroll_view = ScrollView()
        grid_layout = GridLayout(cols=2, spacing=10, size_hint_y=None)
        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        # Load and display each photo in the folder
        for photo_name in os.listdir(self.photo_folder):
            photo_path = os.path.join(self.photo_folder, photo_name)
            if os.path.isfile(photo_path):
                image = Image(source=photo_path, size_hint=(None, None), size=(300, 300))
                grid_layout.add_widget(image)

        scroll_view.add_widget(grid_layout)
        popup.content = scroll_view
        popup.open()

if __name__ == '__main__':
    CameraApp().run()
#可运行