import time
import pyautogui
from PIL import ImageChops
from rect_boundary import RectBoundary


def images_are_different(img1, img2, threshold=0.01):
    """
    判断图像是否发生变化

    通过计算所有像素偏离值的加权和，hist的横坐标越大，偏离越大，则赋予更多权重
    - pix_diff_weighted_sum: 像素偏离值线性加权和 = sigma(横坐标 * 像素个数)
    - pix_max_diff: 最差的情况，每个像素都偏离了最大值，那么hist所有的像素都应该集中在最后一个横坐标，
    也就是hist的length-1坐标

    Params:
    - img1: PIL.Image.Image 第一张图像
    - img2: PIL.Image.Image 第二张图像
    - threshold: float 阈值，默认 0.01
    """
        
    diff = ImageChops.difference(img1, img2)
    hist = diff.convert('L').histogram()

    pix_diff_weighted_sum = sum([i*hist[i] for i in range(len(hist))])

    pix_max_diff = (len(hist) - 1) * sum(hist) # 最大横坐标 * 像素总数
    
    diff_rate = pix_diff_weighted_sum / pix_max_diff
    
    # 如果差异超过阈值，返回img2
    return diff_rate > threshold


def handle_img(img):
    img.save('./screenshot.jpg', format='JPEG')


def run_screenshot_roop(region: tuple[int, int, int, int]):
    """
    循环截取屏幕，直到屏幕内容发生变化

    Params:
    -  region: tuple[int, int, int, int] 左上角x y 宽 高
    """
    previous_screenshot = pyautogui.screenshot(region=region)
    
    while True:
        time.sleep(1)  # 每隔1秒截取一次屏幕    
        current_screenshot = pyautogui.screenshot(region=region)
        if images_are_different(previous_screenshot, current_screenshot):
            print("Screen content changed!")
            handle_img(current_screenshot)
            break
        previous_screenshot = current_screenshot


if __name__ == "__main__":
    rect = RectBoundary(scale_factor=100)

    region = (
        rect.rect_params['x'], 
        rect.rect_params['y'], 
        rect.rect_params['width'], 
        rect.rect_params['height']
    )

    run_screenshot_roop(region)

