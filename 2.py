from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button

class CameraApp(App):
    def build(self):
        # 创建一个垂直布局
        layout = BoxLayout(orientation='vertical')

        # 创建 Camera 小部件
        self.camera = Camera(index=0, resolution=(640, 480), play=True)
        layout.add_widget(self.camera)

        # 创建一个按钮用于关闭相机
        self.button = Button(text="关闭相机", size_hint=(1, 0.2))
        self.button.bind(on_press=self.stop_camera)
        layout.add_widget(self.button)

        return layout

    def stop_camera(self, instance):
        # 停止相机预览
        self.camera.play = False
        print("相机已关闭")

if __name__ == '__main__':
    CameraApp().run()