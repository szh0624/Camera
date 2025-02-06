from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.clock import Clock

class TimerApp(App):
    def build(self):
        self.h = 0  # 小时
        self.s = 0  # 秒
        self.f = 0  # 分钟

        # 创建 Label，初始时间为 00:00:00
        self.label = Label(text="%02d:%02d:%02d" % (0, 0, 0), font_size=56)
        
        # 启动定时器，每秒调用一次 up_time
        Clock.schedule_interval(self.up_time, 1)
        
        return self.label
    
    def up_time(self, dt):
        self.s += 1
        if self.s == 60:
            self.s = 0
            self.f += 1
        if self.f == 60:
            self.f = 0
            self.h += 1
        # 更新 Label 的文本
        self.label.text = "%02d:%02d:%02d" % (self.h, self.f, self.s)

# 设置窗口大小
Window.size = (800, 600)

# 运行应用程序
TimerApp().run()