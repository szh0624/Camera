from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button

class CameraApp(App):
    def build(self):
        # Create a vertical layout
        layout = BoxLayout(orientation='vertical')

        # Create a Camera widget
        self.camera = Camera(index=0, resolution=(1000, 600), play=True)
        layout.add_widget(self.camera)


        return layout


if __name__ == '__main__':
  CameraApp().run()