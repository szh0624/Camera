from kivy.app import App
from kivy.uix.button import Button
from kivy.core.text import LabelBase
LabelBase.register(name="Roboto", fn_regular="msyh.ttc")
class MyApp(App):
    def build(self):
        # 创建一个基础按钮
        btn = Button(text='调整后的按钮',
    size_hint=(0.5, 0.2),  # 宽度占父容器的50%，高度占20%
    pos_hint={'x': 0.25, 'y': 0.4}  # 位置偏移
)
        return btn

if __name__ == '__main__':
    MyApp().run()