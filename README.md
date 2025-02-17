# ScreenMonitor

A Python tool to monitor screen changes

监控屏幕变化的Python工具

## Features
- Select a region of the screen to monitor based on canvas in tkinter.
- Continuously monitor the selected region for changes. Do something when changes are detected, such as save the screenshot.
- Potential for future enhancements like notifications via email, QQ, WeChat, etc.
- 基于tkinter的canvas，选择要监控的屏幕区域。
- 持续监控所选区域的变化。在检测到变化时执行后续操作，如保存截图。
- 未来可能的增强功能，如通过电子邮件、QQ、微信等发送通知。

## Requirements
- `Python>=3.9`
- `pynput`
- `pyautogui`
- `Pillow`

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/ohownew/ScreenMonitor.git
    cd ScreenMonitor
    ```
2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Run the tool:
    ```sh
    python screen_monitor.py
    ```

2. Select the region of the screen to monitor by clicking and dragging the mouse.

3. The tool will continuously monitor the selected region. When a change is detected, a screenshot of the region will be saved as `screenshot.jpg`.

4. If the selected region deviates from the cursor, change the `RectBoundary(scale_factor=100)` into `RectBoundary(scale_factor=None)` in file `screen_monitor.py`
