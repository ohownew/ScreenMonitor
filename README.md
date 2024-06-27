# ScreenMonitor

A Python tool to monitor screen changes and handle screenshots when changes are detected. This tool allows users to select a region of the screen to monitor, and upon detecting changes in that region, it can save the screenshot for further processing.

## Features

- Select a region of the screen to monitor using a graphical interface.
- Continuously monitor the selected region for changes.
- Save the screenshot when changes are detected.
- Potential for future enhancements like notifications via email, QQ, WeChat, etc.

## Requirements
- `Python>=3.9`
- `pynput`
- `pyautogui`
- `Pillow`

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/screen-monitor-tool.git
    cd screen-monitor-tool
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
