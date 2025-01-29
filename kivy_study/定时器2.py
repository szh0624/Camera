from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.text import LabelBase

# 注册系统字体
LabelBase.register(name="Roboto", fn_regular="msyh.ttc")

class Body_box(BoxLayout):
    def __init__(self):
        super().__init__()
        self.ga = False  # 用于标记计时器是否启动
        self.orientation = "vertical"  # 设置布局方向为垂直
        self.h = 0  # 小时
        self.s = 0  # 秒
        self.f = 0  # 分钟

        # 创建一个标签，用于显示时间
        self.label_1 = Label(text="%02d:%02d:%02d" % (0, 0, 0), font_size=56, font_name="Roboto")
        self.add_widget(self.label_1)

        # 创建一个水平布局，用于放置按钮
        self.f_box = BoxLayout(orientation="horizontal", size_hint=(1, 0.3))
        
        # 创建开始按钮
        self.bu1 = Button(text="开始", on_press=self.start_time)
        self.f_box.add_widget(Button(text="开始", on_press=self.start_time))
        
        # 创建退出按钮
        self.f_box.add_widget(Button(text="退出", on_press=self.stop_time))
        
        # 将按钮布局添加到主布局中
        self.add_widget(self.f_box)

    def start_time(self, event):
        """
        开始按钮的回调函数，启动计时器。
        """
        if not self.ga:
            self.ga = True
            self.bu1.text = "暂停"  # 按钮文本改为“暂停”
            Clock.schedule_interval(self.update_time, 1)  # 启动计时器
        else:
            self.ga = False
            self.bu1.text = "开始"  # 按钮文本改为“开始”
            Clock.unschedule(self.update_time)  # 停止计时器

    def stop_time(self, event):
        """
        退出按钮的回调函数，停止应用程序。
        """
        App.get_running_app().stop()

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
        # 更新标签的文本
        self.label_1.text = "%02d:%02d:%02d" % (self.h, self.f, self.s)

    def start_run(self):
        """
        返回当前实例，用于链式调用。
        """
        return self

class ClockApp(App):
    def build(self):
        # 创建 Body_box 的实例并返回
        return Body_box()

# 运行应用程序
if __name__ == '__main__':
    ClockApp().run()