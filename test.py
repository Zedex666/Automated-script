# 如果闪退导致运行失败，解决方法：去应用设置里把______开启
import time

from appium import webdriver
from appium.options.android import UiAutomator2Options


APPIUM_SERVER_URL = "http://127.0.0.1:4723"


def main():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = "15"
    options.device_name = "459c8df8"
    options.udid = "459c8df8"
    options.app_package = "com.microsoft.emmx"
    options.app_activity = "com.microsoft.ruby.Main"

    driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
    try:
        time.sleep(10)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
