from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.clock import Clock

# 全局变量
h = 0  # 小时
s = 0  # 秒
f = 0  # 分钟
label_1 = None  # Label 控件

def up_time(dt):
    """
    定时器回调函数，每秒更新一次时间。
    """
    global h, s, f, label_1
    s += 1
    if s == 60:
        s = 0
        f += 1
    if f == 60:
        f = 0
        h += 1
    # 更新 Label 的文本
    label_1.text = "%02d:%02d:%02d" % (h, f, s)

def show_body():
    """
    创建并返回一个 Label 控件，并启动定时器。
    """
    global label_1
    # 创建 Label，初始时间为 00:00:00
    label_1 = Label(text="%02d:%02d:%02d" % (0, 0, 0), font_size=56)
    # 启动定时器，每秒调用一次 up_time
    Clock.schedule_interval(up_time, 1)
    return label_1
Window.size = (800, 600)
#Window.fullscreen = True全屏
#Window.borderless = True不要标题栏
kivy_app = App()
kivy_app.build = show_body
kivy_app.run()