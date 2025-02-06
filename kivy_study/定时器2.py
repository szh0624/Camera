from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.text import LabelBase

# 注册字体
LabelBase.register(name="Roboto", fn_regular="msyh.ttc")


def stop_time(instance):
    """
    退出按钮的回调函数，停止应用程序。
    """
    App.get_running_app().stop()


class BodyBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"  # 设置布局方向为垂直
        self.ga = False  # 用于标记计时器是否启动
        self.h = 0  # 小时
        self.f = 0  # 分钟
        self.s = 0  # 秒

        # 创建一个标签，用于显示时间
        self.label_1 = Label(text="00:00:00", font_size=56, font_name="Roboto")
        self.add_widget(self.label_1)

        # 创建一个水平布局，用于放置按钮
        self.f_box = BoxLayout(orientation="horizontal", size_hint=(1, 0.3))

        # 创建开始/暂停按钮
        self.bu1 = Button(text="开始", on_press=self.start_time)
        self.f_box.add_widget(self.bu1)

        # 创建重置按钮
        self.bu2 = Button(text="重置", on_press=self.reset_time)
        self.f_box.add_widget(self.bu2)

        # 创建退出按钮
        self.bu3 = Button(text="退出", on_press=stop_time)
        self.f_box.add_widget(self.bu3)

        # 将按钮布局添加到主布局中
        self.add_widget(self.f_box)

    def start_time(self, instance):
        """
        开始/暂停按钮的回调函数，控制计时器的启动和暂停。
        """
        if not self.ga:
            self.ga = True
            self.bu1.text = "暂停"  # 按钮文本改为“暂停”
            Clock.schedule_interval(self.update_time, 1)  # 启动计时器
        else:
            self.ga = False
            self.bu1.text = "开始"  # 按钮文本改为“开始”
            Clock.unschedule(self.update_time)  # 停止计时器

    def reset_time(self, instance):
        """
        重置按钮的回调函数，将计时器重置为 0。
        """
        self.ga = False  # 停止计时器
        self.h = 0  # 小时重置为 0
        self.f = 0  # 分钟重置为 0
        self.s = 0  # 秒重置为 0
        self.label_1.text = "00:00:00"  # 更新显示
        self.bu1.text = "开始"  # 按钮文本改为“开始”
        Clock.unschedule(self.update_time)  # 停止计时器

    def update_time(self, dt):
        """
        计时器回调函数，每秒更新一次时间。
        """
        self.s += 1
        if self.s == 60:
            self.s = 0
            self.f += 1
        if self.f == 60:
            self.f = 0
            self.h += 1
        self.label_1.text = f"{self.h:02d}:{self.f:02d}:{self.s:02d}"  # 更新标签的文本

class ClockApp(App):
    def build(self):
        """
        构建应用程序的主界面。
        """
        return BodyBox()

# 运行应用程序
if __name__ == '__main__':
    ClockApp().run()