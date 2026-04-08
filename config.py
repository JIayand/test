# 浏览器配置
BROWSER_CONFIG = {
    "executable_path": "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "headless": False,
    "args": [
        "--no-sandbox",  # 关闭沙箱（Mac 非root用户必须）
        "--disable-gpu",  # 禁用GPU加速（避免新Mac显卡驱动冲突）
        "--disable-dev-shm-usage",  # 解决内存不足问题
        "--disable-web-security"  # 可选：关闭网页安全限制
    ]
}

# 页面配置
PAGE_CONFIG = {
    "url": "https://scale.dingtalk.com/projects/20895/data?reviewing=1",
    "login_wait_time": 60000,  # 登录等待时间（毫秒）
}

# 审核配置
REVIEW_CONFIG = {
    "loop_count": 5000,  # 循环次数
    "first_click_wait": 1000,  # 第一次点击前等待时间（毫秒）
    "second_click_wait": 800,  # 第二次点击前等待时间（毫秒）
    "final_wait_time": 5000,  # 最终等待时间（毫秒）
}

# XPath 配置
XPATH_CONFIG = {
    "first_element": '//*[@id="label-studio-dm"]/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div[2]/span[1]/span[1]',
    "accept_button": '//*[@id="label-studio-dm"]/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div/button/span'
}