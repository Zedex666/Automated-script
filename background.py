# 如果闪退导致运行失败，解决方法：去应用设置里把______开启
import time

from appium import webdriver
from appium.options.android import UiAutomator2Options


# Appium Server 地址，默认在本机 4723 端口运行
APPIUM_SERVER_URL = "http://127.0.0.1:4723"


def main():
    # 创建 UiAutomator2 选项对象，用于配置 Android 自动化会话参数
    options = UiAutomator2Options()
    options.platform_name = "Android"               # 目标平台：Android
    options.platform_version = "15"                 # 目标系统版本：Android 15
    options.device_name = "459c8df8"                # 设备名称（ADB devices 中显示的设备名）
    options.udid = "459c8df8"                       # 设备唯一标识符，用于定位连接到电脑的特定设备
    options.app_package = "com.microsoft.emmx"      # 要启动的应用包名（Microsoft Edge 浏览器）
    options.app_activity = "com.microsoft.ruby.Main"  # 要启动的应用入口 Activity

    # 连接 Appium Server 并创建会话，在设备上启动 Edge 浏览器
    driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)

    print("----------")
    driver.background_app(5)  # 将应用置于后台运行 5 秒，便于观察应用是否成功启动
    print("----------")

    try:
        # 等待 10 秒，便于观察应用是否成功启动
        time.sleep(5)
    finally:
        # finally 保证无论是否发生异常，都会关闭会话、释放资源
        driver.quit() # 关闭当前驱动对象


# 脚本入口：直接运行此文件时执行 main() 函数
if __name__ == "__main__":
    main()
