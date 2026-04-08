from playwright.sync_api import sync_playwright
from config import BROWSER_CONFIG, PAGE_CONFIG, REVIEW_CONFIG, XPATH_CONFIG

with sync_playwright() as p:
    browser = p.chromium.launch(
        # 需要替换为真实chrome安装路径
        executable_path=BROWSER_CONFIG["executable_path"],
        headless=BROWSER_CONFIG["headless"],
        # 关闭不必要的安全限制，适配 macOS
        args=BROWSER_CONFIG["args"]
    )

    page = browser.new_page()
    # 替换为审核的链接
    page.goto(PAGE_CONFIG["url"])
    # 等待指定时间 用于扫码登录
    page.wait_for_timeout(PAGE_CONFIG["login_wait_time"])
    # 循环审核
    for i in range(REVIEW_CONFIG["loop_count"]):
        # 根据xpath查找节点
        element = page.locator(XPATH_CONFIG["first_element"])
        #点击
        # 等待指定时间 有效
        page.wait_for_timeout(REVIEW_CONFIG["first_click_wait"])
        element.click()
        # 根据xpath查找节点 接受
        element = page.locator(XPATH_CONFIG["accept_button"])
        # 等待指定时间
        page.wait_for_timeout(REVIEW_CONFIG["second_click_wait"])
        element.click()
    # 关闭浏览器
    # 等待指定时间
    page.wait_for_timeout(REVIEW_CONFIG["final_wait_time"])
    browser.close()
