from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button

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
        button_layout.add_widget(capture_button)


        return layout


if __name__ == '__main__':
    CameraApp().run()