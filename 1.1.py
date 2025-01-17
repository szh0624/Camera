from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button

class CameraApp(App):
    def build(self):
        # Create a vertical layout
        layout = BoxLayout(orientation='vertical')

        # Create a Camera widget
        self.camera = Camera(index=0, resolution=(600, 800), play=True)
        layout.add_widget(self.camera)

        # Create a button to stop the camera
        self.button = Button(text="Stop Camera", size_hint=(1, 0.2))
        self.button.bind(on_press=self.stop_camera)
        layout.add_widget(self.button)

        return layout

    def stop_camera(self, instance):
        # Stop the camera preview
        self.camera.play = False
        # Update the button text
        self.button.text = "Camera has been stopped"
        print("Camera has been stopped")

if __name__ == '__main__':
    CameraApp().run()