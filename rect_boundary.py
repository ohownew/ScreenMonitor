import tkinter as tk
from pynput import mouse
import ctypes

class RectBoundary:
    def __init__(self, scale_factor=None):
        self.start_x = 0
        self.start_y = 0
        self.end_x = 0
        self.end_y = 0
        self.is_dragging = False
        # 创建一个Tkinter窗口
        self.tk_root = tk.Tk()

        if scale_factor is None:
            self.ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
        else:
            self.ScaleFactor = scale_factor
            
        self.tk_root.tk.call('tk', 'scaling', self.ScaleFactor / 100)
        # 获取屏幕宽度和高度
        screen_width = self.tk_root.winfo_screenwidth()
        screen_height = self.tk_root.winfo_screenheight()

        print(f"tk get screen size: {screen_width}x{screen_height}")
        self.tk_root.geometry(f"{screen_width}x{screen_height}+0+0")
        # 全屏
        self.tk_root.attributes('-fullscreen', True)
        self.tk_root.attributes('-alpha', 0.5)
        self.tk_root.attributes('-topmost', True)

        self.canvas = tk.Canvas(self.tk_root, cursor="cross", bg='black', width=screen_width, height=screen_height)
        self.canvas.pack(fill=tk.BOTH, expand=False)

        self.rect_params = {'x':-1, 'y':-1, 'height':-1, 'width':-1}

        self.draw()

    def on_click(self, x, y, button, pressed):
        """鼠标点击事件"""
        if button == mouse.Button.left:
            if pressed:
                # 鼠标左键按下，记录起始位置
                self.start_x, self.start_y = x, y
                self.is_dragging = True
                self.canvas.delete("all")  # 清除之前的矩形
            else:
                # 鼠标左键松开，记录结束位置并计算区域
                self.end_x, self.end_y = x, y
                self.is_dragging = False
                self.calculate_region()
                self.tk_root.quit()

    def on_move(self, x, y):
        """鼠标位移事件"""
        if self.is_dragging:
            self.end_x, self.end_y = x, y
            self.draw_rectangle()

    def mouse2canvas(self, x, y):
        """坐标系转换: 系统屏幕 -> tk.canvas"""
        return round(x / self.ScaleFactor * 100), round(y / self.ScaleFactor * 100)

    def draw_rectangle(self):
        """绘制矩形"""
        self.canvas.delete("all")  # 清除之前的矩形
        x1, y1 = self.mouse2canvas(self.start_x, self.start_y)
        x2, y2 = self.mouse2canvas(self.end_x, self.end_y)
        self.canvas.create_rectangle(x1, y1, x2, y2, outline='blue', fill='blue', stipple='gray50')

    def calculate_region(self):
        """计算滑过区域的左上角位置和宽高"""
        x = min(self.start_x, self.end_x)
        y = min(self.start_y, self.end_y)
        width = abs(self.end_x - self.start_x)
        height = abs(self.end_y - self.start_y)
        # print("canvas xy:", self.mouse2canvas(self.start_x, self.start_y))
        print(f"框选区域的位置和尺寸: (x={x}, y={y}, width={width}, height={height})")
        self.rect_params = {'x':x, 'y':y, 'width':width, 'height':height}

    def draw(self):
        """启动tkinter窗并开始监听鼠标事件"""
        listener = mouse.Listener(on_click=self.on_click, on_move=self.on_move)
        listener.start()
        self.tk_root.mainloop()
        listener.stop()
        self.tk_root.destroy()


if __name__ == '__main__':
    rect = RectBoundary()
    print(rect.rect_params)